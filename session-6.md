# Session 6 Problems

In session 6 we learnt about the following:

1. Datetime
2. Interfacing with Excel

Recall from session 4:

1. Reading, editing and writing text and csv files
2. Regular expressions

## Some theory to get us going...

The Unix time variable (timestamp) is based on the total seconds elapsed from the Unix Epoch (12 AM 1st January 1970 UTC).

```
>>> import time
>>> time.time()
1471568701.1974244
```
When we call ```time.time()``` we can assign it to a variable, eg ```time_now = time.time()``` and perform operations as usual - remember this operates in seconds.
```
>>> import time
>>> before = time.time()
>>> after = time.time()
>>> after - before
4.694000005722046
```
We can also call ```datetime.datetime.now()``` which will return a datetime object, which can then be formatted. 
```
>>> import datetime
>>> date_today = datetime.datetime.now()
>>> date_today
datetime.datetime(2016, 8, 22, 8, 46, 4, 937283)
>>> date_today.strftime('%d/%m/%Y')
'22/08/2016'
>>> date_today.strftime('%H:%M:%S')
'08:46:04'
>>> date_today.strftime('The date is %d/%m/%Y, the time is: %H:%M:%S')
'The date is 22/08/2016, the time is: 08:46:04'
```
We can advance or rewind a particular datetime by using ```datetime.timedelta()```.
```
>>> import datetime
>>> time_now = datetime.datetime.now()
>>> time_later = time_now + datetime.timedelta(days=10, hours=5, minutes=24, seconds=12)
>>> time_later.strftime('%H:%M:%S %d/%m/%Y')
'14:16:43 01/09/2016'
```

When we are running a program (for example a ```for``` loop), we can delay the program using the ```time.sleep()``` function:

```
>>> import time
>>> def wait_ten_seconds():
	    print('Waiting for 10 seconds')
	    time.sleep(10)
	    print('Finished!')
>>> wait_ten_seconds()
Waiting for 10 seconds
Finished!
```

## Hints and best practice

Often to cancel a running python script you can push CTRL-C.
Due to the nature of the time.sleep() function, it cannot be interrupted.

Instead of this:

```py
def delay_function(seconds):
  time.sleep(seconds)
  print('Delay complete')
```
try this:
```py
def delay_function(seconds):
  for i in range(seconds):
    time.sleep(1)
  print('Delay complete')
```

## Pip Install

Python can interract with .xlsx files in a similar way to .csv files seen in previous sessions.

To do so, we need to install a library called ```openpyxl```, using a service called ```pip-install```. Unfortunately to do so requires administrator rights to the computer that you're using - if you're on your own laptop, great, otherwise you'll have to come back to this part.

If you're on your own laptop, you will need to add environment variables to use pip-install.

Go to Start > Control Panel > System > Advanced System Settings > Advanced > Environment Variables.
You will need to add two new system variables - Click New... and add the following:

Name: http_proxy  
Value: proxy.ha.arup.com:80

Name: https_proxy  
Value: proxy.ha.arup.com:80

Now open cmd.exe from the start menu and enter the following command:
```
pip install openpyxl
```

## openpyxl
```openpyxl``` is a library that allows you to read and write excel files. This can come in handy when an  file becomes too large to handle effectively in Excel. There is a BASIX.xlsx file in the [resources](https://github.com/tomvalorsa/python-course/tree/master/resources) folder which you can download to your working directory.

Start a new file in IDLE and save it in the same working directory as the excel file you just downloaded.

Some basic commands: (NOTE you will need to have pip-installed openpxyl as outlined above)  

To load the workbook and sheet (Save and run this file):
```
import openpyxl
wb = openpyxl.load_workbook('BASIX.xlsx')
sheet = wb.get_sheet_by_name('BASIX_Scores')
```
To find the sheet names in the workbook (in IDLE) - this will run for a while whilst the file is loaded into memory:
```
>>> wb.get_sheet_names()
['BASIX_Scores']
```
Now we know its name we can select the first sheet:
```
>>> sheet=wb.get_sheet_by_name('BASIX_Scores')
>>> sheet
<Worksheet "BASIX_Scores">
```
You can select an individual cell in this sheet by referencing it using traditional excel syntax:
```
>>> sheet.cell('A1').value
'Id'
```
Or by row-column notation (NOTE row=1 and column=1 not 0):
```
>>> sheet.cell(row=1, column=1).value
'Id'
```
You can loop through cells and print their values to the screen:
```
>>> for i in range(1,10):
	print(sheet.cell(row=i, column=1).value)
Id
32764
52739
175677
182825
199107
238415
14616
14663
>>> 
```
You can write a value or a formula into a cell:
```
sheet.cell(row=1, column=1).value = '=A2+A3/2'
```
You can create a workbook and save a workbook:
```
wb_2=openpyxl.Workbook()
wb_2.save('Workboook2.xlsx')
```

## Houston, we have a problem...

The NASA employee who was supposed to read the countdown for today's space shuttle launch has woken up with a sore throat.
You have offered to use your python skills to write a program that will count down the last 20 seconds before liftoff.

It is important that the countdown announce each stage of the launch as it occurs:

16 seconds: Launch pad sound suppression system activated  
10 seconds: Main engine hydrogen burnoff system activated  
7 seconds: Main engine start  
1 seconds: Solid booster ignition, booster-tower separation  
0 seconds: Exact time (HH:MM:SS DD/MM/YYYY) of liftoff

A sample output is shown below:

```
>>> countdown(20)
Countdown started, T-minus 20
... 19
... 18
... 17
... 16 Launch pad sound suppression system activated
... 15
... 14
... 13
... 12
... 11
... 10 Main engine hydrogen burnoff system activated
... 9
... 8
... 7 Main engine start
... 6
... 5
... 4
... 3
... 2
... 1 Solid booster ignition, booster-tower separation
... 0
... Liftoff at 10:31:29 19/08/2016
```

## BASIX BASICS

You have been asked to interrogate information found within a .xlsx file downloaded from the ABS website.
The file contains information regarding the BASIX projects registered in 2015-16, and contains too many rows of data to manage with Excel.

You have volunteered to use your python skills to create a new excel file with a more useable data set. The relevant information should be displayed in four columns:  

Local Government Authority (LGA) | # of projects | avg. energy score | avg. water score

Hint: you can find the maximum number of rows / columns using the following:
```
sheet.max_row
sheet.max_column
```

A small example BASIX_Results.xlsx file can be found in the [resources](https://github.com/tomvalorsa/python-course/tree/master/resources) folder.
