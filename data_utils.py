"""
    Title: data_utils.py
    Author: Yaqub Hasan
    Date: 5/18/23
"""

import csv

# Name the files for easier use
FILEONE = "students.csv"
FILETWO = "registration.csv"
FILETHREE = "courses.csv"


# Read in information from students.csv
def read_file_one():
    student_data = []  # initialize the student_data
    with open(FILEONE, newline="") as file_one:
        reader = csv.reader(file_one)
        for row in reader:
            student_data.append(row)
    # Return student_data for future use
    return student_data


# Read in information from registration.csv
def read_file_two():
    registration_data = []  # initialize the registration_data
    with open(FILETWO, newline="") as file_two:
        reader = csv.reader(file_two)
        for row in reader:
            registration_data.append(row)
    # Return registration_data for future use
    return registration_data


# Read in information from courses.csv
def read_file_three():
    course_data = []  # initialize the course_data
    with open(FILETHREE, newline="") as file_three:
        reader = csv.reader(file_three)
        for row in reader:
            course_data.append(row)
    # Return course_data for future use
    return course_data


# Write information to students.csv
def write_file_one(student_data):
    with open(FILEONE, "w", newline="") as file_one:
        writer = csv.writer(file_one)
        writer.writerows(student_data)


# Write information to registration.csv
def write_file_two(registration_data):
    with open(FILETWO, "w", newline="") as file_two:
        writer = csv.writer(file_two)
        writer.writerows(registration_data)
