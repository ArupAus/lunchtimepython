# Session 1: Basics Part A

## Rounding numbers
Write a script that prompts the user for a floating point number and the number of decimal places to round the number, print the rounded number to the console. Python has a built-in [function](https://docs.python.org/3/library/functions.html#round) for doing this.

Sample input/output:
```
>>> Enter a floating point number: 2.0453687
>>> How many decimal places would you like: 3
>>> The rounded number is: 2.045
```

## Greetings
Write a script that prompts the user for their full name, then print a message to the console. A sample is shown below (Google "python string split" if you get stuck).
Sample input/output:
```
>>> What is your full name: Alex Smith
>>> Hello Smith, Alex
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

## FizzBuzz

Iterate over each number from 1 to 100. For each number (n) in the range, do the following:
- if n is divisible by 3, print 'Fizz' to the console
- if n is divisible by 5, print 'Buzz' to the console
- if n is divisible by 3 *and* 5, print 'FizzBuzz' to the console
- if none of the above apply, just print n to the console

## Double char

Ask the user to input a string. Return this string, with every character (char) repeated twice.

e.g. 'python' should become 'ppyytthhoonn'

Teacher's pet edition: Ask the user for an number (n) as well. Repeat each char in the given string n times.

## Sum

Calculate the sum of:

- every number from 1 to 100
- every **odd** number from 1 to 100
- every number from 1 to 100 **divisible by 3**
