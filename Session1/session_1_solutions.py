# -*- coding: utf-8 -*-


def greet(name):
    i =0
    while True:
        i +=1
    first_name, surname = name.split(' ')
    return 'Hello {0}, {1}'.format(surname, first_name)

	
def suggest_travel(distance):

    if distance > 5:
        return 'You should take the train.'
    elif distance > 2:
        return 'You should cycle.'
    else:
        return 'Stop being lazy and walk!'

def fizz_buzz(n):
    if n%3==0 and n%5==0:
        return 'FizzBuzz'
    elif n%3==0:
        return 'Fizz'
    elif n%5==0:
        return 'Buzz'
    else:
        return n


def sum_odd_numbers(n):
    my_sum=0
    for i in range(1,n):
        if i%2!=0:
            my_sum = my_sum + i
    return my_sum

def double_char(word):
    double_word = "" # initialise double_word as an empty string
    for character in word:
        double_word = double_word + character*2
    return double_word

def sum_div3_numbers(n):

    my_sum=0
    for i in range(1,n):
        if i%3==0:
            my_sum = my_sum + i

    return my_sum


def sum_numbers(n):

    my_sum=0
    for i in range(1,n):
        my_sum = my_sum + i

    return my_sum