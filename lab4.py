import re

hand = open('mbox-short.txt')
for line in hand:
    x = re.findall('^From', line)
    print(x)
	#if re.findall('^From')
	#	print(line)    	

