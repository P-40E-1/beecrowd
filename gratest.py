#1013
'''Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:'''

import math
value = list(input().split())
a,b,c = value
first_two = (int(a) + int(b) + abs(int(a) - int(b))) / 2
last_two = (int(first_two) + int(c) + abs(int(first_two) - int(c))) / 2
print('%d eh o maior'%last_two)