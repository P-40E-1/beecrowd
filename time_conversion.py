#1019
'''Read an integer value, which is the duration in seconds of 
   a certain event in a factory, and inform it expressed 
   in hours:minutes:seconds.'''

a = int(input())
h = a // 3600
a = a % 3600
m = a // 60
s = a % 60
print(f'{h}:{m}:{s}')