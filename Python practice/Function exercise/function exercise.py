# Exercise 1: Create a function in Python

"""def demo(name, age):
    print(name,age)
demo("Ben",12)"""
# Exercise 2: Create a function with variable length of arguments

"""def func1(*args):
    for i in args:
        print(i)
func1(20, 40, 60)
func1(80, 100)"""

# Exercise 3: Return multiple values from a function
"""def calculate(num1, num2):
    
    add= num1+num2
    sub = num1-num2
    
    return add, sub

result = calculate(10,20)
print(result)"""

# alternative
"""def calculation(a, b):
    return a + b, a - b

add, sub = calculation(40, 10)
print(add, sub)"""


# Exercise 4: Create a function with a default argument

"""def show_employee(name, salary= 9000):
    print("Name: ", name, "Salary: ", salary)

show_employee("Ben", 12000)
show_employee("Jasia")
"""
# Exercise 5: Create an inner function to calculate the addition in the following way

"""def func(a,b):
    def inner_func(a,b):
        return a+b

    sum = inner_func(a,b)   
    return sum + 5

res = func(10,20)
print(res) 
"""

# Exercise 6: Create a recursive function
#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
"""def addtion(num):
    if num:
        return num + addtion(num - 1)
    else:
        return 0
res  = addtion(10)
print(res)"""

# Exercise 7: Assign a different name to function and call it through the new name

"""def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

show_student= display_student
show_student("Emma", 26)
"""
# Exercise 8: Generate a Python list of all the even numbers between 4 to 30

#print(list(range(4,30,2)))

# Exercise 9: Find the largest item from a given list
"""x = [4, 6, 8, 24, 12, 2]

print(max(x))"""