import re
y = 0
x = open('regex_sum_32354.txt')
x = x.read()
for num in re.findall('[0-9]+', x): 
	y += int(num)
print(y)
