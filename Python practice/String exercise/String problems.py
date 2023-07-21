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

# Given:
# s1 = "Abc"
# s2 = "Xyz"
# Expected Output:
# AzbycX

"""s1 = "Abc"
s2 = "Xyz"

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string 
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)"""


# Exercise 7: String characters balance Test

"""
def string_check(s1,s2):
    flag = True

    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag

s1 = "Yn"
s2 = "PYnative"
flag = string_check(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_check(s1, s2)
print("s1 and s2 are balanced:", flag)
"""
# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
"""
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

temp_str = str1.lower()
count = temp_str.count(sub_string.lower())
print("the usa count is:", count)
"""

# Exercise 9: Calculate the sum and average of the digits present in a string
"""
str1 = "PYnative29@#8496"

list1 = []
count = 0

for char in str1:
    if char.isdigit():
        list1.append(int(char))
        count+=1

avg = sum(list1)/count
print("Sum is:", sum(list1), "Average is ", avg)
"""
#Alternative solution:
"""
input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)
"""

# Exercise 10: Write a program to count occurrences of all characters within a string

"""str1 = "Apple"

char_dict = dict()

for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print("Result:", char_dict)
"""
# Exercise 11: Reverse a given string . For many type of method "https://www.scaler.com/topics/reverse-a-number-in-python/"

"""str2 = "Apple"
print(''.join(reversed(str2)))"""

#Alternative method:

"""str1 = "Pynative"
print(str1[::-1])"""

# Exercise 12: Find the last position of a given substring

"""str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)
index = str1.rfind("Emma")
print("Last occurance of Emma starts at index:", index)
"""

# Exercise 13: Split a string on hyphens

"""str1 = "Emma-is-a-data-scientist"
sub_string = str1.split("-")
for sub in sub_string:
    print(sub)"""

# Exercise 14: Remove empty strings from a list of strings

"""str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    if s:
        res_list.append(s)
print(res_list)"""


#Alternative solution:
"""str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

sub_string = list(filter(None, str_list))
print(sub_string)"""

# Exercise 15: Remove special symbols / punctuation from a string

"""import string
str1 = "/*Jon is @developer & musician"

new_str = str1.translate(str.maketrans('', '', string.punctuation))
print(new_str)"""

#Alternative Method:

"""import re

str1 = "/*Jon is @develper & musician"

res = re.sub(r'[^\w\s]','',str1)
print(res)"""

# Exercise 16: Removal all characters from a string except integers
"""
str1 = 'I am 25 years and 10 months old'

res = ''.join([item for item in str1 if item.isdigit()])
print(res)

"""
# Exercise 17: Find words with both alphabets and numbers
"""
str1 = "Emma25 is Data scientist50 and AI Expert"

res = []
temp = str1.split()

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)
    
for i in res:
    print(i)
"""
# Exercise 18: Replace each special symbol with # in the following string

import string

str1 = '/*Jon is @developer & musician!!'

replace_char = "#"

for char in string.punctuation:
    str1 = str1.replace(char, replace_char)
print(str1)

