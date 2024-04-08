'''program that reads three numbers and prints "increasing" if they are in increasing
order, "decreasing" if they are in decreasing order, and "neither" otherwise. Here, "increasing"
means "strictly increasing", where each value is less than the next. The sequence 3 4 4 would
not be considered increasing, for example.'''


num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))

print("The three Numers entered are: ", num1," ", num2," ", num3)

if num1 > num2 and num2 > num3:
    print("The given numbers are in decreasing order.")
elif num1 < num2 and num2 < num3:
    print("The given numbers are in increasing order.")
else:
    print("Neither.")