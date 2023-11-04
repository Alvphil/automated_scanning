# automated_scanning
Tool to automate verification of websites that are up or what code they are serving

To run this program you will need to set up a couple of items:

- Have theHarvester installed using docker. https://github.com/laramies/theHarvester
- have a source file
- have a file for the domains to check

TODO:
- [ ] Automatic upload of results to a private git repo.
- [x] take pictures of the sites that resolves.


What I this tool is supposed to do is to, use the tool theHarvester on a regular basis, clean up the results from that scan, and then go through all the (new?) sites that the tool found and check what kind of respons it receives.

The sites where a server gives a respons get logged, and in a document and pushed up to git for manual? review of new sites.

