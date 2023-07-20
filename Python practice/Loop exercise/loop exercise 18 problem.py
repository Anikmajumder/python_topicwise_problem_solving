#Exercise 1: Print First 10 natural numbers using while loop
'''
i = 1
while i<=10:
    print(i)
    i+=1
'''

# Exercise 2: Print the following pattern
'''
row = 5
for i in range(1,row+1, 1):
    for j in range(1, i+1):
        print(j, end="")
    print("")
'''

 
# Exercise 3: Calculate the sum of all numbers from 1 to a given number
"""
s = 0
input_num = input("Enter your number: ")
input_num = int(input_num)
for i in range(1, input_num+1,1):
    s+=i
print("Sum is: ", s)"""

# Exercise 4: Write a program to print multiplication table of a given number
"""
input_num = int(input("Enter your number: "))
for i in range(1,11,1):
    product = input_num*i
    print(product)"""

# Exercise 5: Display numbers from a list using loop
"""The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop"""

"""
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i>500:
        break
    elif i>150:
        continue
    elif i % 5 == 0:
        print(i)

"""
# Exercise 6: Count the total number of digits in a number
"""
num = 54321

count = 0
while num !=0:
    num = num // 10
    count= count+1
print("Total digit:", count)
 """   

# Exercise 7: Print the following pattern

"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
"""n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j, end="")
    print()
"""
# Exercise 8: Print list in reverse order using a loop

"""list = [12,13,14,15,18]

new_list = reversed(list)
for item in new_list:
    print(item)"""

#alternative solution

"""list1 = [1,2,3,4,5]
for i in range(len(list1)-1, -1,-1):
    print(list1[i])"""

# Exercise 9: Display numbers from -10 to -1 using for loop

"""for n in range(-10,0,1):
    print(n)"""

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop

"""for i in range(5):
    print(i)
else:
    print("Done!")"""

# Exercise 11: Write a program to display all prime numbers within a range

"""start = 25
end = 50

print("Prime numbers between {} and {} are: ".format(start,end))

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if(num%i)==0:
                break
        else:
            print(num)"""


# Exercise 12: Display Fibonacci series up to 10 terms
"""
num1 = 0
num2 = 1

for i in range(10):
    print(num1, end=" ")

    res = num1+num2

    num1 = num2
    num2 = res
"""

# Exercise 13: Find the factorial of a given number

"""num = int(input("Enter number: "))
f = 1

if num<0:
    print("It's no factorial number")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        f=f*i
    print("The factorial number is :" , f)"""

# Exercise 14: Reverse a given integer number

"""num = 23456
reverse_number = 0
print("Given Number: ", num)

while n>0:
    reminder = num % 10
    reverse_number = (reverse_number*10) + reminder
    num = num // 10
print("Reverse Number ", reverse_number)"""

# Exercise 15: Use a loop to display elements from a given list present at odd index positions
"""
list = [10,20,30,40,50,60]

for i in list[1::2]:
        print(i,end=" ")
 """       
# Exercise 16: Calculate the cube of all numbers from 1 to a given number
"""
num = int(input("Enter your number"))
for i in range(1,num+1):
    cube = i*i*i
    print("Current Number is : {}  and the cube is {}".format(i,cube))
"""
# Exercise 17: Find the sum of the series upto n terms
# ex: 2 + 22 + 222 + 2222 + 22222 = 24690

"""start = 2
n = 5
sum = 0

for i in range(0,n):
    print(start,end="+")
    sum += start
    start = start*10+2
print("sum of the series is:", sum )"""
# Exercise 18: Print the following pattern
row = 5
for i in range(0,row):
    for j in range(0, i+1):
        print("*",end=' ')
    print("\r")

for i in range(row, 0 ,-1):
    for j in range(0, i - 1):
        print("*", end= ' ')
    print("\r")