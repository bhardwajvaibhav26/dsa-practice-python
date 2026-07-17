'''
Inverted Right Angled Triangle
Problem Description:

You are given an integer n. 
Your task is to return an inverted right-angled triangle pattern of '*' 
where each side has n characters, represented as a list of strings. 
The first row should have n stars, the second row n-1 stars, and so on, until the last row has 1 star.
'''


def generate_square(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        result.append('*' * i)
    return result[::-1]

for row in generate_square(5):
    print(row)