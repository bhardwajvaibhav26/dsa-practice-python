'''

Hollow Square of side 'N'


Problem Description:

You are given an integer n. 
Your task is to return a hollow square pattern of size n x n made up of the character '*', 
represented as a list of strings. 
The hollow square has '*' on the border, 
and spaces ' ' in the middle (except for side lengths of 1 and 2).

'''

def generate_pattern(n : int) -> list[str] :

    if n == 1 :
        return ['*']
    if n == 2 :
        return ['**','**']
        
    top_bottom = "*" * n
    middle = "*" + " " *(n-2)+ '*'
    
    result = [top_bottom]
    for i in range(n-2):
        result.append(middle)
    result.append(top_bottom)
    
    return result

for row in generate_pattern(8):
    print(row)

