'''

Valid Perfect Square
Problem Description:

You are given a positive integer num. 
Your task is to check whether num is a perfect square or not. 
A perfect square is an integer that is the square of an integer (e.g., 1, 4, 9, 16, ...). 
Return True if num is a perfect square, and False otherwise.

'''

def is_square(num):

    return num >= 0 and (num ** 0.5 ) % 1 == 0


