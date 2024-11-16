# Hello world in Python
print("Hello, World!")
print('Hello, World!')

# Single quotes and double quotes are interchangeable

# Function 
def helloWorld():
    print("Hello, World!")

helloWorld()


# Python Comments
print("Hello World!")   # This is a comment
# print "What will this line do?"

#How comment multiple lines?
'''
This is how to comment multiple lines
Line one
Line two
Line three
'''

# Syntax Runtime, and Logical Errors
# Syntax Errors (Compile-Time Errors)
# print("Uh oh!)    # ERROR! missing close-quote

# Python output:
# SyntaxErrors: EOL while scanning string literal

# Runtime Errors ("Crash")
# print(1/0) # Error! Division by zero!

# Python output:
# ZeroDivisionError: integer division or module by zero

# Logical Errors (Compiles and Runs, but is Wrong!)
# print("2+2=5") # ERROR! Untrue!!!

# Python output:
# 2+2=5

# Basic Console Output
    # Basic print function
print("Carpe")
print("diem")

# Print on same line
print("Carpe", end=" ")
print("diem")

# Print multiple items
print("Carpe", "diem")

# Another Example:
print() # blank line

# Compute the hypotenuse of a right triangle
a = 3
b = 4
c = ((a**2) + (b**2)) ** 0.5
print("side a =", a)
print("side b =", b)
print("hypotenuse c =", c)

# Basic Console Input
# Input a string
name = input("Enter your name: ")
print("Your name is: ", name)

# Input a number (error!)
x = input("Enter a number: ")
# print("one half of ", x, "=", x/2)  # Error!

# Input a number with int()
x = int(input("Enter a number: "))
print("One half of", x, "=", x/2)


# Importing Modules
# Call without importing
# print(math.factorial(20)) # we did not first import the math module

# Python output:
# NameError: name 'math' is not defined
    

# Call with importing
import math
print(math.factorial(20)) # much better ...

# What does a module export?
# list all the functions in the math module
# (ignore items in __double_underscores__)
import math
print(dir(math))

# even better, read the online docs!
import webbrowser
input("Hit enter to see the online docs for the math module.")
webbrowser.open("https://docs.python.org/3/library/math.html")
