# Session 7 Problems

In session 7 we learnt about the following:

1. Formatting your code
2. Useful comments
3. DRY principle/refactoring code


# Scrabble

Write a program that asks a user for a word and gives you back its [Scrabble](https://en.wikipedia.org/wiki/Scrabble) score. For now, pretend the user is your friend and they don't want to break your program - this means you can assume they have only entered one word and it's actually a real word.

e.g.

```
'Penguin' -> 10
'Zebra' -> 16
```

Remember, solving a problem (programming and personal) is easier when you break it down into smaller chunks:

- ask the user for a word to test
- find a way to store the score for each letter
- find the score for each letter in the user's word using your score reference above

Teacher's Pet Edition:

Once you've completed the above, change your program to make sure that the user is only entering one word. When printing out the score, rate the user's word and give them feedback. For example if the score is less than 5 you could print 'Try harder'. Feel free do decide on your own rating system.

e.g.

```
'Another animal' -> 'One word at a time, cheater.'
'Cat' ->
  C - 3
  A - 1
  T - 1
  Rating: Try harder!
```

# Overtime

Nobody got paid for any overtime this month, so you volunteer to figure out how much each person is owed in a bid to secure some early nominations for next year's Oves. Go you. Using data from `overtime.csv` calculate how much each employee is owed, assuming that everyone gets paid $50 per hour of overtime worked, and write this info to a separate csv:

Example Output:

|Employee|Money owed|
|-----|------|
|Tom|200|
|Patrick|350|
|Ian|400|
|Other Tom|200|
|Alex|50|


# Useful Links/Further Reading

- [Try Git](https://try.github.io/levels/1/challenges/1)
- [Pep8 Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Pep8 Code Checker](http://pep8online.com/)
