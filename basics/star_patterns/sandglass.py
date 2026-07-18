'''
Sandglass Pattern
Problem Description:

You are given an integer n. Your task is to return a sandglass pattern of '*',
 where the first row contains 2n - 1 stars and each subsequent row decreases the number of stars by 2, 
 until the last row contains a single star. 
 After reaching the smallest width, the pattern then continues with 
 the same number of stars increasing back to 2n - 1. 
 The stars in each row should be centered.
'''

def generate(n):
    result=[]
    for i in range(1,n+1):
        up = " " * (i-1)+ "8" * (2*(n-i+1)-1)
        result.append(up)

    for j in range(2,n+1):
        bot = " " * (n-j)+ "8" * (2*j-1)
        result.append(bot)

    return result


for row in generate(5):
    print(row)

'''
or
'''

def generate_sandglass(n):
    result = []
    
    # Top half (inverted pyramid)
    for i in range(n, 0, -1):
        spaces = " " * (n - i)
        stars = "8" * (2 * i - 1)
        result.append(spaces + stars+ spaces)
    
    # Bottom half (regular pyramid, skip first row to avoid duplicate middle)
    for i in range(2, n + 1):
        spaces = " " * (n - i)
        stars = "8" * (2 * i - 1)
        result.append(spaces + stars + spaces)
    
    return result

for row in generate_sandglass(5):
    print(row)