# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

"""list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("List one's odd index position:")
print(odd_elements)

even_elements = list2[0::2]
print("List one's even index position:")
print(even_elements)

print("Printing Final list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)
"""
# Exercise 2: Remove and add item in a list
"""
sample_list = [34, 54, 67, 89, 11, 43, 94]

element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List After adding element at index 2 ", sample_list)

sample_list.append(element)
print("List After adding element at last ", sample_list)

"""
# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
"""
sample_list = [11,45,8,23,14,12,78,45,89]

length = len(sample_list)
chunk_size = int(length/3)
start = 0
end = chunk_size

for i in range(3):
    indexes = slice(start, end)

    list_chunk = sample_list[indexes]
    print("Chunk", i, list_chunk)

    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end+= chunk_size
"""


# Exercise 4: Count the occurrence of each element from a list
"""
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item]+=1
    else:
        count_dict[item]=1

print(count_dict)

"""
# Exercise 5: Create a Python set such that it shows the element from both lists in a pair

"""
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)

"""

# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
"""
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection = first_set.intersection(second_set)
print("Intersection is: ", intersection)

for item in intersection:
    first_set.remove(item)

print("After removieng common element", first_set)
"""


# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
"""
first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of First set - ", second_set.issubset(first_set))

print("First set is supter set of second set - ", first_set.issuperset(second_set))
print("Second set is Super set of First set - ", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)
"""
# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
"""
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

roll_number[:] = [item for item in roll_number if item in sample_dict.values()]

print("after removing unwanted elements from list:", roll_number)
"""

# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates

"""speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}
print("Dictionary values: ", speed.values())

speed_list = list()

for val in speed.values():
    if val not in speed_list:
        speed_list.append(val)
print("unique list", speed_list)
"""

# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

sample_list = list(set(sample_list))

t = tuple(sample_list)
print("tuple ", t)

print("Minimum number is: ",min(t))
print("Maximum number is: ",max(t))
