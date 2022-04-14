"""
The programmer: bandar abed alsalme
The Study Division:112

"""

the_name = str(input("please enter your name :"))
the_char = str(input("what is the char do you want me search about : "))

def check(char):
    if the_name.count(the_char) == 1:
        return f"your name is : {the_name} , and the char is : {the_char} and is repeated {the_name.count(the_char)} time"
    else: 
        return f"your name is : {the_name} , and the char is : {the_char} and is repeated {the_name.count(the_char)} times"

print(check(the_char))