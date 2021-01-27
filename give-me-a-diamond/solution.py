"""
ID: 5503013e34137eeeaa001648

You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters.
Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
"""


def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None 
    if n == 1:
        return "*\n"
    
    spaces = n // 2
    first_half = " "*spaces + "*\n"
    for i in range(1,spaces):
        first_half += " "*(spaces-i) + "*"*(3+(i-1)*2) + "\n"
    
    solution = first_half + "*"*n + "\n"
    second_half = ""
    for i in range(spaces-1, 0, -1):
        second_half += " "*(spaces-i) + "*"*(3+(i-1)*2) + "\n"

    solution += second_half + " "*spaces + "*\n"   

    return solution

print(diamond(13))