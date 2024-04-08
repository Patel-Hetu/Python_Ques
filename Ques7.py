'''Write a function biggestOdd(), which reads in numbers from the user until the user enters 0. Then the function returns (not prints) the largest odd number that was entered. For example, if the integers were: 10, 9, 7, 12, 2, 5, 15, 100, 90, 60, 0, then the program would return 15 as the largest odd number. Similarly, if the integers were -55, -33, -10, 100, -5, 0, then the program would return -33 as the largest odd number. If there is no odd number, then the function should return 0. Use the function in a program to check that it works.'''


def biggestOdd():
    largest_odd_num = 0
    while True:
        num = int(input("Enter a number or 0 to stop: "))
        if num == 0:
            break
        if num % 2 != 0 and num > largest_odd_num:
            largest_odd_num = num
    return largest_odd_num
#now calling the function by entering various values
largest_odd_num = biggestOdd()
if largest_odd_num != 0:
    print("The largest odd number entered is", largest_odd_num)
else:
    print("No odd numbers were entered.")
