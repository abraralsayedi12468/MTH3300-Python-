#******************************************************************************
# ryse.py
#******************************************************************************
# Name: Abrar Alsayedi 
#******************************************************************************
# Overall remarks (not to replace in-line comments):
#
#
#
#

import math

hq_lat = 40.740230
hq_long = -73.983766

car1_lat = float(input('Enter Latitude of Car 1: '))
car1_long = float(input('Enter Longitude of Car 1: '))
car1_occ = input('Car 1 occupied (y/n): ')
car2_lat = float(input('Enter Latitude of Car 2: '))
car2_long =float(input('Enter Longitude of Car 2: '))
car2_occ = input('Car 2 occupied (y/n): ')

delta_lat1 = (car1_lat - hq_lat) * 111.048
delta_long1 = (car1_long - hq_long) * 84.515
delta_lat2 = (car2_lat - hq_lat) * 111.048
delta_long2 = (car2_long - hq_long) * 84.515

distance1 = math.sqrt(delta_lat1**2 + delta_long1**2)
distance2 = math.sqrt(delta_lat2**2 + delta_long2**2)

print('CAR 1 DISTANCE: ')
print(f'{distance1:.6f}')

print('CAR 2 DISTANCE: ')
print(f'{distance2:.6f}')

if car1_occ == 'n' and distance1 < 8 and car2_occ == 'n' and distance2 < 8:
    if distance1 < distance2:
        print('CAR 1')
    else:
        print('CAR 2')
elif car1_occ == 'n' and distance1 < 8:
    print('CAR 1')
elif car2_occ == 'n' and distance2 < 8:
    print('CAR 2')
else:
    print('NEITHER')
    
