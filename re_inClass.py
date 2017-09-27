import re

hand = open('mbox-short.txt')
num = []
num2 = []
for line in hand:
    line = line.rstrip()
    if re.findall('X-DSPAM-Confidence', line):
    	x = re.findall('^X-DSPAM-Confidence:.(\S*)', line)
    	num.append(x)
for x in num:
	if len(x) > 0:
		var = x[0]
		num2.append(float(var))
values = "Number of Values = " + str(len(num2))
maximum = "Maximum = " + str(max(num2))
minimum = "Minimum = " + str(min(num2))
average = "Average = " + str((sum(num2)/len(num2)))
print(values)
print(maximum)
print(minimum)
print(average)

    	