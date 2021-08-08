# Celsius to Fahrenheit program
import math
def CtoF(c):
    f = (9 * c) / 5 + 32
    return f

c = None

while True:
    try:
        c = int(input("Please input temperature in Celsius degree: "))
        break
    except Exception:
        print("Please enter an integer, Bro!!!")
        print("-------------------------------")
        print()

print("Temperature in Fahrenheit is: "+ str(CtoF(c)) + "°F")