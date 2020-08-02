# compile_prints.py
#
# author: Chris Johannsen 
#
# This file walks through the user specified directory and finds all c files.
# These files are then stripped of various identifiers such that is will be
# good input for the winnowing algorithm.
# Fingerprints for each file are then created and stored in the prints.csv file
# by default

import argparse
import re
import os
import csv

import alg
import std

d = 'Creates sets of fingerprints for files using the winnowing algorithm' 
parser = argparse.ArgumentParser(description=d)
parser.add_argument('dir', help='directory where files to be fingerprinted are stored')
parser.add_argument('students', help='file where delimited list of students is stored\n' + \
										'valid delimiters include \' \', \',\', and \'\\n\'')
parser.add_argument('-e', '--extension', default='c', \
						help='file extension used to determine which files to fingerprint')
parser.add_argument('-o', '--output', default='prints.csv', \
						help='file where csv data will be written')
parser.add_argument('-k', '--kgram', default=20, type=int, \
						help='size of k-gram used in winnowing algorithm')
parser.add_argument('-w', '--windowsize', default=20, type=int, \
						help='window size used in winnowing algorithm')
args = parser.parse_args()

directory = args.dir
students_file = args.students
ext = args.extension
csv_file = args.output
k = args.kgram
w = args.windowsize

with open(students_file, 'r') as f:	
	students = re.split('[\n, ]', f.read())
stds = {}

# start by formatting our input to the winnowing algorithm
for root, dirs, files in os.walk(directory):
	for filename in files:
		if re.match('[a-zA-Z0-9-_]+\.'+ext, filename) and filename.endswith('.'+ext):
			
			for s in students:
				student = re.search(s, root)
				if student:
					student = s 
					break
			
			with open(root + '/' + filename, 'r') as f:
				file_text = f.read()

			standard = std.standardize(file_text, ext) 
			filename = student + '-' + re.sub('.c', '', filename)
			stds[filename] = standard

with open(csv_file, 'a', newline='') as prints_csv:
	writer = csv.writer(prints_csv)
	for filename, standard in stds.items():
		prints = alg.winnow(standard, k, w)
		writer.writerow([filename] + prints)

