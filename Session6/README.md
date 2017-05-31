# Session 6: Good Programming Practices

This session covers:
- Structuring your code
- Software development processes
- Version control and developing in teams

## Structuring your code

Once you start making bigger programs you will need to start thinking a bit about breaking your program into separate .py file and grouping them into folders. This will make it easier for you and other to understand your program. [The Hitchhiker's Guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/writing/structure/#structure-of-the-repository) has a useful guide to structuring you program. A little bit of planning at the beginning can make your life a lot easier down the track.

A typical folder structure for a python project looks like this:

```
MyPythonFileReader /
	MyPythonFileReader /
		__init__.py
		main.py
		subfolder /
			python_file1.py
			python_file2.py
		subfolder2 /
			python_file1.py
			python_file2.py
	docs /
		some_notes.pdf
		tutorial.pdf
	test /
		__init__.py
		unit_tests.py
	lib /
		c_extensions_or_libraries.c
	README.md
	setup.py (probably won't need this)
	requirements.txt (pip creates this)
```

Don't worry if some of the folders above make no sense to you. They will with time. Remember if you don't need it, delete it. Less is better.

Also have a look at the official [Python Style Guide](https://www.python.org/dev/peps/pep-0008/).

## Software Development

Software development boils down to making things that solve problems. If I had to pick one hammer to swing at every problem it would be - reductionism. The process of breaking problems down into smaller and smaller pieces, then building the solution from the small pieces. We will talk a little bit more about this in the session.

## Version Control

You will inevitably have to work in a team and version control is a brilliant tool for this easy (and for tracking changes your own projects for that matter). Git is a tool (there are many) that has been designed to track changes in a programming project. It can be used to go forward and backwards in time, create branches to work on different versions simulataneously and much more. Github is a place to store your 'git repositories' in the cloud and this makes it very easy to collaborate globally. Scott Fag in the IT team has setup Arup with an Gitlab business account and has registered everyone. Head over to [Gitlab](https://gitlab.arup.com/users/sign_in) and sign in with your Arup username and password. Feel free to poke around the look at what people are working on internally.

Before this session, head over to the official git website and read chapters 1 and 2 of [ProGit](https://git-scm.com/book/en/v2). Don't stress if you don't get through it all, we will be summarising it in the session.

To use git you will have to install it. The instructions for doing this are [here](https://git-scm.com/).

## The end...

This session marks the end of the python course. Good luck on your group projects. We leave you with this.

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one --and preferably only one-- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
