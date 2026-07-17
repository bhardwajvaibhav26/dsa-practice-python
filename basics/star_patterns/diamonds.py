'''

Diamond Pattern
Problem Description:

You are given an integer n. Your task is to return a diamond pattern of '*' 
with n rows for the upper part (the widest row will have 2n - 1 stars), 
and the lower part is the mirrored version of the upper part. 
Each row should be centered with appropriate spaces.

'''

def diamond(n):

    diamond = []

    for i in range(1, n + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        diamond.append(spaces + stars + spaces)

    for i in range(n - 1, 0, -1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        diamond.append(spaces + stars + spaces)

    return diamond

for row in diamond(5):
    print(row)