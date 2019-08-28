# Session 1: Basics Part A

## Warm up exercise: Rounding Numbers
Write a script that prompts the user for a floating point number and the number of decimal places to round the number, print the rounded number to the console. Python has a built-in [function](https://docs.python.org/3/library/functions.html#round) for doing this.

Sample input/output:
```
>>> Enter a floating point number: 2.0453687
>>> How many decimal places would you like: 3
>>> The rounded number is: 2.045
```

## Greetings
Write a script that prompts the user for their full name, then print a greeting to the console. A sample is shown below (Google "python string split" if you get stuck).

Sample input/output:
```
>>> What is your full name: Gandalf Greybeard
>>> Hello Greybeard, Gandalf
```

You should test your function before submitting it. However the marker bot can only assess your answer if it is written as a function as shown below. __Make sure you remove print statements when you submit!__

Submit your function to the MarkerBot as shown below. __Do not change the name of the function - greet.__

```py
def greet(name):
    # place your code here
    return greeting
```

You can test your function on your computer by calling the function as shown below.

```py
def greet(name):
    # place your code here
    return greeting

print(greet('Big Lebowski'))
print(greet('Captain Sparrow'))
```

## Journey to Work

How far do you have to travel to get to work? Write a function that, given how many kms travelled to work, return a suggestion based on the distance travelled:

- if the user travels greater than 5km to work, print 'You should take the train.'
- if the user travels greater than 2km to work, print 'You should cycle.'
- if the user travels 2km or less to work, print 'Why not enjoy the outdoors and walk?'

__Take a look at the cheat sheet for session 1 for clues on how to use conditional statements__

Here are some example inputs and their expected outputs:

|Input|Output|
|-----|------|
|6|'You should take the train.'|
|4|'You should cycle.'|
|2|'Why not enjoy the outdoors and walk?'|

Submit your answer to the marker bot using a function as shown below. __Do not change the name of the function - suggest_travel.__

An additional resource on conditional staements can be found here on [automate the boring stuff on youtube](https://www.youtube.com/watch?v=lWeCgEbk-Ro&feature=youtu.be)

```py
def suggest_travel(distance):
    # place your code here
    return suggestion
```

## FizzBuzz

Build a function that, given a positive integer *n*, returns a value based on the following:

- if n is divisible by 3, return 'Fizz'
- if n is divisible by 5, return 'Buzz'
- if n is divisible by 3 *and* 5, return 'FizzBuzz'
- if none of the above apply, just return n

To test your function, iterate over every number from 0 to 100 and print the value returned by your function to the screen.

Submit your answer to the marker bot using the function as shown below. __Do not change the name of the function.__

```py
def fizz_buzz(n):
    # place your code here
    return value
```

## Double Char

Ask the user to input a string. Return this string, with every character (char) repeated twice.

e.g. 'python' should become 'ppyytthhoonn'

__Make sure you remove print statements and the input function when you submit. Do not change the name of the function - double_char.__

```py
def double_char(word):
    # place your code here
    return word_with_repeated_chars
```

## Sum

Calculate the sum of:

- every number from 1 to n
- every **odd** number from 1 to n
- every number from 1 to n **divisible by 3**

Where *n* is a number supplied by the user.

Submit your answer to the marker bot using functions as shown below. __Do not change the name of the functions.__

```py
def sum_numbers(n):
    # place your code here
    return _sum_of_numbers
```

```py
def sum_odd_numbers(n):
    # place your code here
    return _sum_of_numbers
```

```py
def sum_div3_numbers(n):
    # place your code here
    return _sum_of_numbers
```
