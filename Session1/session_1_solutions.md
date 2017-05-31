# Session 1: Basics Part A

## Rounding numbers
Write a script that prompts the user for a floating point number and the number of decimal places to round the number, print the rounded number to the console. Python has a tool for doing this: `round()`.

Sample input/output:
```
> Enter a floating point number: 2.0453687
> How many decimal places would you like: 3
> The rounded number is: 2.045
```
*ANS:*
```py
numberToRound = float(input("Enter a floating point number: "))
numberOfDecimalPlaces = int(input("How many decimal places would you like: "))
print("The rounded number is: " + str(round(numberToRound, numberOfDecimalPlaces)))
```

## Greetings
Write a script that prompts the user for their full name, then print a message to the console. A sample is shown below (Google "python string split" if you get stuck).
Sample input/output:
```
> What is your full name: Alex Smith
> Hello Smith, Alex
```

*ANS:*
```py
fullName = input("What is your full name: ")

# use the string split method to split the string by the space
# this will only work if the user separates their first and last name with a space

firstName, lastName = fullName.split(' ')
print("Hello " + lastName + ', ' + firstName)
```

## Journey to work

How far do you have to travel to get to work? Ask the user how many kms they travel to work, then give them a suggestion based on their repsonse:
- if the user travels greater than 5km to work, print 'You should take the train.'
- if the user travels greater than 2km to work, print 'You should cycle.'
- if the user travels 2km or less to work, print 'Stop being lazy and walk!'

Here are some example inputs and their expected outputs:

|Input|Output|
|-----|------|
|6|'You should take the train.'|
|4|'You should cycle'|
|2|'Stop being lazy and walk!'|

*ANS:*
```py
distance = float(input("How far do you travel to work? "))

if distance > 5:
	print("You should take the train.")
elif distance > 2:
	print("You should cycle.")
else:
	print("Stop being lazy and walk!")
```

## FizzBuzz

Iterate over each number from 1 to 100. For each number (n) in the range, do the following:
- if n is divisible by 3, print 'Fizz' to the console
- if n is divisible by 5, print 'Buzz' to the console
- if n is divisible by 3 *and* 5, print 'FizzBuzz' to the console
- if none of the above apply, just print n to the console

*ANS:*
```py
for n in range(1, 100):
	if n%3==0 and n%5==0:
		print("FizzBuzz")
	elif n%3==0:
		print("Fizz")
	elif n%5==0:
		print("Buzz")
	else:
		print(n)
```

## Double char

Ask the user to input a string. Return this string, with every character (char) repeated twice.

e.g. "python" should become "ppyytthhoonn"

Teacher's pet edition: Ask the user for an number (n) as well. Repeat each char in the given string n times.

*ANS:*
For the examples in class we used the **range()** method with **for** loops. But the **for** loop can iterate over any collection of things. In the case of **range()**, the for loop is iterating over a collection of integers (ints) that the **range()** method builds for us.

For example:
range(6) = [0,1,2,3,4,5]

So when we use **for n in range(6)**, we are actually looping though each integer in the collection **[0,1,2,3,4,5]**.

We can also think of a string as a collection of characters:
"A Ham" = ["A", " ", "H", "a", "m"]

So we can use a **for** loop to iterate over a collection of characters in a string.

```py
word = input("Enter a word you would like me to double: ")
doubleWord = "" # initialise doubleWord as an empty string
for character in word:
	doubleWord = doubleWord + character*2
print(doubleWord)
```

## Sum

Calculate the sum of:

- every number from 1 to 100
```py
sum=0
for n in range(1,100):
	sum = sum + n
print("This sum from 1 to 100 is: "+str(sum))
```
- every **odd** number from 1 to 100
```py
sum=0
for n in range(1,100):
	if n%2!=0:
		sum = sum + n
print("This sum of every odd number from 1 to 100 is: "+str(sum))
```
- every number from 1 to 100 **divisible by 3**
```py
sum=0
for n in range(1,100):
	if n%3==0:
		sum = sum + n
print("This sum of every number divisible by 3 from 1 to 100 is: "+str(sum))
```
