# Session 2: Basics Part B

## A little theory

These are thought questions - there are probably several right answers.

- How can using a function make your code shorter?
- How can using a function make your code easier to change?
- How can using a function make your code more readable?

## How Long is a String

Create a function called `longer_string` that takes two strings and returns the longer one. For example,

```py
longer_string("Ove", "Arup") # returns "Arup"
```

If they are the same length return the first string.

Submit your function to the MarkerBot as shown below.

```py
def longer_string(string1, string2):
    # you can use whatever variable names want for the arguments and return variable
    # place your code here
    return longer_string
```

## Printing Triangles

Create a function called `build_triangle` that takes a single integer and returns a sideways *triangle* of that height, made of *'s. For example:

```
>>> build_triangle(5)
*
**
***
****
*****
```

The function should return a single string. A string can be separated over multiple lines when printed by adding `\n` to the string. For example:

```
>>> greeting = "Hello,\nWorld!"
>>> print(greeting)
Hello,
World!
```

*HINT:* Python's ability to 'multiply' a string by an integer may prove useful.

Submit your function to the MarkerBot as shown below.

```py
def build_triangle(n):
    # place your code here
    return triangle
```

Say you wanted to build a three storey triangle, you function would return the string `"*\n**\n***"`. Which, when printed, looks like:

```
*
**
***
```

**Bonus points:** make a pyramid instead.

## Multiples of 3 and 5

If we list all the natural numbers (integers) below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Build a function that returns the sum of all the multiples of 3 or 5 below a given number.

Submit your function to the MarkerBot as shown below.

```py
def sum_multiples(n):
    # main function
    # place your code here
    return total

# feel free to add extra functions to make your code more readable
# just make sure you don't change the name of the main function (sum_multiples)
# The main function is what the markerBot assesses.
def is_multiple(i):
    # you can name these functions whatever you want
```

*This is the first problem from [Project Euler](https://projecteuler.net/about). If you like math and enjoy these problem sets you will love project euler.*

**Bonus points:** This is very similar to a problem in session 1. Lets take it a step further. Change the function so that it the numbers we are checking are multiples of become arguments to the function. For example:

```
>>> sum_multiples(10, [3,5])
23
```

This sums all numbers below 10 that are multiples of 3 or 5. We know the answer to this is 23.

What is the sum of all numbers below 1000 that are multiples of 7, 13 or 23?

```
>>> sum_multiples(1000, [7,13,23])
```

*[7,13,23] is a python list. This is a sneak peak at next week where will be covering more python datatypes.*


## Prime Numbers

Create a function called `is_prime` that takes a single integer and returns `True` or `False` indicating whether or not the number is prime. A number is prime if its only even divisors are 1 and the number itself. For example, 7 is prime since it is only divisible by 1 and 7, but 14 is not prime since it is divisible by 1, 2, 7 and 14.

You will likely need to use some sort of loop inside your function.

Feel free to reseach prime numbers, but resist the temptation to copy algorithms found while googling.

Submit your function to the MarkerBot as shown below.

```py
def is_prime(n):
    # place your code here
    return n_is_prime_number
```

