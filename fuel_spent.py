#1017
''' this program calculates and shows the amount of spent fuel liters on a trip, using a car that does 12 Km/L'''

time = int(input())
avarage_speed = int(input())
distance_travelled = avarage_speed / 12
spend_fuel = distance_travelled * time
print('%.3f'%spend_fuel)