#1009
'''Make a program that reads a seller's name, his/her fixed salary and the sale's total made by 
   himself/herself in the month (in money). Considering that this seller receives 15% over all products sold, 
   write the final salary (total) of this seller at the end of the month , with two decimal places.

- Don’t forget to print the line's end after the result, otherwise you will receive “Presentation Error”.

- Don’t forget the blank spaces.'''

#name input
A_str=(input())
#fixed salary
S=float(input())
#sales total made by himself
H=float(input())
P=((H/100)*15)
Final=S+P
print("TOTAL = R$% .2f"%Final)