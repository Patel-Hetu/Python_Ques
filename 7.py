'''a program that reads in three integers and prints "in order" if they are sorted in order
either ascending or descending, or "not in order" otherwise. For example, 1 2 3 is "in order", 1
5 2 is "not in order", 5 2 1 is "in order", and 1 2 2 is "in order".'''


num1 = int(input("Enter the First Value: "))
num2 = int(input("Enter the Second Value: "))
num3 = int(input("Enter the Third Value: "))

if num1 > num2 > num3 or num1 < num2 < num3 :
    print("The entered values are in order.")
elif num1 > num2 and num2 == num3:
    print("The entered values are in order.")
elif num1 < num2 and num2 == num3:
    print("The entered values are in order.")
elif num3 > num2 and num1 == num2:
    print("The entered values are in order.")
elif num3 < num2 and num1 == num2:
    print("The entered values are in order.")
elif num1 == num2 == num3:
    print("The entered values are in order.")
else:
    print("The entered values are not in order.")
    