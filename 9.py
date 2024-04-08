''' a program that reads a temperature value and the letter C for Celsius or F for
Fahrenheit. Print whether water is liquid, solid, or gaseous at the given temperature at sea
level. '''


temp = int(input("Enter the temperature: "))

scale = input("Choose the scale( C or F ): ")

if scale == "C" or scale == "c":
    if temp <= 0:
        print("Water is in solid state.")
    elif temp >= 100:
        print("Water is in gaseous state.")
    else:
        print("Water is in liquid state.")
elif scale == "F" or scale == "f":
    if temp <= 0:
        print("Water is in solid state.")
    elif temp >= 212:
        print("Water is in gaseous state.")
    else:
        print("Water is in liquid state.")
else:
    print("Please enter a valid scale.")