#1012
'''Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.'''

#user_value
value = list(map(float,input().split(" ")))
#determine pi value
pi = 3.14159
a,b,c = value
#equations
RT = .5 * a * c
C = pi * c * c
T = .5 * c * (a + b)
S = b * b
R = a * b
#print Areas
print("TRIANGULO: %.3f"%RT)
print("CIRCULO: %.3f"%C)
print("TRAPEZIO: %.3f"%T)
print("QUADRADO: %.3f"%S)
print("RETANGULO: %.3f"%R)