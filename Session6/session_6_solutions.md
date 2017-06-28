# Session 6: Good Programming Practices


## Password Generator

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

The solution
```py
import os
import string
import random

FILENAME = 'words.txt'
WORDS_FILE_PATH = os.path.join(os.getcwd(), 'Resources', FILENAME)

def get_words_from_file(minimum_word_len = 4):
    with open(WORDS_FILE_PATH,'r') as f:
        lines = f.readlines()

    all_words = lines[0].split()

    filtered_words = []
    for word in all_words:
        if len(word) >= minimum_word_len:
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
    minimum_word_len = 4
    number_of_words = 2
    number_of_digits = 3

    list_of_words = get_words_from_file(minimum_word_len)

    password = select_random_words(list_of_words, number_of_words) + generate_random_numbers(number_of_digits)

    return password
```

The checker
```py

import re
import os
import string

# Might need to change the file path??
FILENAME = 'words.txt'
WORDS_FILE_PATH = os.path.join(os.getcwd(), 'Resources', FILENAME)

def get_words_from_file(minimum_word_len = 4):
    with open(WORDS_FILE_PATH,'r') as f:
        lines = f.readlines()

    all_words = lines[0].split()

    filtered_words = []
    for word in all_words:
        if len(word) >= minimum_word_len:
            filtered_words.append(word)

    return filtered_words

def check_password_correct():

    password = generate_password()

    password_words = re.findall(r'[A-Z][a-z]+', password)
    password_digits = re.findall(r'[0-9]+', password)[0]

    if len(password_words) != 2:
        return False
    if len(password_digits) != 3:
        return False

    possible_words = set(get_words_from_file())
    possible_digits = set(string.digits)

    for digit in password_digits:
        if digit not in possible_digits:
            return False
    for word in password_words:
        if word.lower() not in possible_words:
            return False
    
    return True
```

## Session Attendance

A Solution

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

```py
import os
import string
import collections

FILEPATH = os.path.join(os.getcwd(), 'Resources', '2016_budget_speech.txt')

IGNORE = {
    'a', 'also', 'an', 'and', 'are', 'as', 'be', 'by', 'can', 'do', 'for', 'from',
    'have', 'in', 'is', 'it', 'just', 'more', 'not', 'of', 'on', 'or', 'our',
    'over', 'than', 'that', 'the', 'their', 'these', 'they', 'this', 'those',
    'to', 'up', 'we', 'with'
}

with open(FILEPATH, 'r') as f:
    speech = f.read()
    chars_to_remove = list(string.punctuation) + ['\n'] + list(string.digits)
    for char in chars_to_remove:
        speech = speech.replace(char, '')

word_counter = collections.Counter(w.lower() for w in speech.split() if w not in IGNORE)

def common_words():
    return sorted(w for w in word_counter if word_counter[w] > 10)

def most_used_words():
    return [word for word, _ in word_counter.most_common(20)]
```