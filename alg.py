import sys
import hashlib

def hash_kgram(k, h):
	h.update(k)
	return int.from_bytes(h.digest(), 'big')

def winnow(std, k, win_size):	
	hasher = hashlib.blake2b(digest_size=8)
	hashes = [0]*(win_size)	# circular buffer
	right = -1	# rightmost item we're considering from std
	minimum = 0	# minimum hash value in window
	fingerprints = []	# tuples of fingerprints and respective line number

	for i in range(0, win_size):
		hashes[i] = sys.maxsize

	i = 0			# index std
	line_number = 0 # need to keep track for results
	while i < len(std)-k:
		right = (right + 1) % win_size
		hashes[right] = hash_kgram(std[i:i+k].encode('utf-8'), hasher) 
		if minimum == right:
			# previous min no longer in window
			# iterate backwards through window to get rightmost minimum
			j = (right - 1) % win_size
			while j != right:
				if hashes[j] < hashes[minimum]:
					minimum = j
				j = (j - 1 + win_size) % win_size
			fingerprints.append((hashes[minimum], line_number)) 
		else:
			# previous min is still min
			if hashes[right] < hashes[minimum]:
				minimum = right
				fingerprints.append((hashes[minimum], line_number))
		i += 1
		if std[i] == '\n':
			line_number += 1
	
	return fingerprints
