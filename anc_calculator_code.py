# --------------------------------------------------
# Programm by Yoatn
#
# Start date   07.11.2017   00:00
# End date     00.00.2017   00:00
#
# Description:
#
# --------------------------------------------------

import math

MethodOfMeasurement = input("Do you know angle between line? (y/n): ")

weight = int(input("The weight of the load (kg): "))
angle1 = int(input("Angle (°): "))
angle2 = angle1/2
angle3 = math.radians(angle2)

la = round(weight / math.cos(angle3) / 2)

print ("")
print ("The result:")
print ("The weight of the load: ", weight,"kg")
print ("Angle between ankers: ", str(angle1) + '°')
print ("Loag on the each anker: ", la,"kg")

