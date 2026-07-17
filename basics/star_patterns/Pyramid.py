'''
Pyramid Pattern

Problem Description:

You are given an integer n. 
Your task is to return a pyramid pattern of '*' where each side has n rows, 
represented as a list of strings. 
The pyramid is centered, with 1 star in the first row, 
3 stars in the second row, and so on, 
increasing by 2 stars per row until the base row has 2n - 1 stars.
'''


def func(n: int) -> list[str]:
    rows = []
    for i in range(1, n + 1):
        b = " " * (n - i) + "*" * (2 * i - 1)
        rows.append(b)
    return rows

for row in func(5):
    print(row)
