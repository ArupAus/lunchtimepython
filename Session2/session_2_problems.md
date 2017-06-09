# Session 2: Basics Part B

## A little theory

These are thought questions - there are probably several right answers.

- How can using a function make your code shorter?
- How can using a function make your code easier to change?
- How can using a function make your code more readable?

## How Long is a Strings

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

Create a function called `print_triangle` that takes a single integer and returns a sideways *triangle* of that height, made of *'s. For example:

```
>>> print_triangle(5)
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
def print_triangle(n):
    # place your code here
    return triangle
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

def is_multiple(i):
    # feel free to add extra functions to make your code more readable
    # you can name these functions whatever you want
    # just make sure you don't change the name of the main function (sum_multiples)
```

*This is the first problem from [Project Euler](https://projecteuler.net/about). If you like math and enjoy these problem sets you will love project euler.*

## Prime Numbers

Create a function called `is_prime` that takes a single integer and returns `True` or `False` indicating whether or not the number is prime. A number is prime if its only even divisors are 1 and the number itself. For example, 7 is
prime since it is only divisible by 1 and 7, but 14 is not prime since it is divisible by 1, 2, 7 and 14.

You will likely need to use some sort of loop inside your function.

Feel free to reseach prime numbers, but resist the temptation to copy algorithms found while googling.

Submit your function to the MarkerBot as shown below.

```py
def is_prime(n):
    # place your code here
    return n_is_prime_number
```

