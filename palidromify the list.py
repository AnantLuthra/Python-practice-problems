"""
Author: Anant
Date: 3/11/21
Purpose: Practice of python..
"""

elements = []
print("Enter the elements of list and for quitting enter q")
while True:  # Fist taking list elemets by user..
    try:
        element = input()
        if element == "q":  # Stopping taking input while entered q.
            break
        element = int(element)
        elements.append(element)
    except Exception as e:
        raise ValueError("Only integer's are allowed not other characters..")

list1 = []
for i in elements:
    if i > 10:
        i = str(i)  # checking if the given element is already a palindrome...
        if i == i[::-1]:
            i = int(i)
            i += 1 # If yes then it will add one, so that it can found 
        while True:
            # Converting into str to reverse it for checking its a palindrome or not..
            i = str(i)
            b = i[::-1]
            if i == b:
                list1.append(b)
                break
            i = int(i)
            i += 1  # To check next element if the present number is not a palindome
    else:
        list1.append(i)

print(list1)
