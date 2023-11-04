#!/bin/bash
File="domains.txt"
current_date=$(date +"%Y_%m_%d")
Lines=$(cat $File)
mkdir harvester_output
let "i = 1"
for Line in $Lines
do
    let "j = 1"
    export TARGET="$Line"
    cat sources.txt \
    | while read source; 
    do
        docker run \
            --rm \
            --mount type=bind,source="$HOME/.theHarvester/api-keys.yaml",target="/app/api-keys.yaml" \
            --mount type=bind,source="$(pwd)/harvester_output",target=/data\
            --entrypoint "/app/theHarvester.py" \
            theharvester -d "${TARGET}" -b $source -f "/data/${i}${j}_${source}_${TARGET}";\
    let "j += 1"
done
let "i += 1"
done
find harvester_output/ -name "*.json" -type f | xargs cat | jq -r '.hosts[]' 2>/dev/null | cut -d':' -f 1 | sort -u > "complete_theHarvester.txt"
rm -rf harvester_output 
cat *_theHarvester.txt > complete_list.txt
rm *_theHarvester.txt