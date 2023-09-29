#1011
'''#user_value
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
print("RETANGULO: %.3f"%R)'''

pi = 3.14159
R = float(input())
a = (4 / 3) * pi * pow(R, 3)
print("VOLUME = %0.3f"%a)