'''Write a function perfectcube(n), which returns True if n is a perfect cube and returns False otherwise. Notice that this function is not printing anything, but rather returning True or False. The function must use exhaustive enumeration to check if n is a perfect cube. That means checking if 0**3 is n or 1**3 is n or 2**3 is n, and so on, up to where it is pointless to check further. (Instead of n, you might be checking against abs(n), since for example, -125 is a perfect cube. Use the function in a program where you ask the user for n and you print a statement like "Yes, that is a perfect cube" or "No, that number is not a perfect cube", as appropriate.'''

num = int(input("Enter a number to check whether its a perfect cube or not: "))

def perfectcube(n):
    i = 0
    while i**3 <= abs(n):
        if i**3 == abs(n):
            return True
        i += 1
    return False


if perfectcube(num):
    print("Yes,",num,"is a perfect cube")
else:
    print("No,",num,"is not a perfect cube")
