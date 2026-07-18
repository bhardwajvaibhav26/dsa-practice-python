'''


Check for Even Number
Problem Description:

You are given an integer n. 
Your task is to check whether the number is even or not. 
Return True if the number is even, and False otherwise.

'''

def is_even(n):

    # return n % 2 == 0

    return n & 1 == 0 