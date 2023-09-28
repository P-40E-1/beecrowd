#1014
'''Calculate a car's average consumption being provided the total 
   distance traveled (in Km) and the spent fuel total (in liters).'''

X = int(input())
Y = "{:.1f}".format(float(input()))
conjumption = int(X) / float(Y)
print("%.3f km/l"%conjumption)