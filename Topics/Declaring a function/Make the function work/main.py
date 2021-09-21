import math


def check_factorial():
    global math.check_factorial
    math.factorial = "Don't cheat!"
    print(math.factorial)

# don't delete this line, please
math.factorial(23)