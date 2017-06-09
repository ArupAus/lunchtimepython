# Session 6: Good Programming Practices

In session 5 we learned:

1. Errors and Exceptions
2. Debugging and testing using logging

Take the opportunity to practice everything that you have learned in the course so far. Use the concepts taught in session 5 to help debug and test your programs.

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

__ANS:__

```py
import string
import random

def generate_password():
	possible_chars = string.ascii_letters + string.digits # what is string.ascii_letters and string.digits ?
	password = ''
	while len(password)<12:
		password += random.choice(possible_chars)
	return password

```

## Human Password Generator

Who can remember a password like the ones generated above. Lets build another password generator. This time lets combine two random words and three numbers. It will be much easier to remember.

In the [resources](https://github.com/tomvalorsa/python-course/tree/master/resources) folder in this github page you will find a very long list of words to choose from. Write a function called `generate_password2` that returns a random password as described above. This problem will require some careful planning. Try to break the problem down into logical sub-problems and build functions. Here is a few likely sub-problems to get you started:

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

__ANS:__

```py
import os
import string
import random

def get_words_from_file(minimum_word_len = 3):
	words_file_name = 'words.txt'
	words_file_path = "D:\\SoftwareProjects\\PythonCourse\\python-course\\resources\\Session-5" # replace with your working directory
	words_full_file_path = os.path.join(words_file_path, words_file_name)

	words_file = open(words_full_file_path,'r')
	lines = words_file.readlines()
	words_file.close()

	all_words = lines[0].split()

	filtered_words = []
	for word in all_words:
		if len(word) > minimum_word_len:
			filtered_words.append(word)

	return filtered_words


def generate_random_numbers(number_of_digits):
	numbers = ''
	while len(numbers)<number_of_digits:
		numbers += random.choice(string.digits)
	return numbers


def select_random_words(list_of_words, number_of_words):
	passwords = ''
	for i in range(number_of_words):
		random_word = random.choice(list_of_words)
		passwords += random_word.title() # make first letter uppercase
	return passwords


def generate_password():
	minimum_word_len = 5
	number_of_words = 2
	number_of_digits = 3

	list_of_words = get_words_from_file(minimum_word_len)

	password = select_random_words(list_of_words, number_of_words) + generate_random_numbers(number_of_digits)

	return password

# now run:
generate_password()
```

## Session Attendance

We would like you to investigate attendance in the python course. In the [resources](https://github.com/tomvalorsa/python-course/tree/master/resources) folder in this gitbhub page there is a csv file with recorded attendance for sessions 0-8. We would like to know two things from the data set:

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

__ANS:__
```py
import os

def get_attendance_records():
    attendance_file_name = 'attendance.csv'
    attendance_file_path = "D:\\SoftwareProjects\\PythonCourse\\python-course\\resources\\Session-5" # replace with your working directory
    attendance_full_file_path = os.path.join(attendance_file_path, attendance_file_name)

    attendance_file = open(attendance_full_file_path,'r')
    lines = attendance_file.readlines()
    attendance_file.close()

    header = lines[0]
    attendance_records = lines[1:]

    return attendance_records

def convert_attendance_record_to_bools(sessions):
    sessions_bool = []
    for session in sessions:
        if session == 'Yes':
            sessions_bool.append(1)
        else:
            sessions_bool.append(0)
    return sessions_bool

def print_session_attendance(session_attendance):
    print('------------------------------')
    print('Attendance for each sessions')
    print('------------------------------')
    for session, attendance in session_attendance.items():
        print("Session {0}: {1}".format(session, attendance))
    print('------------------------------')

def print_attendee_consistency(attendee_consistency):
    print('------------------------------')
    print('Attendee consistency')
    print('------------------------------')
    for sessions, attendance in attendee_consistency.items():
        print("{0} People attended {1} sessions".format(attendance, sessions))
    print('------------------------------')

def session_attendance():
	number_of_sessions = 9
	session_attendance = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
	attendee_consistency = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

	attendance_records = get_attendance_records()

	for record in attendance_records:
		record = record.strip('\n').split(',') # convert record from a string to a list
		sessions = convert_attendance_record_to_bools(record[2:])
		number_of_sessions = len(sessions)
		number_of_sessions_attended = sum(sessions)
		# add record to attendee_consitency dictionary
		attendee_consistency[number_of_sessions_attended] += 1
		# add record to session attendance dictionary
		for i in range(number_of_sessions):
			session_attendance[i] += sessions[i]


	print_attendee_consistency(attendee_consistency)
	print_session_attendance(session_attendance)

# to run the script
session_attendance()
```

## Common Words

Have you ever listened to a politician give a speech?
In the [resources](https://github.com/tomvalorsa/python-course/tree/master/resources) folder there is a .txt copy of the 2016 budget speech delivered by Honourable Scott Morrison MP, Treasurer of the Commonwealth of Australia - download this file and save it in your working directory. For the more adventurous types, there is also a recent speech by Donald Trump.

We would like to find out a few things from the speech:

1. What words occur more than 10 times?
2. What were the 20 most frequently used words?
3. How could you make these results more interesting/relevant? (for example, by removing words with < 3 letters)

A simple approach (for parts 2 and 3) we would recommend is to use a dictionary to store words and their corresponding frequencies.
You will need to extract each word from the speech individually, remembering that 'Tax' is not the same as 'tax' (hint: or 'tax,').

How would you extract each word from the following sentence? "Tax, tax and more tax."

Important to note here: dicionaries are by their python definition unordered. Lists on the other hand, can be ordered (sorted), for example:
```
>>> myList = [3, 1, 9, 2, 15, 32]
>>> sortedList = sorted(myList)
>>> sortedList
[1, 2, 3, 9, 15, 32]

>>> myList.sort()
>>> myList
[1, 2, 3, 9, 15, 32]
```
The `sorted(list)` method takes a list and returns a list sorted by value (smallest to largest).
The `list.sort()` method sorts a list in its place.
You can reverse the order of either of these functions by including `reverse = True` as an argument, for example `sorted(list, reverse = True)`.

A generic code snippet that returns (key, value) tuple pairs from a dictionary:
```
>>> animal_frequency = {'frog':5, 'antelope':2, 'toucan':3}
>>> letter_frequency.items()
dict_items([('antelope', 2), ('frog', 5), ('toucan', 3)])
```

This is not in any particular order. How would you sort these values by their frequencies?
A sample output is shown below:

```
[('the', 198), ('and', 164), ('will', 81), ('for', 69), ('tax', 69), ('our', 53), ('this', 47), ('are', 38), ('that', 37), ('jobs', 37)]
```
__ANS__

Loading the words into a dictionary with their respective frequencies:
```py
text_file = open('2016_budget_speech.txt', 'r')
lines = text_file.readlines()
text_file.close()

stripped_words=[]
word_freq={}

# here we split all lines by spaces,
# then strip words of all punctuation,
# and append to stripped_words
for line in lines:
    for word in line.lower().split(' '):
        stripped_words.append(word.strip(',\n.;:"- /'))

# add each word to the dictionary
# if the word exists, add 1 to the counter
# if not, set the counter = 1
for word in stripped_words:
    # test if in dictionary
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
```

Now all the words from the speech have been loaded into `word_freq`. Go ahead - type `print(word_freq)` and see what happens.

If we want to see which words occur more than 10 times, we can iterate through the dictionary, and only print a word (key) if its frequency (value) is > 10:

```py
for word in word_freq.items():
	if word[1] > 10:
        	print(word)
```
But this doesn't give us anything particularly useful. Instead let's write a function that accepts a dictionary:

```py

# previous code here

# function to sort a dictionary, returning a list of tuples sorted by value
def sortDict(dictionary):

    # initialise two lists, one for unsorted tuples and one for sorted tuples    
    unsorted_words = []
    sorted_words = []

    # if word in dictionary is longer than 2 characters, append to unsorted_words
    for item in dictionary.items():
        if len(item[0]) > 2:
            unsorted_words.append(item)

    # sort words in unsorted_words by their frequencies, but remember to add the first word to the list!
	# we can iterate through the words in unsorted_words, and compare their frequencies to words that
	# are already in sorted_words, inserting them in the right spot.
    for item in unsorted_words:
        if len(sorted_words) == 0:
            sorted_words.append(item)
        else:
            for i in range(len(sorted_words)):
                if item[1] > sorted_words[i][1]:
                    sorted_words.insert(i, item)
                    break
                if item[1] < sorted_words[-1][1]:
                    sorted_words.append(item)

	# return a list of tuples
    return(sorted_words)

# Now we can just run the function with our list, printing only the first 10 values
print(sortDict(word_freq)[:10])
```

which should give us...

```
>>> [('the', 198),
 ('and', 164),
 ('will', 81),
 ('for', 69),
 ('tax', 69),
 ('our', 53),
 ('this', 47),
 ('are', 38),
 ('that', 37),
 ('jobs', 37)]
```