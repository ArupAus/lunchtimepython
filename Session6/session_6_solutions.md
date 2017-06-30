# Session 6: Good Programming Practices

## Session Attendance

```py
def get_attendance_records(file_path):

    attendance_file = open(file_path,'r')
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

def session_attendance(file_path):
	number_of_sessions = 9
	session_attendance = {u'Session_0':0, u'Session_1':0, u'Session_2':0, u'Session_3':0, u'Session_4':0, u'Session_5':0, u'Session_6':0, u'Session_7':0, u'Session_8':0}
	attendee_consistency = {u'0_Sessions':0, u'1_Sessions':0, u'2_Sessions':0, u'3_Sessions':0, u'4_Sessions':0, u'5_Sessions':0, u'6_Sessions':0, u'7_Sessions':0, u'8_Sessions':0, u'9_Sessions':0}

	attendance_records = get_attendance_records(file_path)

	for record in attendance_records:
		record = record.strip('\n').split(',') # convert record from a string to a list
		sessions = convert_attendance_record_to_bools(record[2:])
		number_of_sessions = len(sessions)
		number_of_sessions_attended = str(sum(sessions))+'_Sessions'
		# add record to attendee_consitency dictionary
		attendee_consistency[number_of_sessions_attended] += 1
		# add record to session attendance dictionary
		for i in range(number_of_sessions):
            key = 'Session_'+int(i)
			session_attendance[key] += sessions[i]
    
    return {
        u"by_attendee" : attendee_consistency,
        u"by_session" : session_attendance
    }

```

## Common Words

```py
import string
import collections
from operator import itemgetter

IGNORE = {
    'a', 'also', 'an', 'and', 'are', 'as', 'be', 'by', 'can', 'do', 'for', 'from',
    'have', 'in', 'is', 'it', 'just', 'more', 'not', 'of', 'on', 'or', 'our',
    'over', 'than', 'that', 'the', 'their', 'these', 'they', 'this', 'those',
    'to', 'up', 'we', 'with'
}

def build_word_counter(file_path):
    with open(file_path, 'r') as f:
        speech = f.read()
        chars_to_remove = list(string.punctuation) + ['\n'] + list(string.digits)
        for char in chars_to_remove:
            speech = speech.replace(char, '')
    
    return collections.Counter(w.lower() for w in speech.split() if w not in IGNORE)

def common_words(file_path):
    word_counter = build_word_counter(file_path)
    return sorted(w for w in word_counter if word_counter[w] > 10)

def most_used_words(file_path):
    word_counter = build_word_counter(file_path)
    word_counter_sorted = sorted(word_counter.most_common(20), key=itemgetter(1,0))
    return [word for word, _ in word_counter_sorted]
```

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
