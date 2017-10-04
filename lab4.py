import re

hand = open('mbox-short.txt')
for line in hand:
    if re.findall('^From', line):
    	print(line)
for line in hand:
	host = re.findall("^From (.*)@[^ ]*", line)
	print(host)

