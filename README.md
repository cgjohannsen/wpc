# Winnowing Plagiarism Checker

This set of scripts seeks to implement the winnowing algorithm presented and used by MOSS (http://theory.stanford.edu/~aiken/moss/) in order to effectively notify of potential cases of code plagiarism.

http://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf

## HowTo

Use the src/compile_prints.py and src/find_matches.py scripts as directed in their usage statements or follow below.

First use the src/compile_prints.py script to create a csv file of fingerprints for each file in the user specified directory. As input to this script, give it a valid directory path where the code is stored and a list of usernames. This list should be delimited by a ' ', ',', or '\\n'. The directory should hold subdirectories which are each associated with a different username, this is how to program determines which file is associated with what username. 

Once the fingerprints are outputted to some csv file, use the src/find_matches.py script to output a file that shows the number of fingerprint matches between files. One can determine the level of granularity by setting how many matches should be found to be considered significant and reported to the user.
