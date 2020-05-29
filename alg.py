import sys
import hashlib

def winnow(std, k, win_size):
	
	hasher = hashlib.blake2b(digest_size=8)

	hashes = [0]*(len(std)+1)
	right = win_size - 1
	minimum = 0
	fingerprints = []

	for i in range(0, len(std)+1):
		hashes[i] = sys.maxsize

	while right < len(std):
		right = right + 1
		to_hash = std[right - win_size:right].encode('utf-8')
		hasher.update(to_hash)	
		hashes[right] = int.from_bytes(hasher.digest(), 'big')
		if minimum == right:
			# previous min no longer in window 
			for i in range(right - win_size, right):
				if hashes[i] < hashes[minimum]:
					minimum = i
			fingerprints.append(hashes[minimum])
		else:
			# previous min is still min
			if hashes[right] < hashes[minimum]:
				minimum = right
				fingerprints.append(hashes[minimum])

	return fingerprints
