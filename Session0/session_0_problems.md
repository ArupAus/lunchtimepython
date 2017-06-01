# Session 0: Getting Set up (Pre-Work)

As part of the pre work you have installed python and a text editor. You have also watched two videos from automate the boring stuff. In the videos you learned:
- Expressions and Statements
- Integers, floats and strings
- Variables

Aim of this problem set is to gently introduce you to the python interpreter and make sure everything is working.

Go to your start menu and select the program `IDLE (Python 3.6 64-bit)` inside the `Python 3.6` folder. This will load up the interpreter. Use this to explore the problems below.

## Python as a calculator
To use python as a calculator, simply type in the expression and press enter.

```
>>> (34/4.5)*3+4
26.666666666666664
```

What would the expression `(34/4.5)*(3+4)` evaluate to?

## Division
What is 17 divided by 3?
How many times does 3 divide into 17?
*HINT:* What is the diference between `17/3` and `17//3`?

## Working with strings

A string is a group of characters (Examples of characters: `'a'`, `'b'`, `'X'`, `'$'` or `'5'`). You string the characters together to create a string: `'abX$5'`

You can add strings together.
```py
my_string = 'I have eaten ' + '99' + ' burritos.'
```

You cannot add strings and other types together. Try it in the interpreter.
```py
my_string = 'I have eaten ' + 99 + ' burritos.'
```

How can you fix this?


## A little theory
It is usefule to distinguish between values and operators that act on values. Which of the following are operators and which are values?

```py
*
'hello'
-88.8
-
/
+
5
```

## Computers love arithmetic
Write a script that prompts the user for two numbers, multiplies the numbers together and prints the result to the console.

To print something to the screen:
```
>>> my_number = 55
>>> print(my_number)
55
```

To prompt the user to enter a number:
```py
# To prompt the user to enter a value
>>> my_string = input("Message to the user")
```




