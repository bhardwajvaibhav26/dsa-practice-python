
'''

Right Angled Triangle

Problem Description:

You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side has n characters, 
represented as a list of strings. The triangle has '*' characters, 
starting with 1 star in the first row, 2 stars in the second row, 
and so on until the last row has n stars.

'''

def generate_square(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        result.append('*' * i)
    return result

for row in generate_square(5):
    print(row)