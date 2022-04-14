"""
The programmer: bandar abed alsalme
The Study Division:112

"""

def triangle():
    for i in range(0, 5):
        for x in range(0 , i+1):
            print("* " , end="")
        print('\r')

if __name__ == "__main__":
    triangle()