'''program that reads an integer and prints how many digits it has by checking whether
the number is >= 10, >= 100, and so on. However, if the number is greater than a million, just
print "lots". If the number is negative, then first multiply it by -1.'''





num = int(input("Enter the Value: "))
pnum = 0
if num < 0:
    num = num * -1

if num < 10:
    print("The entered number has 1 digit.")
elif 10 <= num < 100:
    print("The entered number has 2 digits.")
elif 100 <= num < 1000:
    print("The entered number has 3 digits.")
elif 1000 <= num < 10000:
    print("The entered number has 4 digits.")
elif 10000 <= num < 100000:
    print("The entered number has 5 digits.")
elif 100000 <= num < 1000000:
    print("The entered number has 6 digits.")
elif num >= 1000000:
    print("The entered number is large.")
    