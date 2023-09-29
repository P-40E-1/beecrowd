#1008
'''Write a program that reads an employee's number, his/her worked hours number in a 
   month and the amount he received per hour. Print the employee's number and salary 
   that he/she will receive at end of the month, with two decimal places.

Don’t forget to print the line's end after the result, otherwise you will receive “Presentation Error”.
Don’t forget the space before and after the equal signal and after the U$.'''

N = int(input())
H = float(input())
S = float(input())
salary = (H*S)
print("NUMBER =",N)
print("SALARY = U$ %.2f"%salary)