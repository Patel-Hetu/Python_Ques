'''a program that translates a letter grade into a number grade. Letter grades are A, B,
C, D, and F, possibly followed by + or -. Their numeric values are 4, 3, 2, 1, and 0. There is no F+
or F-. The symbol + increases the numeric value by 0.3, and the symbol - decreases it by 0.3. For
example: Enter a letter grade: B-The numeric value of B- is 2.7.'''

grade = input("Enter your grade: ")

ans = "The numberic grade is "

if grade == "A+":
    a = 4 + 0.3
    print(ans,a)
elif grade == "A":
    print(ans,"4")
elif grade == "A-":
    A = 4 - 0.3
    print(ans,A)
elif grade == "B+":
    b = 3 + 0.3
    print(ans,b)
elif grade == "B":
    print(ans,"3")
elif grade == "B-":
    B = 3 - 0.3
    print(ans,B)
elif grade == "C+":
    c = 2 + 0.3
    print(ans,c)
elif grade == "C":
    print(ans,"2")
elif grade == "C-":
    C = 2 - 0.3
    print(ans,C)
elif grade == "D+":
    d = 1 + 0.3
    print(ans,d)
elif grade == "D":
    print(ans,"1")
elif grade == "D-":
    D = 1 - 0.3
    print(ans,D)
else:
    print("Please enter a valid grade.")