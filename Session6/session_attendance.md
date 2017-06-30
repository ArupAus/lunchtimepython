
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

```
    {
        "name" : "Session Attendance",
        "question" : "We would like you to investigate attendance in the python course.",
        "function_name" : "session_attendance",
        "timeout" : 1.0,
        "args" : [["attendance.csv"]],
        "answers" : [{
            "by_attendee" : {
                "0_Sessions":0,
                "1_Sessions":0,
                "2_Sessions":1,
                "3_Sessions":1,
                "4_Sessions":7,
                "5_Sessions":11,
                "6_Sessions":8,
                "7_Sessions":5,
                "8_Sessions":13,
                "9_Sessions":4
            },
            "by_session" : {
                "Session_0":31,
                "Session_1":38,
                "Session_2":33,
                "Session_3":32,
                "Session_4":34,
                "Session_5":33,
                "Session_6":39,
                "Session_7":37,
                "Session_8":34
            }
        }]
    },

```