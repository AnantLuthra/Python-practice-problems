# Write a program to print the given number is odd or even.

import math

# def check_ev(number):
#     return print("even") if number % 2 == 0 else print("odd")

# for i in [1,2,3,4,5]:
#     check_ev(int(input("Enter the value: ")))

# def squares(a, b):
#     # Write your code here
#     for i in range(a, b+1):
#         if math.sqrt(4):

# a = int(input("hehe: "))

# if str(math.sqrt(a)).split(".")[1] == '0':
#     print("it's a square root.")

# -----------------------------------------------------------------------
# grades = [10, 24, 64, 26, 87, 54]


# def gradingStudents(grades):
#     # Write your code here
#     final_grades = []
#     for i in grades:
#         multiple = 1
#         temp_i = i
#         while multiple != 0:
#             temp_i += 1
#             multiple = temp_i % 5
#         multiple = 1
#         if (temp_i - i) < 3 and temp_i >= 40:
#             final_grade = temp_i
#         else:
#             final_grade = i
#         final_grades.append(final_grade)
        

#     return final_grades

# print(gradingStudents(grades))


# ---------------------------------------------------------------

# word = "zaba"
# # h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]

# def designerPdfViewer(h, word):
#     # Write your code here
#     dict1 = {i:ord(i)-97 for i in "abcdefghijklmnopqrstuvwxyz"}
#     # values = [h[dict1[i]] for i in word]
#     values = []
#     for i in word:
#         value1 = dict1[i]
#         print(value1)
#         value1 = h[value1]
#         print(value1)
#         values.append(value1)
#     print(max(values) * len(word))
    
# designerPdfViewer(h, word)

# ----------------------------------------------------------------

# def findDigits(n):
#     # Write your code here
#     total = 0
#     for i in str(n):
#         if i != '0' and n % int(i) == 0:
#             total += 1
#     return total

# print(findDigits(1012))


# ----------------------------------------------------------------

# def chocolateFeast(n, c, m):
#     # Write your code here
#     bars = n // c
#     wrap_remain = bars
#     total_bars = 0
#     check = True
#     while bars != 0:
#         if check:
#             check = False
#             pass
#         else:
#             wrap_remain += bars
#         total_bars += bars
#         bars = 0
#         for i in range(1, wrap_remain+1):
#             if wrap_remain < m:
#                 break
#             wrap_remain -= m
#             bars += 1
    
#     return total_bars

# print(chocolateFeast(6, 2, 2))


# ----------------------------------------------------------------


