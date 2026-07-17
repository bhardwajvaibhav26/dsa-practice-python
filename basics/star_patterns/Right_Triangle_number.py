'''
Right Angled Triangle with Numbers
Problem Description:

You are given an integer n. 
Your task is to return a right-angled triangle pattern where each row contains repeated digits. 
The first row contains the number 1 repeated once, 
the second row contains the number 2 repeated twice, 
and so on until the nth row contains the number n repeated n times.

'''
def func(n):
    for i in range (1,n+1):
        print(f'{i}'*i)

func(5)

def gen(n):
    pyra = []
    for i in range(1,n+1):
        num = i * str(i)
        pyra.append(num)
    return pyra