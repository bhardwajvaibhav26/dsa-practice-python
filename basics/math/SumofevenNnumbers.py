'''
Sum of N Even Natural Numbers
Problem Description:

You are given an integer n. 
Your task is to calculate and return the sum of the first n even natural numbers. 
The even natural numbers are: 2, 4, 6, 8, ...

'''

def sumeven(n):
    # return n * (n+1)

    return sum(x for x in range(1,2*n+1) if x %2 ==0)

print(sumeven(5))