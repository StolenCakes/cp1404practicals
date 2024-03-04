"""
help(random.randint)
Help on method randint in module random:
randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

help(random.randrange)
Help on method randrange in module random:
randrange(start, stop=None, step=1, _int=<class 'int'>) method of random.Random instance
    Choose a random item from range(start, stop[, step]).

    This fixes the problem with randint() which includes the
    endpoint; in Python this is usually not what you want.
"""

# 1. For Line 1, what was the smallest number you could have seen, what was the largest? [print(random.randint(5, 20))]
print("""
smallest number = 5
largest number = 20
""")

# 2. For Line 2, what was the smallest number you could have seen, what was the largest? Could line 2 have produced a 4? [print(random.randrange(3, 10, 2))]
print("""
smallest number = 3
largest number = 9
No, line 2 cannot produce a 4 since the numbers generated have intervals of 2, starting from 3.
This means that any randomly generated value will come out as odd numbers.
""")

# 3. For Line 3, what was the smallest number you could have seen, what was the largest? [print(random.uniform(2.5, 5.5))]
print("""
smallest number = 2.5
largest number = 5.5
""")

# 4. Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
print(random.randint(1, 100))