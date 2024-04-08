'''Write a function hello(firstname, lastname), which, for example, if called with hello('John', 'Smith'), would print two lines:Hello John Smith Hello Smith, JohnUse the function in a program where you ask the user for first and last name and then call the function.'''

lastname = input("Enter your last name: ")
firstname = input("Enter your first name: ")

def hello(firstname, lastname):
    print("Hello",firstname,lastname)
    print("Hello",lastname,",",firstname)
    
hello(firstname, lastname)