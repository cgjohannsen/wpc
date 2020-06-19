# Winnowing Plagiarism Checker

This script seeks to implement the winnowing algorithm presented and used by MOSS (http://theory.stanford.edu/~aiken/moss/) in order to effectively notify of potential cases of code plagiarism.

http://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf

## HowTo

The find_c_match.py script will crawl through a directory of all students' work and find the c files. From there it strips out all "unimportant" bits (whitespace, punctuations, etc.) and then runs this through the winnowing algorithm from above to find similarities. All similiarites above a certain threshold are recorded in the 'match' output file.
