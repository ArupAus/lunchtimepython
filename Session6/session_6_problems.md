# Session 6: Good Programming Practices

Take the opportunity to practice everything that you have learned in the course so far. Use the concepts taught in session 6 to track your work on git if you like. Feel free to push your work to gitlab and collaborate with others.

## Session Attendance

We would like you to investigate attendance in the python course. In the [resources folder](https://github.com/ArupAus/lunchtimepython/tree/2017/Session6/Resources) in our github repo you will find a csv file with recorded attendance for sessions 0-5 **attendance.csv**. Download it and use it for the following problem. We would like to know two things from the data set:

1. What was the attendance for each session (to determine popular sessions)
2. What was the attendance for each person (to determine if people are consistently attending sessions)

Again, plan carefully for this problem. Think about the steps to solve the problem and break it down into functions.

Submit your function to the MarkerBot as shown below.

```py
def session_attendance(file_path):
    # use file_path as an argument to your function
    # so that the MarkerBot can assess your answer.
    return attendance_dict
```

To make our lives easier with assessing your answer. Format the above into a dictionary and have you function return the dictionary instead of the output above. The resulting dictionary should look like:

```py
attendance_dict = {
    u"by_attendee" : {
        u"0_Sessions":0,
        u"1_Sessions":0,
        u"2_Sessions":1,
        u"3_Sessions":1,
        u"4_Sessions":7,
        u"5_Sessions":11,
        u"6_Sessions":8,
        u"7_Sessions":5,
        u"8_Sessions":13,
        u"9_Sessions":4
    },
    u"by_session" : {
        u"Session_0":31,
        u"Session_1":38,
        u"Session_2":33,
        u"Session_3":32,
        u"Session_4":34,
        u"Session_5":33,
        u"Session_6":39,
        u"Session_7":37,
        u"Session_8":34
    }
}
```

**Bonus points:**

Write a function that prints the dictionary like the following:

```
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

In the [resources folder](https://github.com/ArupAus/lunchtimepython/tree/2017/Session6/Resources) in our github repo you will find a copy of the 2016 budget speech delivered by Honourable Scott Morrison MP, Treasurer of the Commonwealth of Australia **2016_budget_speech.csv**. Download it and use it for the following problem.

We would like to find out a few things from the speech:

1. What words occur more than 10 times?
2. What were the 20 most frequently used words that are longer than 3 characters (this will ignore 'the', 'and' etc)?



You will need to extract each word from the speech individually, remembering that we should consider 'Tax' as the same word as 'tax' and 'tax,'. Though python certainly will consider these the same. A simple approach is to use a dictionary to store words and their corresponding frequencies.

```
>>> animal_frequency={'frog':5, 'antelope':2, 'toucan':3}
>>> for word, frequency in animal_frequency.items():
        print(word, frequency)
toucan 3
antelope 2
frog 5
```

To make things more interesting, lets ignore the boring words:

```py
IGNORE = [
    'a', 'also', 'an', 'and', 'are', 'as', 'be', 'by', 'can', 'do', 'for', 'from',
    'have', 'in', 'is', 'it', 'just', 'more', 'not', 'of', 'on', 'or', 'our',
    'over', 'than', 'that', 'the', 'their', 'these', 'they', 'this', 'those',
    'to', 'up', 'we', 'with'
]
```

Answer the two questions above by submitting two separate functions to the MarkerBot. The functions signatures are shown below. **Read the comments carefully!** Your functions must return the list of words in a very particular format for the MarkerBot to assess the functions correctly.

The [python website](https://docs.python.org/3/howto/sorting.html#sortinghowto) has a great page on sorting.

### The most common words.
```py
def common_words(file_path):
    # Use file_path as an argument to your function so that the MarkerBot can assess your answer.
    #
    # Return the list of words that occur more than 10 times in alphabetical order.
    #
    # Don't forget to ignore the words in the list above.
    #
    return words # this must be a list

# you can use additional functions (in fact you should). Just make sure you submit the two functions above without changing the name of these functions.
```

### Most frequent words.
```py
def most_used_words(file_path):
    # Use file_path as an argument to your function so that the MarkerBot can assess your answer.
    #
    # Return the list of the 20 most frequently used words in ascending order (from least commone to most common).
    # If two words have the same frequency, order them in alphabetical order.
    #
    # don't forget to ignore the words in the list above.
    #
    return words # this must be a list

# you can use additional functions (in fact you should). Just make sure you submit the two functions above without changing the name of these functions.
```

### The following questions cannot be not marked by the MARKBOT. They are bonus problems.

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
    return password

```

Sample input/output
```
>>> generate_password()
d9WDf9F35fsg
```

This definitely produces a secure password (see note at bottom of page). There are actually 62^12 different combinations, thats 3,226,266,762,397,899,821,056 possible passwords!!!

## Human Password Generator

Who can remember a password like the ones generated above. Lets build another password generator. This time lets combine two random words and three numbers. It will be much easier to remember.

In the [resources folder](https://github.com/ArupAus/lunchtimepython/tree/2017/Session6/Resources) in our github repo you will find a .txt file with 80,000 words, **words.txt**. Write a function called `generate_password2` that returns a random password as described above. This problem will require some careful planning. Try to break the problem down into logical sub-problems and build functions. Here is a few likely sub-problems to get you started:

1. read the words.txt file
2. build a `list` of words from the file (ignore words less than 4 characters long)
3. randomly select two words from the list and three numbers
4. combine words and numbers into one string and return to the user

**NOTE: The files words.txt is a big single line file. i.e. there are no line breaks.**

Sample input/output
```
>>> generate_password2()
BakedFool112
>>> generate_password2()
BlackMandarin685
```

Note that the first letter of each word is capitalised.

### DISCLAIMER: You should do some more reading about random password generators before you attempt to use these functions. It turns out that random.choice is not really random...