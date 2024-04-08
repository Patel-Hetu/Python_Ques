'''Write a function biggestBuried(s), which the parameter s is a string, and the function returns the largest integer buried in the string. If there is no integer inside the string, then return 0. For example, biggestBuried('abcd51kkk3kk19ghi') would return 51, and biggestBuried('kkk32abce@@-33bb14zzz') would return 33, since the '-' character is treated like any other non digit. Note that a character is a digit if it is greater than or equal to '0' and less than or equal to '9'. Alternatively, you can use string.isdigit() to check if the string is a digit.'''

def biggestBuried(string):
    largest_int_burried = 0
    current_int = ""
    for num in string:
        if num.isdigit():
            current_int += num
        else:
            if current_int != "":
                num = int(current_int)
                if num > largest_int_burried:
                    largest_int_burried = num
            current_int = ""
    if current_int != "":
        num = int(current_int)
        if num > largest_int_burried:
            largest_int_burried = num
    return largest_int_burried

string = input("Enter a string: ")
largest_int_burried = biggestBuried(string)
if largest_int_burried != 0:
    print("The largest integer buried in the string is", largest_int_burried)
else:
    print("No integers are found in the string.")
