"""
ID: 54e6533c92449cc251001667
Problem: 

Implement the function unique_in_order which takes as argument a sequence and returns a list of items
without any elements with the same value next to each other and preserving the original order of elements.

"""
def unique_in_order(arr):
    output = [arr[0]] 
    for i in arr:
        if i != output[-1]:
            output.append(i)
    return output

print(unique_in_order('AAAABBBCCDAABBB') == ['A','B','C','D','A','B'])
