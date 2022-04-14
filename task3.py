"""
The programmer: bandar abed alsalme
The Study Division:112

"""


weight = int(input("please enter the weight: "))

def convert(weight):
    return weight * 0.453


while weight < 0:
    if weight > 0:
        break
    else:
        print("you can't enter less than 0 or 0")
        weight = int(input("enter the weight again :"))

print("your weight from kg to pound is :",convert(weight))