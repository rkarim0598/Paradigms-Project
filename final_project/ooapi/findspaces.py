import sys

f = open(sys.argv[1])

i = 0
for line in f:
	i += 1
	if line[0] == ' ':
		print(i)
