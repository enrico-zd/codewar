"""
Your task is to make a function that can take any non-negative integer as an argument and return it with 
its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

"""

# # cara sendiri
# def descending_order(num):
#     angka = [int(x) for x in str(num)]
#     data = len(angka)-1
#     for i in range(data):
#         for j in range(data):
#             if angka[j] < angka[j+1]:
#                 angka[j], angka[j+1] = angka[j+1], angka[j]

#     s = [str(y) for y in angka]
#     hasil = int(''.join(s))
#     return hasil

# print(descending_order(123456789))

# # cara solusi
# def Descending_Order(num):
#     return int("".join(sorted(str(num), reverse=True)))