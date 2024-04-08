'''a program that reads four integers and prints "two pairs" if the input consists of two
matching pairs (in some order) and "not two pairs" otherwise. For example, 1 2 2 1 is "two
pairs", 1 2 2 3 is "not two pairs", and 2 2 2 2 is "two pairs".'''


num1 = int(input("Enter the First Value: "))
num2 = int(input("Enter the Second Value: "))
num3 = int(input("Enter the Third Value: "))
num4 = int(input("Enter the Fourth Value: "))

if num1 == num2 or num2 == num3 or num3 == num4 or num4 == num1:
    print("The entered numbers are in a pair of two.")
else:
    print("The entered numbers are not in a pair of two.")