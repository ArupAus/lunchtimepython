# Cheat Sheet

Here are some commands for your reference that you will encounter throughout the sessions.

## Session 0: Getting Started

__Assigning variables__

Remember starting variable names with numbers is not allowed

```py
2var = 0 # invalid variable name
var2 = 0 # valid variable name
```

```py
var_name = 0           # integer
var_name = 'a string'  # string
var_name = 2.3         # float

```
__Converting Types__

Remember to switch between types to perform operations

```py
str(3) # '3'
int('2') # 2
float('3.2') # 3.2
```

__Order of Operation__
```py
(3+2)*5 # 25
# remember BOMDAS?
# Brackets Over Multiplication, Division, Addition and Subtraction
```
__Rounding Numbers__
```py
round(3.4564,2) # will round the number to 2 decimal places
```
## Session 1: Basics Part A

__Bools and Comparison operators__

```py
# comparison operators
== # equal to
!= # not equal to
< # less than
> # greater than
<= # less than or equal to
>= # greater than or equal to
# expressions that evaluate to a boolean value
42 <= 42 # True
'42' == 42 # False
my_age = 27 # assign 27 to my_age
my_age == 27 # True
# boolean operators
True and False # False
True or False # True
myAge > 25 or myAge < 20 # True
myAge > 25 and myAge < 20 # False
not True # False
not False # True
```
__For loops__
```py
for i in range(10): # loops over the set -> 0,1,2,...,9
	print(i)

```

__While loops__

```py
i = 0 
while i < 10:
	print(i)
	i = i+1  # alternatively short hand is i += 1

```

__If Statements__
```py
# if statement
condition = True # condition is an expression that evaluates to True or False
if (condition):
	# execute the body of code. Indentation is important!

# if else statement
if (condition):
	# execute this body of code
else:
	# execute this body of code

# if elif else statement
if (condition1):
	# execute this body of code
elif (condition2):
	# execute this body of code
elif (condition3):
	# execute this body of code
else:
	# execute this body of code

# you can have as many elif's as you like
```

## Session 2: Basics Part B

__Defining a function__

```py
def add(a, b):
	return a+b
```

__Calling a function__

```py
c = add(4, 5)
# c = 9
```

## Session 3: Data Structures

__Lists__
```py
# python list - a variable to store stuff
names = ["Jess","Tom","Laura","Will"]

# list splicing
names[0] # "Jess"
names[1] # "Tom"
names[-2] # "Laura"
# names[start:stop:step] grabs multiple elements from list (includes start, excludes stop)
names[1:3:1] # ["Tom", "Laura"]

# how long is the list
len(names) # 4
# adding to list
names.append("Jason") # add "Jason" to end
names.insert(2, "John") # insert "John" at index 2
names.extend(["Alex","Faye","Mia"]) # append "Alex", "Faye" and "Mia" to the list
# remove from the list
names.pop() # removes "Mia" and returns
names.remove("Tom") # removes first "Tom" found

# some useful things you can do with lists
"Sam" in names # False
"Sam" not in names # True

# loop through each element in an array
for name in names:
	print(name)
```

__Dictionaries__
```py
person = {"name":"Alex", "age":27, "height":158, 42:"The ultimate question"}

person["name"] # "Alex"
person["age"] # 27

len(person) # 4
person["graduate"] = True # adds another key-value pair to the dictionary
person.pop(42) # returns "The ultimate Question" and deletes the key-value pair from the dictionary

# looping through dictionary
person.values() # ["Alex", 27, 158, True]
person.keys() # ["name", "age", "height", "graduate"]
person.items() # [("name", "Alex"), ("age", 27), ("height", 158), ("graduate", True)]

for k, v in person.items():
	print("Key: "+ str(k)+ "\tValue: "+ str(v)
```

## Session 4: Reading/Writing Files

Navigation of directories in python can be done using the following commands

```py
import os

# working director
os.getcwd() # will return a path to your current working directory

# check if file exists
os.path.exists(... your path)

#Joining Paths
path = '.\\Desktop\\'
file = 'example.txt'
full_path = os.path.join(path, file)

#changing directory
os.chdir()

```

__Splitting a string__
```py
split_string = 'hello i am a string'.split() # returns a list split by whitespace
split_string # ['hello', 'i', 'am', 'a', 'string']

csv_string = '1,2,456,789,1566'.split(',') # returns a list split by ,
csv_string # ['1','2','456','789','1566'] note that these are still strings not ints

# you can use map and list to convert the list
csv_ints = list(map(int,'1,2,3,4,5'.split(','))) # [1,2,456,789,1566]
```
__Opening a file__
```py
f = open('file.txt', 'r')    # read mode
f = open('file.txt', 'w')    # write mode
f = open('file.txt', 'a')    # append mode
```
__Reading a file__
```py
f = open('file.txt', 'r')    # read mode
lines  = f.readlines()       # returns a list of strings representing your lines in your file
for line in lines:           # iterate over each line in your list of lines
  print(line)                # print out each line to the shell
f.close()
```

__Writing a file__
```py
f = open('file.txt', 'w')    # read mode
f.write("To write or not to write\nthat is the question!\n")
f.close()
```
