"""
Square of side 'N'

Problem Description: You are given an integer n. 
Your task is to return a square pattern of size n x n made up of the character '*', 
represented as a list of strings.

"""

def generate_square(n: int) -> list[str]:
    for i in range (n):
        print("*" * n)
generate_square(7)
''' or '''

def generate_square(n: int) -> list[str]:
    return ['*' * n for i in range(n)]