# Session 4: Working with Files

## A little theory

 - What is a relative path relative to?
 - What does an absolute path start with?
 - What are the . and .. folders?
 - In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
 - What are the three “mode” arguments that can be passed to the open() function?
 - What happens if an existing file is opened in write mode?
 - What is the difference between the read() and readlines() methods?


## Evaluating lines

Below is a snippet that will open and close a file, can you write some code that will evaluate the word count of line of text in example.txt
print it to the screen?

```py

f = open("example.txt", "w")
f.write("To write or not to write\nthat is the question!\n")
f.close()

f = open("example.txt", "r")

### your code here ###

f.close()

```

Example Output
```
> Line 0 word count: 6
> Line 1 word count: 4
```


## Chasing outstanding debts

In the resources folder on this GitHub page you will find a csv file of project debts - *debts.csv* (it is not real data). If the link does not work, you will find the file on our Yammer Page under the "files" tab.

A csv file looks likes an excel file, but it is actually just simple text separated by commas (hence Comma Separated Values - csv). Your task is to find the sum of all the debts listed in the csv file.
Below is a sample of what it looks like:
{: .table table-hover }
|Job Number|Debt|
|-----|------|
|243156|1235.63|
|236412|2356.21|
|315224|23.01|

What would the instructions look like to do this by hand? Surprisingly, the instructions for the computer are quite similar.

Below is some python code that you can copy and paste into your script to read the csv line by line. This time you will be using the 'with open() as ...:' statement instead of just open. It will behave in a similar manner. 

```py
import csv
with open("debts.csv") as csvfile:
  csvData = csv.DictReader(csvfile)
  for row in csvData:
    job_number = row['Job Number']
    debt = row['Debt']
    print(job_number, debt)
```
## Biggest debt

Based on the example above write a function 

```py
def biggest_debt(file_path):
    # your code here
    return job_number, debt
```
## Total debt

Based on the example above write a function 

```py
def total_debt(file_path):
    # your code here
    return debt
```

## Sorted debt

Based on the example above write a function that returns a list of tuples `(job_number, debt)` sorted in descending order. An example output might look like this  `[(260405, 33209.61), (233405, 22209.16), (260565, 339.10)]`

```py
def sorted_debt(file_path):
    # your code here
    return debt
```