"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

"""

# cara sendiri
def coba(a):
    while True:
        x = 0
        y = 0
        for char in a:
            if char > 0:
                x += 1
            elif char < 0:
                y += char
        if a == []:
            return a
        else:
            return [x,y]
        
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(coba(a))


