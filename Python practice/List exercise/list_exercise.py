# Exercise 1: Reverse a list in Python

"""list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

# Alternative Solution:

list1 = [100, 200, 300, 400, 500]
list1 = list1[::-1]
print(list1)"""

# Exercise 2: Concatenate two lists index-wise

"""list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = [i + j for i, j in zip(list1, list2)]
print(new_list)
"""

# Exercise 3: Turn every item of a list into its square
"""
numbers = [1, 2, 3, 4, 5, 6, 7]
new_list=[]
for i in numbers:
    i=i*i
    new_list.append(i)
print(new_list)

"""
# Exercise 4: Concatenate two lists in the following order

"""list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = [i+j for i in list1 for j in list2]
print(result)
"""
# Exercise 5: Iterate both lists simultaneously
"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x,y in zip(list1,list2[::-1]):
    print(x,y)
  """  
# Exercise 6: Remove empty strings from the list of strings
"""
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

res = list(filter(None, list1))
print(res)
"""

# Exercise 7: Add new item to list after a specified item
"""
Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

"""

"""
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)
"""

# Exercise 8: Extend nested list by adding the sublist

"""
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]
Expected Output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']"""

"""
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)
"""
# Exercise 9: Replace list’s item with new value if found
"""
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)

list1[index] = 200
print(list1)
"""
# Exercise 10: Remove all occurrences of a specific item from a list.
"""
list1 = [5, 20, 15, 20, 25, 50, 20]
def remove_value(sample_list, value):
    return [ i for i in sample_list if i != value] 

res = remove_value(list1, 20)
print(res)

"""
#alternative solution:

list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)

print(list1)


