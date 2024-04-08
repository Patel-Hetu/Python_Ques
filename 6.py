''' Repeat Exercise 5, but first ask the user whether "increasing/decreasing" should be "strict" or
"lenient". In lenient mode, the sequence 3 4 4 is "increasing", and the sequence 4 4 4 is both
increasing and decreasing.'''

num1 = int(input("Enter the First Value: "))
num2 = int(input("Enter the Second Value: "))
num3 = int(input("Enter the Third Value: "))


print("The entered numbers are: ",num1," ",num2," ",num3)

mode = input("Enter whether the mode should be strict or lenient: ")


if mode == "strict":
    if num1 > num2 and num2 > num3:
        print("The given numbers are in decreasing order.")
    elif num1 < num2 and num2 < num3:
        print("The given numbers are in increasing order.")
    else:
        print("Neither.")
elif mode == "lenient":
    if num1 > num2 and num2 == num3:
        print("The given numbers are in decreasing order.")
    elif num1 < num2 and num2 == num3:
        print("The given numbers are in increasing order.")
    elif num3 > num2 and num1 == num2:
        print("The given numbers are in increasing order.")
    elif num3 < num2 and num1 == num2:
        print("The given numbers are in decreasing order.")
    elif num1 == num2 == num3:
        print("The given numbers are in both increasing and decreasing.")
else:
        print("Please enter either strict or lenient.")

    