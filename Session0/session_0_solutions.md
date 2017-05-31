# Session 0: Getting Set up (Pre-Work)

## A little theory
Which of the following are operators, and which are values?

*ANS:*

```py
*		operator
'hello'	value
-88.8	value
-		operator
/		operator
+		operator
5		value
```

Why does this expression cause an error? How can you fix it?

```py
'I have eaten ' + 99 + ' burritos.'
```

*ANS:*
The + operator cannot add an integer (int) to a string (str). you must convert the integer to a string first.

```py
'I have eaten ' + str(99) + ' burritos.'
```

## Computers love arithmetic
Write a script that prompts the user for two numbers, multiplies the numbers together and prints the result to the console.

```py
# To prompt the user to enter a value
my_string = input("Message to the user")
```

*ANS:*
```py
# this will only work if the user enters whole numbers (integers)
number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
number3 = int(number1)*int(number2)
print(number1 + " times " + number2 + " equals " + str(number3))
```

## Division
What is 17 divided by 3?
How many times does 3 divide into 17?

*ANS:*
Welcome to integer arithmetic.

17 divided by 3:
17/3 = 5.666666666667

3 divides into 17:
17//3 = 5