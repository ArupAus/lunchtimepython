# Session 6: Good Programming Practices

Take the opportunity to practice everything that you have learned in the course so far. Use the concepts taught in session 6 to track your work on git. Feel free to push your work to gitlab and collaborate with others.

## Password Generator

The first tool that hackers use to crack passwords is social engineering. Social engineering essentially involves stalking you on social media, email etc and guess your password from birthdays and family names. Lets write a python program that generates a password on request that cannot be subject to social engineering hacking.

First lets build a completely random password. Write a function called `generate_password` that generates a password of 12 characters. The code below will help you get started.

```py
import string
import random

def generate_password():
	possible_chars = string.ascii_letters + string.digits # what is string.ascii_letters and string.digits ?
	password = ''
	# write your python code here
	# use a for loop and look into (google) python's random.choice module

```

Sample input/output
```
>>> password = generate_password()
>>> print(password)
d9WDf9F35fsg
```

This definitely produces a secure password. There are actually 62^12 different combinations, thats 3,226,266,762,397,899,821,056 possible passwords!!!

## Human Password Generator

Who can remember a password like the ones generated above. Lets build another password generator. This time lets combine two random words and three numbers. It will be much easier to remember.

In the resources folder in this gitlab page you will find a .txt file with 80,000 words. Write a function called `generate_password2` that returns a random password as described above. This problem will require some careful planning. Try to break the problem down into logical sub-problems and build functions. Here is a few likely sub-problems to get you started:

1. read the words.txt file
2. build a `list` of words from the file
3. randomly select two words from the list and three numbers
4. combine words and numbers into one string and return to the user

Sample input/output
```
>>> password = generate_password2()
>>> print(password)
bakedfool112
>>> password2 = generate_password2()
>>> print(password2)
blackmandarin685
```

Consider building a small library using the folder structure we recommended.

## Session Attendance

We would like you to investigate attendance in the python course. In the resources folder in this gitblab page there is a csv file with recorded attendance for sessions 0-5. We would like to know two things from the data set:

1. What was the attendance for each session (to determine popular sessions)
2. What was the attendance for each person (to determine if people are consistently attending sessions)

Again, plan carefully for this problem. Think about the steps to solve the problem and break it down into functions.

A sample of the output of the analysis is shown below.
```
>>> print(session_attendance())
------------------------------
Attendee consistency
------------------------------
0 People attended 0 sessions
0 People attended 1 sessions
1 People attended 2 sessions
1 People attended 3 sessions
7 People attended 4 sessions
11 People attended 5 sessions
8 People attended 6 sessions
5 People attended 7 sessions
13 People attended 8 sessions
4 People attended 9 sessions
------------------------------
------------------------------
Attendance for each sessions
------------------------------
Session 0: 31
Session 1: 38
Session 2: 33
Session 3: 32
Session 4: 34
Session 5: 33
Session 6: 39
Session 7: 37
Session 8: 34
------------------------------
```
## Common Words

Have you ever listened to a politician give a speech?
In the resources folder there is a .txt copy of the 2016 budget speech delivered by Honourable Scott Morrison MP, Treasurer of the Commonwealth of Australia - download this file and save it in your working directory.

We would like to find out a few things from the speech:

1. What words occur more than 10 times?
2. What were the 20 most frequently used words?
3. How could you make these results more interesting/relevant? (hint: remove words with < 3 letters)

A simple approach (for parts 2 and 3) we would recommend is to use a dictionary to store words and their corresponding frequencies.
You will need to extract each word from the speech individually, remembering that 'Tax' is not the same as 'tax' (hint: or 'tax,').

How would you extract each word from the following sentence: "Tax, tax and more tax."

A generic code snippet that prints the key-value pairs from a dictionary:

```
>>> animal_frequency={'frog':5, 'antelope':2, 'toucan':3}
>>> for word, frequency in letter_frequency.items():
		print(word, frequency)
toucan 3
antelope 2
frog 5
```

This is not in any particular order. How would you sort these values by their frequencies?

A sample output is shown below:

```
Word: 'the', frequency: 198 
Word: 'and', frequency: 164
Word: 'will', frequency: 80
Word: 'for', frequency: 69
Word: 'tax', frequency: 65
Word: 'our', frequency: 53
Word: 'this', frequency: 46
Word: 'are', frequency: 38
Word: 'that', frequency: 37
Word: 'their', frequency: 36
Word: 'jobs', frequency: 36
Word: 'new', frequency: 30
```
