#--------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   00:00
# End date     00.00.2017   00:00
#  
# Description:
#
#--------------------------------------------------

import math

MethodOfMeasurement = input("Do you know angle between line? (y/n): ")

if MethodOfMeasurement == 'y':

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

if MethodOfMeasurement == 'n':
    weight = int(input("The weight of the load (kg): "))
    LineA = int(input("LineA (cm): "))
    LineB = int(input("LineB (cm): "))
    DistBetweenLine = int(input("Distance Between Ankers (cm): "))

    CosA = (LineA ** 2 + LineB ** 2 - DistBetweenLine ** 2) / 2 * LineA * LineB
    print(CosA)
    la = round(weight / CosA / 2)

    print("")
    print("The result:")
    print("The weight of the load: ", weight, "kg")
    # print("Angle between ankers: ", str(angle1) + '°')
    print("Loag on the each anker: ", la, "kg")
