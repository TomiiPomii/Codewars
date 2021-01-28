"""
ID: 54bf85e3d5b56c7a05000cf954bf85e3d5b56c7a05000cf9

Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.
"""

def number(lines):
    for i, line in enumerate(lines):
        lines[i] = str(i+1) + ": " + line
    return lines

print(number([]))