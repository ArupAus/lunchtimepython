# Session 4: Working with Files

## A little theory

 - What is a relative path relative to?
 - What does an absolute path start with?
 - What are the . and .. folders?
 - In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
 - What are the three “mode” arguments that can be passed to the open() function?
 - What happens if an existing file is opened in write mode?
 - What is the difference between the read() and readlines() methods?

## Warm up

A super useful method when dealing with strings is the `.split()` and `.replace()` methods. Fire up the python shell and copy the following in to see how it works.
Try splitting by different characters and see what you come up with. 
```
>>> words = “This is random text we’re going to split apart”
>>> words2 = words.split(' ')
>>> words2

['This', 'is', 'random', 'text', 'we're', 'going', 'to', 'split', 'apart']


>>> words.replace('random', 'specified')
'This is specified text we’re going to split apart'

```

Below is a snippet that will open a text file named `example.txt` write some content and close a file. Can you write some code that will evaluate the word count of line of text in `example.txt` and print it to the screen?

```py

## write some content into a file
f = open("example.txt", "w")
f.write("To write or not to write\nthat is the question!\n")
f.close()


## open and read some content in a file
f = open("example.txt", "r")
lines = f.readlines() # reads all lines in a file into a list of strings
for line in lines:
    # remove \n from your lines using
    line.replace('\n', '')
    
    ### your code here ###

f.close()

```

Example Output
```
> Line 0 word count: 6
> Line 1 word count: 4
```

### longest_line
Write a function that will find the line with the greatest number of words and return a dict with the line number and number of words. Line numbers start at 0 for this problem.

For example, the text below
```
Coconut is a functional programming language that compiles to Python.
Since all valid Python is valid Coconut, using Coconut will only extend and enhance what you're already capable of in Python.
Why use Coconut? Coconut is built to be useful.
```
would yield
```
{"line_number":1, "num_words":21}
```

This time you will be using the `with open() as ...:` statement instead of just open. It will behave in a similar manner but will automatically close the file after it reaches the end of the indentation. 

Supply your text file to the funciton via the `file_path` argument and the character you wish to split lines by with the `split_char` arg. 

In the event of a tie for total number of words in a line, return the last occurence

```py
def longest_line(file_path, split_char):
    with open(file_path, 'r') as input_file:
        # your code here

    return {u'line_number': line_number, u'num_words': num_words}
```
__* leave the u in front of the keys in the dictionary you return.__


### longest_line_string

In the event of a tie for total number of words in a line return the line with the longest string in the line. Line numbers start at 0 for this problem.

```py
def longest_line_string(file_path, split_char):
    with open(file_path, 'r') as input_file:
        # your code here

    return {u'line_number': line_number, u'num_words': num_words, u'longest_string_length':longest_string_length}
```
__* leave the u in front of the keys in the dictionary you return.__

## Chasing outstanding debts

Click this link to download - [*debts.csv*](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session4/Resources/debts.csv) (it is not real data).

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
with open("debts.csv", 'rU') as csvfile:
  csvData = csv.DictReader(csvfile)
  for row in csvData:
    job_number = row['Job Number']
    debt = row['Debt']
    print(job_number, round(debt, 2))
```
### biggest_debt

Based on the example above write a function that returns the job number and amount of the biggest debt `biggest_debt`. In the event of a tie for biggest debt return the last occurence

```py
def biggest_debt(file_path):
    # your code here
    return {u'job_number': job_number, u'debt': round(debt, 2)}
```
__* leave the u in front of the keys in the dictionary you return.__

### total_debt

Based on the example above write a function that calculates the total debt for a given file. Return a single number that equal the total debt from a given csv file

```py
def total_debt(file_path):
    # your code here
    return round(debt, 2)
```

### sorted_debt

Based on the example above write a function that returns a list of dicts `{u'job_number': 123456, u'debt': 323}` sorted in descending order of debt. An example output might look like this

```py
[
    {u'job_number': 260405, u'debt': 33209.61},
    {u'job_number': 233405, u'debt': 22209.16},
    {u'job_number': 260565, u'debt': 339.10}
]
```

```py
def sorted_debts(file_path):
    # your code here
    # do not round your debts in this exercise!
    debts = []
    #leave a 'u' in front of the keys in the dictionary you return

    return debts
```