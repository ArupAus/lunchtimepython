# Session 0 Solutions

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

## Chasing outstanding debts
In the resources folder on this GitHub page you will find a csv file of project debts - *debts.csv* (it is not real data). If the link does not work, you will find the file on our Yammer Page under the "files" tab.

A csv file looks likes an excel file, but it is actually just simple text separated by commas (hence Comma Separated Values - csv). Your task is to find the sum of all the debts listed in the csv file.
Below is a sample of what it looks like:

|Job Number|Debt|
|-----|------|
|243156|1235.63|
|236412|2356.21|
|315224|23.01|

What would the instructions look like to do this by hand? Surprisingly, the instructions for the computer are quite similar.

Below is some python code that you can copy and paste into your script to read the csv line by line.

```py
import csv
with open("debts.csv") as csvfile:
  csvData = csv.DictReader(csvfile)
  for row in csvData:
    jobNumber = row['Job Number']
    debt = row['Debt']
    print(jobNumber, debt)
```

*ANS:*
This is a tricky problem and is beyond what we had taught you in session 0. We justed want to show you how small and readable a program that reads a csv (excel) file can be.

```py
import csv
with open("debts.csv") as csvfile:
  csvData = csv.DictReader(csvfile)
  sum = 0
  for row in csvData:
    jobNumber = row['Job Number']
    debt = row['Debt']
    sum = sum + float(debt)
print("The sum of all debts is: $" + str(round(sum, 2)))
```
