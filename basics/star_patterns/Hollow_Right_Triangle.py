'''
Hollow Right Triangle

Problem Description:

You are given an integer n. Your task is to return a hollow right-angled triangle pattern of '*', 
where the first and last rows contain stars, while the inner rows contain a star at the beginning and end, with spaces in between. 
The triangle should be right-aligned.
'''

def generate(n):
    result = []
    for i in range(1, n + 1):
        if i == 1:
            result.append("*")
        elif i == n:
            result.append("*" * n)
        else:
            result.append("*" + " " * (i - 2) + "*")
    return result


for row in generate(7):
    print(row)