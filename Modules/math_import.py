from math import sqrt #importing only sqrt function not entire module

print("Sqaure Root : ",sqrt(9))


# ALIAS For Importing Modules

import math as m

cosine=m.cos(0)

print(cosine)


# ALIAS can be used for Importing Functions

from math import factorial as f

# you can import many functions from modules
# from math import factorial,log10,sqrt,sin



factorial_10=f(10)

print(factorial_10)

# import all function from a modules
from math import * #not best approaches
