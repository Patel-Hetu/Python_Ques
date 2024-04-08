'''Write a function squareRoot(x, epsilon) that uses bisection search to return a number y that is close enough to the square root of x, so that abs(y**2 - x) < epsilon. Try out the function in a program to verify that it works properly.'''

def squareRoot(x, epsilon):
    low = 0
    high = max(1, x)
    mid = (low + high) / 2
    while abs(mid**2 - x) >= epsilon:
        if mid**2 < x:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2
    return mid

x = float(input("Enter a number to find the square root of: "))
epsilon = float(input("Enter the maximum difference between the square of the mid and x: "))
y = squareRoot(x, epsilon)
print("The square root of", x, "is approximately", y)

