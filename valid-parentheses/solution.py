"""
ID: 52774a314c2333f0a7000688

Write a function that takes a string of parentheses,
 and determines if the order of the parentheses is valid.
  The function should return true if the string is valid, and false if it's invalid.
"""

par_set = set("()")

def valid_parentheses(string):

    open_parentheses = 0

    for parentheses in string:
        if open_parentheses < 0 or open_parentheses >= (len(string) // 2) + 1: return False

        if parentheses not in par_set: continue

        if parentheses == "(":
            open_parentheses += 1

        elif parentheses == ")":
            open_parentheses -= 1

    return open_parentheses == 0

print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses("(())"))
