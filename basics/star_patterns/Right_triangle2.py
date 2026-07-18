'''

Right Angled Triangle II
Problem Description:


You are given an integer n. 
Your task is to return a right-angled triangle pattern of '*', 
where each row contains stars aligned to the right. 
The first row has one star, the second row has two stars, and so on, until the nth row has n stars.
'''

def Generate(n):
    result = []
    for i in range(1,n+1):
        row = " "* (n-i) + "*" * i
        result.append(row)
    return result
 
for row in Generate(5):
    print(row)
