# Session 1 Problems


## A little theory

- What is the difference between the equal to operator `==` and the assignment operator `=`?
- What is an infinite loop?
- What is the difference between break and continue?
- Which Python utility can you use to run a loop a certain amount of times?

*ANS:*

*What is the difference between the equal to operator `==` and the assignment operator `=`?* The equal to operator compares whether one value is equal to another and evaluates to a bool ('True' or 'False'), where the assignment operator takes the expression on the right and assigns it to the variable on the left.
'a == 4' returns 'True' or 'False' depending on the value of 'a'
'a = 4' assigns '4' to the variable 'a'

*What is an infinite loop?* The computer is stuck in a 'while' or a 'for' that never ends.

*What is the difference between break and continue?* 'break' will break out of a loop completely, where 'continue' will skip whatever remains in the loop body and begins the next iteration.

*Which Python utility can you use to run a loop a certain amount of times?* The 'for' loop is perfect for this.

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
