# 1. Some builtin Types
import math

def f():
    print("This is a user-defined function")
    return 42

print("Some basic types in Python:")
print(type(2)) # int
print(type(2.2)) # float
print(type("2.2")) # str (string)
print(type(2 < 2.2)) # bool (boolean)
print(type(math)) # module
print(type(math.tan)) # builtin_function_or_method ("function" in Brython)
print(type(f)) # function (user-defined function)
print(type(type(42))) # type


print("#####################################################")
print("And some other types we will see later in the course...")
print(type(Exception())) # Exception
print(type(range(5))) # range
print(type([1,2,3])) # list
print(type((1,2,3))) # tuple
print(type({1,2})) # set
print(type({1:42})) # dict (dictionary or map)
print(type(2+3j)) # complex (complex number) (we may not see this type)


# 2. Some Builtin Constants
print("Some builtin constants:")
print(True)
print(False)
print(None)
print("And some more constants in the math module:")

print(math.pi)
print(math.e)


# 3. Some Builtin Functions
print("Type conversion functions:")
print(bool(0)) # convert to boolean (True or False)
print(float(42)) # convert to a floating point number
print(int(2.8)) # convert to an integer (int)

print("And some basic math functions:")
print(abs(-5)) # absolute value
print(max(2,3)) # return the max value
print(min(2,3)) # return the min value
print(pow(2,3)) # raise to the given power (pow(x,y) == x**y)
print(round(2.354, 1)) # round with the given number of digits


# 4. Types Affect Semantics
print(3 * 2)
print(3 * "abc")
print(3 + 2)
print("abc" + "def")
# print(3 + "def")


# 5. Integer Division
print("The / operator does 'normal' float division:")
print(" 5/3 =", ( 5/3))
print()
print("The // operator does integer division:")
print(" 5//3 =", ( 5//3))
print(" 2//3 =", ( 2//3))
print("-1//3 =", (-1//3))
print("-4//3 =", (-4//3))


# 6. The Modulus or Remainder Operator (%)
print(" 6%3 =", ( 6%3))
print(" 5%3 =", ( 5%3))
print(" 2%3 =", ( 2%3))
print(" 0%3 =", ( 0%3))
print("-4%3 =", (-4%3))
#print(" 3%0 =", ( 3%0))


# Verify that (a%b) is equivalent to (a - (a//b)*b):
def mod(a, b):
    return a - (a//b)*b
print(41%14, mod(41,14))
print(14%41, mod(14,41))
print(-32%9, mod(-32,9))
print(32%-9, mod(32,-9))


# 7. Operator Order (Precedence and Associativity)
print("Precedence:")
print(2+3*4) # prints 14, not 20
print(5+4%3) # prints 6, not 0 (% has same precedence as *, /, and //)
print(2**3*4) # prints 32, not 4096 (** has higher precedence than *, /, //, and %)

print()

print("Associativity:")
print(5-4-3) # prints -2, not 4 (- associates left-to-right)
print(4**3**2) # prints 262144, not 4096 (** associates right-to-left)


# 8. Approximate Values of Floating-Point Numbers
print(0.1 + 0.1 == 0.2) # True, but...
print(0.1 + 0.1 + 0.1 == 0.3) # False!
print(0.1 + 0.1 + 0.1) # prints 0.30000000000000004 (uh oh)
print((0.1 + 0.1 + 0.1) - 0.3) # prints 5.55111512313e-17 (tiny, but non-zero!)


# Equality Testing with almostEqual:
print("The problem....")
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2) # False (never use == with floats!)

print()
print("The solution...")
epsilon = 10**-10
print(abs(d2 - d1) < epsilon) # True!

print()
print("Once again, using a useful helper function, almostEqual:")
def almostEqual(d1, d2):
    epsilon = 10**-10
    return (abs(d2 - d1) < epsilon)

d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2) # still False, of course
print(almostEqual(d1, d2)) # True, and now packaged in a handy reusable function!


# 9. Short-Circuit Evaluation
def yes():
    return True
def no():
    return False
# def crash():
#   return 1/0 # crashes!

print(no() and crash()) # Works!
print(crash() and no()) # Crashes!
print (yes() and crash()) # Never runs (due to crash), but would also crash (without short-circuiting)


# Once again, using the "or" operator:
def yes():
    return True
def no():
    return False
def crash():
    return 1/0 # crashes!

print(yes() or crash()) # Works!
print(crash() or yes()) # Crashes!
print(no() or crash())  # Never runs (due to crash), but would also crash
                        # (without short-circuiting)


# Yet another example:
def isPositive(n):
    result = (n > 0)
    print("isPositive(",n,") =", result)
    return result

def isEven(n):
    result = (n % 2 == 0)
    print("isEven(",n,") =", result)
    return result

print("Test 1: isEven(-4) and isPositive(-4))")
print(isEven(-4) and isPositive(-4)) # Calls both functions
print("----------")
print("Test 2: isEven(-3) and isPositive(-3)")
print(isEven(-3) and isPositive(-3)) # Calls only one function!


# 10. type vs isinstance
# In general, you should use (isinstance(x, T)) instead of (type(x) == T)
# In fact, we will disallow type(x) in labs and hw's.
print(type("abc") == str)
print(isinstance("abc", str))

# We'll see better reasons for this when we cover OOP + inheritance later
# in the course. For now, here is one reason: say you wanted to check
# if a value is any kind of number (int, float, complex, etc).
# You could do:
def isNumber(x):
    return ((type(x) == int) or (type(x) == float)) # are we sure this is ALL kinds of
                                                    # numbers?

print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))

# But this is cleaner, and works for all kinds of numbers, including
# complex numbers for example:
import numbers
def isNumber(x):
    return isinstance(x, numbers.Number) # works for any kind of number
print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))