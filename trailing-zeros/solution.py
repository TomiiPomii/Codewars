"""
ID: 52f787eb172a8b4ae1000a34

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html 
"""

def zeros(n):
    quotient = round(n / 5)

    if  quotient <= 5:
        return quotient
    else:
        return quotient + zeros(quotient)

print(zeros(0))
print(zeros(6))
print(zeros(30))