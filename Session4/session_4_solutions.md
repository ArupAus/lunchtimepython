# Session 4: Working with Files
```py
import csv


def longest_line(file_path, split_char):
    line_number = 0
    num_words = -1

    with open(file_path, 'r') as input_file:
        for i, line in enumerate(input_file.readlines()):
            line = line.split(split_char)
            if len(line) >= num_words:
                num_words = len(line)
                line_number = i

    return {'line_number': line_number, 'num_words': num_words}


def longest_line_string(file_path, split_char):
    line_number = 0
    num_words = -1
    longest_string_length = -1

    with open(file_path, 'r') as input_file:
        for i, line in enumerate(input_file.readlines()):
            line = line.split(split_char)
            if len(line) >= num_words:
                if  max([len(x) for x in line]) >= longest_string_length:
                    longest_string_length = max([len(x) for x in line])
                    num_words = len(line)
                    line_number = i

    return {'line_number': line_number, 'num_words': num_words, 'longest_string_length':longest_string_length}


def biggest_debt(file_path):

    debt = -1
    job_number = -999888

    with open(file_path, 'rU') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            temp_job_no = int(row['Job Number'])
            temp_debt = float(row['Debt'])
            if temp_debt > debt:
                debt = temp_debt
                job_number = temp_job_no

    return {'job_number': job_number, 'debt': debt}


def total_debt(file_path):
    debt = 0
    with open(file_path, 'rU') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            debt += float(row['Debt'])

    return debt


def sorted_debts(file_path):
    debt_list = []
    with open(file_path, 'rU') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            debt_list.append({'job_number': int(row['Job Number']), 'debt': float(row['Debt'])})
    return sorted(debt_list, key=lambda k: k['debt'], reverse=True) 

```