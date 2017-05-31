# Session 2: Basics Part B

## A little theory

These are thought questions - there are probably several right answers.

- How can using a function make your code shorter?
- How can using a function make your code easier to change?
- How can using a function make your code more easily readable?

## Find the longer of two strings

Create a function called `longer_string` that takes two strings and returns the
longer one. For example,

```python
longer_string("Ove", "Arup") # returns "Arup"
```

## Print out a triangle

Create a function called `print_triangle` that takes a single integer and
prints out a sideways 'triangle' of that height, made of *'s or #'s or @'s or
whatever you feel like. For example, `print_triangle(5)` might print out

```
*
**
***
****
*****
```

Hint: Python's ability to 'multiply' a string by an integer may prove useful.

Bonus points: make a pyramid instead.

## Check if a number is prime

Create a function called `is_prime` that takes a single integer and returns
`True` or `False` indicating whether or not the number is prime. A number is
prime if its only even divisors are 1 and the number itself. For example, 7 is
prime since it is only divisible by 1 and 7, but 14 is not prime since it is
divisible by 1, 2, 7 and 14.

You will likely need to use some sort of loop inside your function.

