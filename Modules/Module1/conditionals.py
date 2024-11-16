# 1. If statement

def f(x):
    print("A", end=" ")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    print("D")

f(0)
f(1)


# A more interesting example:
# These examples define abs(n), which is a nice example here, but it is
# also a builtin function, so you do not need to define it to use it.
def abs1(n):
    if (n < 0):
        n = -n
    return n

# again, with same-line indenting

def abs2(n):
    if (n < 0): n = -n # only indent this way for very short lines (if at all)
    return n

# again, with multiple return statements

def abs3(n):
    if (n < 0):
        return -n
    return n

# aside: you can do this with boolean arithmetic, but don't!
def abs4(n):
    return (n < 0)*(-n) + (n>=0)*(n) # this is awful! now show that they all work properly:

print("abs1(5) =", abs1(5), "and abs1(-5) =", abs1(-5))
print("abs2(5) =", abs2(5), "and abs2(-5) =", abs2(-5))
print("abs3(5) =", abs3(5), "and abs3(-5) =", abs3(-5))
print("abs4(5) =", abs4(5), "and abs4(-5) =", abs4(-5))


# 2. if-else statement
def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    else:
        print("D", end="")
        if (x == 1):
            print("E", end="")
        else:
            print("F", end="")
    print("G")

f(0)
f(1)
f(2)


# Revisiting abs(n):
def abs5(n):
    if (n >= 0):
        return n
    else:
        return -n

# or, if you prefer...

def abs6(n):
    if (n >= 0):
        sign = +1
    else:
        sign = -1
    return sign * n

print("abs5(5) =", abs5(5), "and abs5(-5) =", abs5(-5))
print("abs6(5) =", abs6(5), "and abs6(-5) =", abs6(-5))


# 3. if-else expression
# if-else expression (not an if-else statement!)

def abs7(n):
    return n if (n >= 0) else -n

print("abs7(5) =", abs7(5), "and abs7(-5) =", abs7(-5))


# 4. if-elif-else statement
    def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    elif (x == 1):
        print("D", end="")
    else:
        print("E", end="")
        if (x == 2):
            print("F", end="")
        else:
            print("G", end="")
    print("H")

f(0)
f(1)
f(2)
f(3)


# A more interesting example:
def numberOfRoots(a, b, c):
    # Returns number of roots (zeros) of y = a*x**2 + b*x + c
    d = b**2 - 4*a*c
    if (d > 0):
        return 2
    elif (d == 0):
        return 1
    else:
        return 0

print("y = 4*x**2 + 5*x + 1 has", numberOfRoots(4,5,1), "root(s).")
print("y = 4*x**2 + 4*x + 1 has", numberOfRoots(4,4,1), "root(s).")
print("y = 4*x**2 + 3*x + 1 has", numberOfRoots(4,3,1), "root(s).")

# Another example:
def getGrade(score):
    if (score >= 90):
        grade = "A"
    elif (score >= 80):
        grade = "B"
    elif (score >= 70):
        grade = "C"
    elif (score >= 60):
        grade = "D"
    else:
        grade = "F"
    return grade

print("103 -->", getGrade(103))
print(" 88 -->", getGrade(88))
print(" 70 -->", getGrade(70))
print(" 61 -->", getGrade(61))
print(" 22 -->", getGrade(22))