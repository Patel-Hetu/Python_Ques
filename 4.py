'''a program that reads three numbers and prints "all the same" if they are all the same,
"all different" if they are all different, and "neither" otherwise.'''


num1 = int(input("Enter the first value: "))
num2 = int(input("Enter the second value: "))
num3 = int(input("Enter the third value: "))

if num1 == num2 == num3:
    print("All the entered values are the same.")
elif num1 != num2 and num2 != num3 and num3 != num1:
    print("All the entered values are different.")
elif num1 != num2 or num2 != num3 or num3 != num1:
    print("Neither.")
