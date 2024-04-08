'''Write a function hello(name), which prints "Hello" followed by the value of name. 
For example, hello('Ahmad') would print "Hello Ahmad". Write a program that asks the 
user for their name, and then uses the function to greet the person.'''


name = input("Enter your first name: ")

def hello(name):
    print("Hello",name)
    
hello(name)