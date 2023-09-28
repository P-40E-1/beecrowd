#1015
'''Read the four values corresponding to the x and y axes of two 
   points in the plane, p1 (x1, y1) and p2 (x2, y2) and 
   calculate the distance between them, showing four 
   decimal places after the comma, according to the formula:'''

import math

x1,y1 = list(map(float,input().split(" ")))
x2,y2 = list(map(float,input().split(" ")))
Distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print('%.4f'%Distance)