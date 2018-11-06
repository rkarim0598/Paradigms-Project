f = open('_tv_database.py')

i = 0
for line in f:
	i += 1
	if line[0] == ' ':
		print(i)
