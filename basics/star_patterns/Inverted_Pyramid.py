'''
Inverted Pyramid Pattern

Problem Description

You are given an integer n. Your task is to return an inverted pyramid pattern of '*', 
where each side has n rows, represented as a list of strings. 
The first row has 2n - 1 stars, 
the second row has 2n - 3 stars, and so on, 
until the last row has 1 star, with each row centered using spaces.
'''

def func(n: int) -> list[str]:
    rows = []
    for i in range(1, n + 1):
        b = " " * (i - 1) + "*" * (2 * (n-i+1) - 1)
        rows.append(b)
    return rows

for row in func(5):
    print(row)