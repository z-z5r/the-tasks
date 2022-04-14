"""
The programmer: bandar abed alsalme
The Study Division:112

"""


#the function is x**2 - 2y**2 = 1


for x in range(1 , 101):
    for y in range(1 , 101):
        if x**2 - 2*y**2 == 1:
            print("the numbers are :", x , ",", y)
