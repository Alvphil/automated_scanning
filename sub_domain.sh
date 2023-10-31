#!/bin/bash
File="domains.txt"
current_date=$(date +"%Y_%m_%d")
Lines=$(cat $File)
for Line in $Lines
do
    mkdir ./$Line
    export TARGET="$Line"
    cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "./${TARGET}/${source}_${TARGET}";done
    find ${TARGET}/ -name "*.json" -type f | xargs cat | jq -r '.hosts[]' 2>/dev/null | cut -d':' -f 1 | sort -u > "${TARGET}_theHarvester.txt"
    rm ${TARGET}/ -r
done
cat *_theHarvester.txt > complete_list.txt
rm *_theHarvester.txt