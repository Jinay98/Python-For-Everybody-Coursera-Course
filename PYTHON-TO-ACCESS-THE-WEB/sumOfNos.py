import re

file = open('regex_sum_467622.txt')
sum = 0
numbers = 0
for line in file:
    line = line.rstrip()
    temp = re.findall('[0-9]+', line)
    if len(temp) > 0:
        for nos in temp:
            numbers += 1
            sum += int(nos)

print("The total numbers are ", numbers)
print('The sum of the numbers in text above is', sum)
