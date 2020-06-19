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

k = 20 # k-gram length
w = 20 # window size

for key, val in stds.items():
	prints = alg.winnow(val, k, w)
	for p in prints:
		if p[0] in fingerprints:
			fingerprints[p[0]].append((key, p[1]))
		else:
			fingerprints[p[0]] = [(key, p[1])]

total = {}

with open('matches', 'w') as f:
	for key, val in stds.items():
		prints = alg.winnow(val, k, w)
		matches = {}
		for p in prints:
			if len(fingerprints[p[0]]) > 1:
				for hits in fingerprints[p[0]]:
					if not hits[0] == key:
						if not hits[0] in matches:
							matches[hits[0]] = 1
						else:
							matches[hits[0]] += 1
		total[key] = matches
	for key, val in total.items():
		significant = {}
		for match, hits in val.items():
			if hits > 5:
				significant[match] = hits
				f.write('{}\n{}\n\n'.format(key, significant))

	

"""
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
