# -----------------------------------------
# 📌 Strings
# -----------------------------------------


# Escape Character
# \" (double quotes) & \' (single quotes)
print("\"Hello Python\" I said")          # Output: "Hello Python" I said
print('\'Python is amazing\' I thought')  # Output: 'Python is amazing' I thought
# \n (new line) & \t (tab)
print("Hello\nPython")  # Output: Hello
                        #         Python
print("Hello\tPython")  # Output: Hello    World


# Zero Index
print("Hello"[0])    # Output: H
print("Hello"[1])    # Output: e
print("Hello"[2])    # Output: l
print("Hello"[3])    # Output: l
print("Hello"[4])    # Output: o

print("Hello"[-1])   # Output: o
print("Hello"[-2])   # Output: l
print("Hello"[-3])   # Output: l
print("Hello"[-4])   # Output: e
print("Hello"[-5])   # Output: H


# Slicing [:] (String range selection operator)
print("Hello"[1:4])  # Output: ell
print("Hello"[0:2])  # Output: He
print("Hello"[1:])   # Output: ello
print("Hello"[:3])   # Output: Hel
#print("Hello"[7])    # Output: Traceback (most recent call last):
                     #           File "<python-input-19>", line 1, in <module>
                     #             print("Hello"[7])
                     #                   ~~~~~~~^^^
                     #         IndexError: string index out of range


# List Slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(numbers[0:12:2])  # Output: [1, 3, 5, 7, 9, 11]
print(numbers[::1])     # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(numbers[::4])     # Output: [1, 5, 9, 13]
print(numbers[::-1])    # Output: [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numbers[::-3])    # OUtput: [13, 10, 7, 4, 1]
