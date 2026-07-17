'''
Rectangle Pattern

Problem Description:

You are given two integers, n and m. 
Your task is to return a rectangle pattern of '*', 
where n represents the number of rows (length) and m represents the number of columns (breadth).

'''

def generate_pattern(n : int,m :int) -> list[str] :
    result = []
    for i in range(n):
        result.append('*' * m)
    return result

for row in generate_pattern(4,7):
    print(row)