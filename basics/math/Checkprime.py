'''

Check for Prime Number
Problem Description:

You are given an integer n. 
Your task is to check whether the number is prime or not. 
A prime number is a number greater than 1 that has no divisors other than 1 and itself. 
Return True if the number is prime, and False otherwise.

'''

def is_prime(n):

    if n <= 1 :
        return False
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True

