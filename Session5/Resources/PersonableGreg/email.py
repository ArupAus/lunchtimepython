import random

# TO DO:
# 1. fix write_personal_email() so it greets/signs off properly 
# 2. read employees file and loop through calling write_personal_email() with details from Employees.csv


def write_personal_email(template, destination, first_name, last_name, age):

    hip_greetings = ['yo', 'hola', 'what up', 'whats crackin']
    hip_sign_offs = ['laters', 'cya', 'hasta luego', 'peace', 'ya boi'] # feel free to add more

    normal_greeting = 'Dear'
    normal_signoff = 'Regards'

    # open template html
    f = open(template, 'r+')

    # read all the lines in from the template email
    lines = f.readlines()
    f.close()

    # intialise a list to append lines to once 'personalised'
    personalised_message = []

    for line in lines:

        if '{{FIRST_NAME}}' in line:
            line = line.replace('{{FIRST_NAME}}', first_name)
        if '{{LAST_NAME}}' in line:
            line = line.replace('{{LAST_NAME}}', last_name)

        # TO DO: add more conditional statements to select random 
        # greeting and sign off from using random.choice(hip_greetings)
        # The tags to replace are {{GREETING}} and {{SIGN_OFF}}
        # remember only use hip greeting if age < 30

        personalised_message.append(line)


    # open a new file to personalised message
    f_out = open(destination + first_name + last_name + '.html', 'w')

    # loop through personal message and write to personal file
    for line in personalised_message:
        f_out.write(line+'\n')

    f_out.close()


write_personal_email('template.html','', 'Joe', 'Blogs', 25) # run like this to test function

# TO DO: read employee csv and loop through each line calling 

# f = open('Employees.csv', 'r+')

# read all the lines in from the template email
# lines = f.readlines()

# for line in lines:

    # TO DO: use line.split function to process data from Employees.csv and then call
    # write_personal_email(destination, firstname, lastname, age)
