# Session 0: Getting Set up (Pre-Work)

As part of the pre work you have installed python and a text editor. You have also watched two videos from automate the boring stuff. In the videos you learned:
- Expressions and Statements
- Integers, floats and strings
- Variables

If you havent done this yet please go to the top of screen and click on __Get set up__ to 


Aim of this problem set is to gently introduce you to the python interpreter and make sure everything is working.

Go to your start menu and select the program `IDLE (Python 3.6 64-bit)` inside the `Python 3.6` folder. This will load up the interpreter. Use this to explore the problems below.

## Python as a calculator
To use python as a calculator, simply type in the expression and press enter.

```
>>> (34/4.5)*3+4
26.666666666666664
```

What would the expression `(34/4.5)*(3+4)` evaluate to?

## Division
What is 17 divided by 3?
How many times does 3 divide into 17?
*HINT:* What is the diference between `17/3` and `17//3`?

## Working with strings

A string is a group of characters (Examples of characters: `'a'`, `'b'`, `'X'`, `'$'` or `'5'`). You string the characters together to create a string: `'abX$5'`

You can add strings together.
```py
my_string = 'I have eaten ' + '99' + ' burritos.'
```

You cannot add strings and other types together. Try it in the interpreter.
```py
my_string = 'I have eaten ' + 99 + ' burritos.'
```

How can you fix this?


## A little theory
It is useful to distinguish between values and operators that act on values. Which of the following are operators and which are values?

```py
*
'hello'
-88.8
-
/
+
5
```

## Computers love arithmetic
Write a short program that prompts the user for two numbers, multiplies the numbers together and prints the result to the console (do this in the console for now, we will show you how to write scripts in session 1).

To print something to the screen:
```
>>> my_number = 55
>>> print(my_number)
55
```

To prompt the user to enter a number:
```py
# To prompt the user to enter a value
>>> my_string = input("Message to the user")
```


## Hello World -Submitting your solutions for marking 
No programming course should deprive you of a hello world so sticking with tradition we will require you to create a hello world program.
This excerise is to show you how to submit solutions to this website for marking. We this example will be using Microsoft VS code which is cross platform for people with mac or *nix machines.


below is what we call a function, similar to how you might use the sum function in excel `=SUM(A1:A3)` which accepts a range as the input argument. However in this case we are writing the implementation for a function called hello_world which accepts no arguments and returns `hello world!` when called. If this doesn't make sense don't worry we will cover this in more depth in future sessions.

What is import is when you submit you solutions to this website they will be in the form of a function. Be careful to submit files with the function name as specified in the question otherwise it will not mark your work.

```py

def hello_world():
    return 'hello world!'

```

Copy code above into a new file in VS Code __Do not change the name of the function from__ `hello_world`
![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SubmittingSolutions/00paste.PNG)

Save your file as  `.py`  in a folder somewhere appropriate. In this case I have put it in a folder names lunchtime on my desktop
![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SubmittingSolutions/01saveas.PNG)

VS Code has an explorer useful for managing your files and will start a terminal to execute your code from the folder you specify. Click on the 2 pages icon on the top left and open folder. Point it towards your lunchtime folder and hit ok.
![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SubmittingSolutions/03opnfolder.PNG)

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SubmittingSolutions/03zOpenFolder.PNG)

Now we will open a terminal to run your hello world program. you can shortcut by pressing ``crtl + ` `` or going to ` view > Integrated Terminal `
![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SubmittingSolutions/04openTerminal.png)
On windows a powershell console will show up. If on a mac bash, either way you should be able to run your program by typing `python hello_world.py`. This is telling your computer to get python to run your code. If the terminal complains that it doesn't have a command `python` your environment variables haven't been set yet. Please go back to the Get Set up page and make sure when you install python you click add python to PATH in `Step 4: Install Python` or ask a tutor in the first session to help you.

If python cant find your file you are not in the correct directory. You can type `ls` to list all files and directories in your current location and navigate by typing `cd ..` to go up a directory, `cd directory_name` to go into a directory. 
Getting comfortable with the terminal is an important skill when programming, don't worry with these commands you can't break anything. :)

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SubmittingSolutions/05nothinghappens.PNG)

Add the following lines to you code to get it to print the output of your `hello_world()` function. Note we are using the built in function `print()` which comes as part of the python standard library in order to see the value the `hello_world()` function returns.

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SubmittingSolutions/06print.png)


Now if you go over to the submission panel on the left of screen you will see a submit panel appear under Session 0, you can drag and drop you file on the choose file or select with explorer by hitting choose. Once you file is selected hit submit 

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SubmittingSolutions/07__submit.PNG)

After that you will see a modal appear and you result will update in the submission panel
![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SubmittingSolutions/07_modal.png)
![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SubmittingSolutions/07mark.PNG)

And thats it, well done submitting you customary hello world program.

## Congratulations
 You have now successfully submitted the pre - work! Rest up for now we will see you in session 1!