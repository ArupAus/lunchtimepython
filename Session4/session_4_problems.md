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

## Tails

You land your dream job at the bureau of meteorology and the weather is your oyster. Your first job is to check the logs of weather stations around your area and make that the data is being recorded correctly. Using your wealth of programming knowledge you devise a plan to write a python program that will do you work for you while you kick back and daydream what an aurora borealis tornado might look like.

Write a program That:

1. reads the recordings from all logs
2. performs some form of check to see whether the logging data appears correct
3. based on the outcome of the check will print to the screen a message

__Pro tips__

 - Save the folder WeatherData frome the Resources folder from gitlab to your desktop 
 - Save your python program in a place where you can access these files 'relatively' easily
 - Dont rush to code, break down the step on paper first
 - Ask questions, lots of them

```py
# Create a list of logs
WORKING_DIR = # example 'c:\\Users\\guest\\Desktop\\Session-4 Tails\\'
logs = ...your code here


for log in logs:
	
	f = open(log, "r")
	# ...your code here. get the last n recordings from the file. 
	# Think about how would you check if the recordings are likely to be valid?
	
	f.close()
```

Example Outputs
```
> Weather Station Adelaide recordings appear valid
> Weather Station Sydney recordings seem fishy... take a better look
```


## Personable Greg

Greg has made an executive decision that the Arup Board needs to be more engaged with its younger employees and overly formal communication is only making the board look even more out of touch. He has decided that all employees under the age of 30 should recieve a less formal emails. Furthermore, there should be numerous random greetings so that the emails appear more personable.

Greg's go to developer is on holiday at the moment and you step in to help her out. You are given the code below which is almost complete. She has done a good job and left *TODO* notes in her code where it needs fixing. Building the code as is will generate a template but its not quite finished yet. 

__Pro tips__

 - Save the `template.html` and `employees.csv` from github resources folder named PersonableGreg in the Resources folder into a folder on your desktop
 - Copy the code below and save it in a place where you can access the `template.html` and `employees.csv` easily, build the code first to how it works then start to make required changes
 - Direct your output to a folder where things wont get too messy
 - Dont rush to code, break down the step on paper first
 - Ask questions, lots of them

```py
import random

# TODO:
# 1. fix write_personal_email() so it greets/signs off properly 
# 2. read employees file and loop through calling write_personal_email() with details from Employees.csv


def write_personal_email(template, destination, first_name, last_name, age):

    hip_greetings = ['yo', 'hola', 'what up', 'whats crackin']
    hip_sign_offs = ['laters', 'cya', 'hasta luego', 'peace', 'ya boi'] # feel free to add more
    
    normal_greeting = 'Dear'
    normal_signoff = 'Regards'
    
    # open template html
    f = open(template, 'r+')

    # read all the lines in from the template email
    lines = f.readlines()
    f.close()

    # intialise a list to append lines to once 'personalised'
    personalised_message = []

    for line in lines:
        
        if '{{FIRST_NAME}}' in line:
            line = line.replace('{{FIRST_NAME}}', first_name)
        if '{{LAST_NAME}}' in line:
            line = line.replace('{{LAST_NAME}}', last_name)
        
        # TODO: add more conditional statements to select random 
        # greeting and sign off from using random.choice(hip_greetings)
        # The tags to replace are {{GREETING}} and {{SIGN_OFF}}
        # remember only use hip greeting if age < 30
        
        personalised_message.append(line)


    # open a new file to personalised message
    f_out = open(destination + first_name + last_name + '.html', 'w')

    # loop through personal message and write to personal file
    for line in personalised_message:
        f_out.write(line+'\n')
    
    f_out.close()


write_personal_email('template.html','', 'Joe', 'Blogs', 25) # run like this to test function


# TODO: read employee csv and loop through each line calling 

# f = open('Employees.csv', 'r+')

# read all the lines in from the template email
# lines = f.readlines()

# for line in lines:

    # TO DO: use line.split function to process data from Employees.csv and then call
    # write_personal_email(destination, firstname, lastname, age)

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
