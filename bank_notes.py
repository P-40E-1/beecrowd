#1018
'''In this problem you have to read an integer value and calculate the smallest possible 
   number of banknotes in which the value may be decomposed. The possible banknotes are 100,
   50, 20, 10, 5, 2 and 1. Print the read value and the list of banknotes.'''

a = int(input())
print(a)
for i in [100,50,20,10,5,2,1]:
    print(f'{int(a // i)} nota(s) de R$ {i},00')
    a = a % i