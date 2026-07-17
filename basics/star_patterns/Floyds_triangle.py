'''
Floyds Triangle

Problem Description:

You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, 
represented as a list of strings. 
Floyd's Triangle is a triangular array of natural numbers where the first row contains 1, 
the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on.
'''

def generate(n):
    pyr =[]
    current = 1
    for i in range (1,n+1):
        row = []
        for j in range(i):
            row.append(str(current))
            current += 1
        pyr.append(" ".join(row))
    return pyr

for row in generate(5):
    print(row)

"""

Or

"""

import itertools
def floyd_triangle(n):
    nums = itertools.count(1)
    for i in range(1, n+1):
        print(' '.join(str(next(nums)) for _ in range(i)))

floyd_triangle(5)