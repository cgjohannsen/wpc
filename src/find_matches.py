# find_matches.py
#
# author: Chris Johannsen
#
# This script takes input from the user defined csv file that was outputted
# from compile_prints.py and uses that data to find matches between files.
# The user can specify how many matches are significant

import argparse
import csv
	
d = 'Finds matches between fingerprints of files as outputted by compile_prints.py'
parser = argparse.ArgumentParser(description=d)
parser.add_argument('-m', '--matches', type=int, default=10, \
						help='number of matches between files that is significant')
parser.add_argument('-i', '--input', default='prints.csv', \
						help='csv file where fingerprint data is read from')
parser.add_argument('-o', '--output', default='matches', \
						help='file where output of significant matches will be written')
args = parser.parse_args()

num_significant = args.matches
input_file = args.input
output_file = args.output

fingerprints_prints = {}
fingerprints_filename = {}

with open(input_file, 'r') as prints_csv:
	reader = csv.reader(prints_csv)
	for row in reader:
		filename = row[0]
		fingerprints_filename[filename] = []
		for i in range(1, len(row)):
			fingerprints_filename[filename].append(row[i])
			if row[i] in fingerprints_prints:
				fingerprints_prints[row[i]].append(filename)
			else:
				fingerprints_prints[row[i]] = [filename]

match_totals = {}
for current_file, current_file_prints in fingerprints_filename.items():
	matches = {}
	for fingerprint in current_file_prints:
		if len(fingerprints_prints[fingerprint]) > 1:
			for filename in fingerprints_prints[fingerprint]:
				if current_file != filename:
					if not filename in matches:
						matches[filename] = 1
					else:
						matches[filename] += 1
	match_totals[current_file] = matches

with open(output_file, 'w') as match_file:
	for filename, matches in match_totals.items():
		significant = []
		for match, num_matches in matches.items():
			if num_matches >= num_significant:
				significant.append((match, num_matches))
		
		if len(significant) > 0:
			match_file.write('{}\n{}\n\n'.format(filename, significant))
			
