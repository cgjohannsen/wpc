# find_c_matches.py
#
# author: Chris Johannsen 5/29/20
#
# This file walks through the lab-* directory and finds all c files.
# These files are then stripped of various identifiers such that is will be
# good input for the winnowing algorithm.
# Fingerprints for each file are then created and compared between documents

# TODO
# Remove unique variable names:
#	This will make the program robust to variable name changes.
#	All ints, chars, doubles, etc. should have generic variable names
#	for their respective data type
# Find optimal k and window size values:
#	Need to run some tests to find the value of k and window size
#	such that only meaningful similarities are caught

import string
import re
import os
import itertools

import alg

stds = {}

# start by formatting our input to the winnowing algorithm
for root, dirs, files in os.walk('./lab-9/'):
	for filename in files:
		if re.match('[a-zA-Z0-9-_]+\.c', filename) and filename.endswith('.c'):
			with open(root + '/' + filename, 'r') as f:
				std = f.read()

			# Remove:
			# case sensitivity
			# preprocessor directives
			# whitespace
			# punctuation
			# int main(int...

			std = std.lower()					
			std = re.sub(r'#.*\n', r'',  std)
			std = re.sub('int.*main.*(.*int.*argc.*,.*char.*argv.*)', r'', std)
			std = re.sub(r'[' + string.whitespace + string.punctuation + ']', r'', std)

			key = re.search('(?<=lab-9-).*', root).group() + '-' + re.sub('.c', '', filename)
			stds[key] = std

fingerprints = {}

for k, v in stds.items():
	fingerprints[k] = alg.winnow(v, 20, 20)

counts = []

# quick and dirty way to compare each files' fingerprints
with open('matches', 'w') as f:
	l = itertools.combinations(fingerprints.items(), 2)
	for comp in l:
		count = 0
		for i in range(0, len(comp[0][1])):
			for j in range(i, len(comp[1][1])):
				if comp[0][1][i] == comp[1][1][j]:
					count = count + 1
		if count > 3:
			f.write('{}\n{}\n{}\n\n'.format(comp[0][0], comp[1][0], count))
			counts.append(count)

"""
	for k0, v0 in fingerprints.items():
		count = 0
		for k1, v1 in fingerprints.items():
			for i in range(0, len(v0)):
				for j in range(i, len(v1)):
					if v0[i] == v1[j]:
						count = count + 1
			if count > 0:
				f.write('{}\n{}\n{}\n\n'.format(k0, k1, count))
				counts.append(count)
"""
print(counts)
