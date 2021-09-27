"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

"""

# # cara sendiri
# def coba(a):
#     while True:
#         x = 0
#         y = 0
#         for char in a:
#             if char > 0:
#                 x += 1
#             elif char < 0:
#                 y += char
#         if a == []:
#             return a
#         else:
#             return [x,y]
        
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# print(coba(a))



# # cara solusi 1
# def count_positives_sum_negatives(arr):
#     pos = sum(1 for x in arr if x > 0)
#     neg = sum(x for x in arr if x < 0)
#     return [pos, neg] if len(arr) else []



# # cara solusi 2
# def count_positives_sum_negatives(arr):
#     return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []



# # cara solusi 3
# def count_positives_sum_negatives(arr):
#     return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []

