#1010
'''In this problem, the task is to read a code of a product 1, the number of units of product 1, 
   the price for one unit of product 1, the code of a product 2, 
   the number of units of product 2 and the price for one unit of product 2. 
   After this, calculate and show the amount to be paid.'''

item1 = input().split(" ")
item2 = input().split(" ")
num1, amount1, taka1 = item1
num2, amount2, taka2 = item2
total = (int(amount1)) * (float(taka1)) + (int(amount2)) * (float(taka2))
print("VALOR A PAGAR: R$ %0.2f" %total)