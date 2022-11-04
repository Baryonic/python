import math as mat#built in module
eys= mat.e

from math import factorial
print(factorial(5))#note that math.factorial is not required due to the import

import time
print(time.gmtime())

def f1():
    print("f1() called")

def f2():
    print("f2() tries to call f1()")
    f1()





