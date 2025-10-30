# 1. HELLO WORLD
# display text/ data: "print()";
# print("Hello World!")
# print('')
# print("My first python program")

# 2. Comment - to explain your code, ignore by python generators
# Other way to comment
"""
Name
"""

# 3. Variables
# Create method
# name = 12
# print(name)

# 4. String - sentence
# name ="chahra"
# print(name)
# Variables can only named by letters first, no numbers accepted
# Name = "hassan"
# name = "hassan"
# Python is case sensitive

# Multiple assignments (multi. variables)
# y, z, x = 1, 2, 3
# print(y, z, x)

# Assign same value to multiple variables

# a = b = c = 20
# print (a, b, c)

# Var can be updated or reassigned
# num = 12
# print(num)
# num = 13
# print(num)
# num = num + 1
# print(num)

# ====== Exercise ====== 
# 5. Data types
# 5-1 numeric types
# num = 12
#num2 = 1.34 #float
#num3 = 3 +4j #complex num
#print (num, num2, num3)
#print(type(num)) #extract type
#print(type(num2), type(num3))

# 5-2 boolean type
#sunny = True
#raining = False
#print(sunny, raining)

# 6 Sequence types - hold multiple values in sequential order
# Lists
#numbers = [2,3,4,5]
#print(numbers)
# access list items by index (0-based)
#print(numbers[3])
# change the 3
#numbers [1] =6
#print(numbers)
#numbers [3] = "hello"
#print(numbers)

# Add items
#numbers.append(100) #add item
#print(numbers)
#numbers.insert(1,200)
#print(numbers)

#remove items
#numbers.remove(2)
#print(numbers) 

# List slicing (extract a portion)
#print (numbers[:4])
#print (numbers[2:5])
#print(numbers[2:])

# Sorting and reversing
#numbers2 = [2,1,5,43,2]
#numbers2.sort()
#print(numbers2)

# List length and membership
#print(len(numbers2))

# Identify belongs to list or not
#print(23 in numbers2)

# Create Tuples on python 
#names = ("apple", "orange", "banana")
#print(names)

# Tuples cannot be modified
# names[2] = "blueberry" #error
# You can combine Tuples
#names2 = ["orange", "watermelon"]
#print(names+names2) #problem

# Mapping type

#dictionary
#person ={"name":"chahra","age":15}
#print(person)

# Accessing values by key
#print(person["name"], person["age"])

# Add new key-value pairs
#person["city"]="london"
#print(person)

# Nested dictionaries (dictionary inside a dictionary)
#students = { "s01":{"name":"chahra", "age":20}, 
#       "s02":{"name":"anis", "age":21}}     
#print(students)

# Set type

#numbers = {1,2,3,3}
#print(numbers)

# Add and remove elements
#numbers.add(4)
#print(numbers)
#numbers.discard(4)
#print(numbers)

# Set automatically remove duplicates

# Set operations (like in math)

#nums = {1,22,3,3}
#nums2 = {3,2,1,44}
#names = {"chahra","abd","Abd"}
#print (names)
#print (nums | nums2)
#print (nums & nums2)
#print(nums-nums2)

# Membership check on sets
#print(2 in nums)
#print(22 in nums)

# Convert list to set to remove duplicates
#numbers_list =[1,2,3,3] #have duplicates
#unique = set(numbers_list)
#print(unique)

# Casting: converting between types
#print(float(3))
#print(int(3.4))

# Input
#print(input("Please enter a value: ")) #problem
#input always return a string, can convert it using int(), float() etc

#num = int(input("enter a value: ")) #problem
#print(type(num))#problem

# OUTPUT
#name = "chahra"
#city = "london"
#print(f"my name is {name} i am from {city}")

#print("my name is: ", name)

#print(name+city)
#print(name+2) #doesn't work w/ string + integers

#print("my name is: " , end = "\n")
#print("my name is: " , end = "\t")
#print("my name is: " , end = "\\")

# 'sep' changes the separator between items

# OPERATORS
# 1. arithmetic operators
#num =1
#num2 =3
#print(num+num2)
#print(num*num2)
#print(num-num2)
#print(num/num2)

# 2. assignment operators

#num = 12
#num += 1
#print(num)
#num -=1
#num *=2
#print(num)

# 3. comparison operators - outcome: true/false

#print(3<5)
#print(3>5)
#print(3>=5)
#print(3==5)
#print(3!=5)

# 4. Logical oeprators
print(3 and 5)
print(3 or 5)

# 5. membership operators

# STRINGS - next week
