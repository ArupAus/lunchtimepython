# Session SciPy Problems

In session 4 we learnt about the following:

1. Numpy
2. SciPy
3. Matplotlib

Visit the [SciPy](https://www.scipy.org/) website for documents and examples on all three.

We are going to use the data we gathered in the reading and writing files session (session 4) and do some plotting.

## A simple line graph
Plot a line graph for the functions `sin()` and `cos()` between `0` and `4\pi` using both `numpy` and `matplotlib`. The [Cheat Sheet](https://github.com/tomvalorsa/python-course/blob/master/cheat_sheet.md) will help you.

## A histogram of debt
In the [resources](https://github.com/tomvalorsa/python-course/tree/master/resources) folder on this GitHub page you will find a csv file of project debts - *debts.csv* (it is not real data). This data set was introduced in session 4 where you were asked to find the sum of all debts.

Below is a sample of what the data file looks like:

|Job Number|Debt|
|-----|------|
|243156|1235.63|
|236412|2356.21|
|315224|23.01|

Your task is to write a python program that plots a [histogram](https://en.wikipedia.org/wiki/Histogram) of the debts. There is an example in the [Cheat Sheet](https://github.com/tomvalorsa/python-course/blob/master/cheat_sheet.md). Is there a pattern of debts here?

The sample code given in session 4 is repeated below:
```py
import csv
with open("debts.csv") as csvfile:
  csvData = csv.DictReader(csvfile)
  for row in csvData:
    job_number = row['Job Number']
    debt = row['Debt']
    print(job_number, debt)
```



## Tails
Your dream job at the bureau of meteorology is going well. However, you decide that you would like to start investigating the [weather files](https://github.com/tomvalorsa/python-course/tree/master/resources/Session-4%20Tails) you have been given.

Using what you learned in session 4, write a python program that plots `Wind speed in m/s` vs `Speed of maximum windgust in last 10 minutes in  m/s` using a scatter plot. (A scatter plot is just a line graph where you use dots `'b.'` rather than a line `'b'`).

There seems to be a pattern here. What rule of thumb could you use to predict the wind gust from the wind speed?