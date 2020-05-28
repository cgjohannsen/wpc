import sys

with open('std', 'r') as f:
	std = f.read()

k = 8
hashes = [0]*(len(std)-k)

for i in range(0, len(std)-k):
	hashes.append(hash(std[i:i+k]))

win_size = 8
hash_buffer = [0]*win_size

for i in range(0, win_size)
	hash_buffer[i] = sys.maxsize

while cond:
	r = (r + 1) % win_size
	if m == r:
		# previous min no longer in window/buffer 
		# ...
	else:
		# previous min is still min
		#...


	
