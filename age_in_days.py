#1020
'''Read an integer value corresponding to a person's age (in days) and print it in years, 
    months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”'''

dia = int(input())
ano = dia // 365
dia = dia % 365
mes = dia // 30
dia = dia % 30
print(f'{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)')