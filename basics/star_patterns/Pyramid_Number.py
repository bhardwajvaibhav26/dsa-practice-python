'''


Number Pyramid Pattern
Problem Description:

You are given an integer n.
Your task is to return a pyramid pattern of numbers, 
where each row contains increasing numbers starting from 1 up to the row number, 
and the pyramid is centered with leading spaces.

'''

def generate (n):
    result = []
    for i in range (1,n+1):

        res =[]
        col = " " * (n-i)
        for j in range(1,i+1):  
            res.append(str(j))
        result.append(col + " ".join(res)+col)
    return result


for row in generate(5):
    print(row)
