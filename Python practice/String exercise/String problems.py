# Exercise 1A: Create a string made of the first, middle and last character

"""str1 = "james"

res = str1[0]
l = len(str1)
middle = int(l/2)
res = res + str1[middle]
res = res + str1[l-1]
print("new string: ", res)"""

# Exercise 1B: Create a string made of the middle three characters

"""def get_middle_three_chars(str1):
    print("Original string: ", str1)

    mi = int(len(str1)/2)
    res = str1[mi-1:mi+2]
    print("middle three chars are: ", res)


get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")"""

# Exercise 2: Append new string in the middle of a given string
"""
def append_middle(s1, s2):
    print("original string:", s1,s2)

    mi = int(len(s1)/2)
    x = s1[:mi:]
    x = x + s2
    x = x + s1[mi:]
    print("After appending new string in middle:", x)

append_middle("Ault", "Kelly")
"""
# Exercise 3: Create a new string made of the first, middle, and last characters of each input string

# Given:
# s1 = "America"
# s2 = "Japan"
# Expected Output:
# AJrpan
"""
def given_string(s1,s2):
    print("given string", s1,s2)

    mid1 = int(len(s1)/2)
    mid2 = int(len(s2)/2)
    res = s1[0]+s2[0]+s1[mid1]+s2[mid2]+s1[len(s1)-1]+s2[len(s2)-1]
    print(res)

given_string("America", "Japan")

"""
# Exercise 4: Arrange string characters such that lowercase letters should come first

"""def str1(s):
    lower = []
    upper = []
    for i in s:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)
    sorted_str = ''.join(lower + upper)
    print("Result:", sorted_str)

str1("PyNaTive")
"""
# Exercise 5: Count all letters, digits, and special symbols from a given string
"""
strl = "@#yn26at^&i5ve"

s = 0
d = 0
c = 0


for symbol in strl:
    if symbol.isalpha():
        c+=1
    elif symbol.isdigit():
        d+=1
    else:
        s+=1
print("Symbol: ", s)
print("Digit: ", d)
print("Char: ", c)
"""
# Exercise 6: Create a mixed String using the following rules
# Exercise 7: String characters balance Test
# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Exercise 9: Calculate the sum and average of the digits present in a string
# Exercise 10: Write a program to count occurrences of all characters within a string
# Exercise 11: Reverse a given string
# Exercise 12: Find the last position of a given substring
# Exercise 13: Split a string on hyphens
# Exercise 14: Remove empty strings from a list of strings
# Exercise 15: Remove special symbols / punctuation from a string
# Exercise 16: Removal all characters from a string except integers
# Exercise 17: Find words with both alphabets and numbers
# Exercise 18: Replace each special symbol with # in the following string