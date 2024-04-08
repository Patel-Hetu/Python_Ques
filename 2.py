'''program that reads a floating point number and prints "zero" if the number is zero.
Otherwise, it prints "positive" or "negative" (as appropriate). Add "small" if the absolute value
is less than 1, and add "large" if the absolute value is greater than 1000'''

num = float(input("Enter the Value: "))

if num == 0:
    print("The entered value is Zero.")
elif num > 0:
    if abs(num) < 1:
        print("The entered value is Small Positive Number.")
    elif abs(num) > 1000:
        print("The entered value is Large Positive Number.")
    else:
        print("The entered value is Positive Number.")
else:
    if abs(num) < 1:
        print("The entered value is Small Negative Number.")
    elif abs(num) > 1000:
        print("The entered value is Large Negative Number.")
    else:
        print("The entered value is Negative.")

