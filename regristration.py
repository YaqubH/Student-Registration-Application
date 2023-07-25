"""
    Title: registration.py
    Author: Yaqub Hasan
    Date: 5/18/23
"""

# ! /usr/bin/env python3
from data_utils import read_file_one, read_file_two, read_file_three, write_file_one, write_file_two
from datetime import datetime


def add(ids, student_data):
    counter = 0  # initialize counter to zero

    # Get student last name
    last_name = input("Enter Student's Last Name: ")

    # Check student last name for numbers or spaces
    while not last_name.isalpha():
        print("Invalid last name. Please enter a name without spaces or numbers.\n")
        last_name = input("Enter Student's Last Name: ")

    # Get student first name
    first_name = input("Enter Student's First Name: ")

    # Check student first name for numbers or spaces
    while not first_name.isalpha():
        print("Invalid first name. Please enter a name without spaces or numbers.\n")
        first_name = input("Enter Student's First Name: ")

    # Create a unique ID for the student
    stu_id = f"{first_name[0].lower()}{last_name.lower()}"
    student_id = stu_id + "0"
    while student_id in ids:
        counter += 1
        student_id = stu_id + str(counter)

    # Append new student to student_data
    new_student = (student_id, last_name, first_name)
    student_data.append(new_student)

    # Write new student to the students file
    write_file_one(student_data)

    print(f"Student {student_id} hs been added.\n")

    # return the students id as well as their first and last names for later use
    return student_id, first_name, last_name


def display_menu(first_name):
    # Get the exact time
    right_now = datetime.now()

    # Format the time
    current_time = right_now.strftime("%I:%M:%S %p")

    # Use if statement to check what greeting to output
    if "12:00AM" <= current_time <= "11:59AM":
        greeting = "Good morning"
    elif "12:00PM" <= current_time <= "4:59PM":
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    # Output the greeting as well as the users first name and the menu
    print(f"{greeting} {first_name}, what would you like to do today?\n")
    print("info     - Student information")
    print("list     - Course listing")
    print("detail   - Course detail")
    print("register - Register for a class")
    print("drop     - Drop class")
    print("menu     - Menu")
    print("exit     - End session")
    print()

    # Get the students choice and return it
    selection_choice = input("Enter selection: ")
    return selection_choice


def info(student_id, first_name, last_name, registration_data, course_data):
    units = 0  # initialize the units variable to zero
    print(f"\nStudent ID: {student_id}\n{last_name}, {first_name}")
    registered_courses = []  # initialize the registered_courses
    for reg in registration_data:
        # Check to see if student_id match
        if reg[0] == student_id:
            # Iterate through course_data
            for course in course_data:
                # Check to see registration code match
                if course[0] == reg[1]:
                    registered_courses.append(course)
                    # add up the units
                    units += float(course[3])
                    break

    # Output the registered courses
    if registered_courses:
        print("Registered Courses")
        print(f"{'Ticket':15} {'Code':15} {'Course Name':45} {'Units':10} {'Day':10} {'Time':20} {'Instructor':15}")
        print("=" * 140)

        # Iterates through all the registered courses for the student and output the information
        for ticket, code, name, unit, day, time, instructor in registered_courses:
            print(f"{ticket:15} {code:15} {name:45} {unit:10} {day:10} {time:20} {instructor:15}")

        # Output the total number of courses and units the student is taking
        print(f"{len(registered_courses)} Course(s) Registered \t\t\t\t\t\t\t\t\t\t\t\t   Units: {units}")
    else:
        print("\nNo registered courses found for the student.")


def course_list(course_data):
    # Get the student input on how they would like to sort the information
    listing_choice = input("\nList by Course Ticket or Course Code? (t/c): ")

    # If user selects "t" then sort by course ticket
    if listing_choice.lower() == "t":
        print("\nCourse Listing by Ticket")
        print(f"{'Ticket':15} {'Code':15} {'Course Name':45} {'Units':10} {'Day':10} {'Time':20} {'Instructor':15}")
        print("=" * 140)

        # Sort by course ticket
        course_data.sort(key=lambda x: x[0])

        # Iterate through course_data and then print
        for ticket, code, name, unit, day, time, instructor in course_data:
            if day.lower() == "online":
                time = ""
            print(f"{ticket:15} {code:15} {name:45} {unit:10} {day:10} {time:20} {instructor:15}")

    # Else if user selects "c" then sort by course code
    elif listing_choice.lower() == "c":
        print("\nCourse Listing by Code")
        print(f"{'Code':15} {'Ticket':25} {'Course Name':45} {'Units':10} {'Day':10} {'Time':20} {'Instructor':15}")
        print("=" * 140)

        # Sort by course code
        course_data.sort(key=lambda x: x[1])

        # Iterate through course_data and then print
        for code, ticket, name, unit, day, time, instructor in course_data:
            if day.lower() == "online":
                time = ""
            print(f"{code:15} {ticket:25} {name:45} {unit:10} {day:10} {time:20} {instructor:15}")

    else:
        print("Invalid choice. Please try again.\n")

    print("=" * 140)

    # Output the total number of courses
    print(f"{len(course_data)} Courses")


def detail(student_data, registration_data, course_data):
    # Set the variables for later use
    ids = [row[0] for row in student_data]
    last_names = [row[1] for row in student_data]
    first_names = [row[2] for row in student_data]

    # Get the course ticket number the student wishes to view
    ticket_num = input("\nEnter course ticket # (or exit): ")
    while ticket_num != "exit":

        f_courses = []  # initialize the f_courses
        # Find the course with the given ticket number
        for course in course_data:
            # If found append to f_courses
            if course[0] == ticket_num:
                f_courses.append(course)

        # Print out and format the information
        if f_courses:
            print(f"Code: {f_courses[0][1]} Course Name: {f_courses[0][2]}")
            print(f"Unit: {f_courses[0][3]} Day: {f_courses[0][4]} Time: {f_courses[0][5]}")
            print(f"Instructor: {f_courses[0][6]}")
            print("========================================================================")

            code_names = []  # initialize the code_names
            # Find the registration entries for the course
            for reg in registration_data:
                # If found append to code_names
                if reg[1] == ticket_num:
                    code_names.append(reg[0])

            # Iterates through code_names
            for reg in code_names:
                # If found return the exact index then set the variables and then print
                if reg in ids:
                    index = ids.index(reg)
                    student_id = ids[index]
                    first_name = first_names[index]
                    last_name = last_names[index]
                    print(f"{student_id:15} {first_name:15} {last_name:15}")

            # Print out the total number of students registered to this course
            print(f"Total Students Registered: {len(code_names)}")
            return
        elif ticket_num == "exit":
            print("\nSession ended.")
        else:
            print(f"{ticket_num} is an invalid ticket number. Please try again.")

        ticket_num = input("\nEnter course ticket # (or exit): ")


def register(student_id, registration_data, course_data):
    registered_courses = []  # initialize registered_courses
    # Iterates through registration_data
    for reg in registration_data:
        # If an ID match occurs append the course ticket number to registered_courses
        if reg[0] == student_id:
            registered_courses.append(reg[1])

    registered_units = 0  # initialize registered_units
    # Iterates through course_data
    for course in course_data:
        # If course is in registered_courses add the course units to registered_units
        if course[0] in registered_courses:
            registered_units += float(course[3])

    # Get the course ticket number the student wishes to register for
    ticket_num = input("\nEnter ticket # or 'exit': ")

    while ticket_num != 'exit':
        # If ticket_num in registered_courses then print out that this student is already in the course
        if ticket_num in registered_courses:
            print(f"{student_id} is already registered for this course.")
            return
        else:
            course = 0  # initialize course
            # Iterate through course_data
            for cou in course_data:
                # If a ticket match is found put it in course
                if cou[0] == ticket_num:
                    course = cou
                    break
            if course == 0:
                # If no course was found (course is still 0) print out invalid ticket number
                print(f"{ticket_num} is an invalid ticket number. Please try again.")
                ticket_num = input("Enter ticket # or 'exit': ")
            else:
                # But if ticket is found then check if the student exceeds their maximum units allowed
                course_units = float(course[3])
                if registered_units + course_units > 12:
                    print("This would exceed your maximum units allowed.")
                    return
                else:
                    # if they are not then append this student to registration_data
                    # and print that they were ad to the class
                    registration_data.append((student_id, ticket_num))
                    # Write to the registration file
                    write_file_two(registration_data)
                    print(f"{student_id} was added to {ticket_num}")
                    return


def drop(student_id, registration_data):
    # Get the course ticket number the student wishes to drop
    ticket_num = input("\nEnter ticket # or 'exit': ")
    while ticket_num != 'exit':
        # Iterate through registration_data
        for i in range(len(registration_data)):
            # Checks if the current registration_data entry matches the ticket_num and student_id
            if registration_data[i][1] == ticket_num and registration_data[i][0] == student_id:
                # If it does then the program will delete at that index
                registration_data.pop(i)
                # write to the registration file
                write_file_two(registration_data)
                # It will then output this print message before exiting the function
                print(f"{student_id} was dropped from {ticket_num}.")
                return
        else:
            print(f"{ticket_num} was an invalid ticket number or you are not registered in this course. "
                  f"Please try again.")
            ticket_num = input("Enter ticket # or 'exit': ")


def menu():
    # When this function is called it will just display the menu
    print()
    print("info     - Student information")
    print("list     - Course listing")
    print("detail   - Course detail")
    print("register - Register for a class")
    print("drop     - Drop class")
    print("menu     - Menu")
    print("exit     - End session")


def main():
    # Read in the files using functions in data_utils
    student_data = read_file_one()
    registration_data = read_file_two()
    course_data = read_file_three()

    # Set the student information for later use
    ids = [row[0] for row in student_data]
    last_names = [row[1] for row in student_data]
    first_names = [row[2] for row in student_data]

    # Print program name
    print("Saddleback College Registration\n")

    # Prompt the student to either log in, register as a new student, or exit the program
    choice = input("Enter a Student ID (or 'add' to add a new student, or 'exit' to exit the application): ")
    print()
    while choice.lower() != "exit":
        # if their ID is in the id list then get their first and last name
        if choice in ids:
            index = ids.index(choice)
            student_id = ids[index]
            first_name = first_names[index]
            last_name = last_names[index]

            # Output the display_menu and return their selection choice
            selection_choice = display_menu(first_name)
        # If the student was to register as a student then send them to the add function
        elif choice == "add":
            # After the add function return their student ID as well as their full name for later use
            student_id, first_name, last_name = add(ids, student_data)
            # Then output the display_menu and return their selection choice
            selection_choice = display_menu(first_name)
        else:
            print("Student id not found, please try again\n")
            choice = input("Enter a Student ID (or 'add' to add a new student, or 'exit' to exit the application): ")
            print()
            continue

        # Depending on their selection_choice send them to required function
        while True:
            if selection_choice.lower() == "info":
                info(student_id, first_name, last_name, registration_data, course_data)
            elif selection_choice.lower() == "list":
                course_list(course_data)
            elif selection_choice.lower() == "detail":
                detail(student_data, registration_data, course_data)
            elif selection_choice.lower() == "register":
                register(student_id, registration_data, course_data)
            elif selection_choice.lower() == "drop":
                drop(student_id, registration_data)
            elif selection_choice.lower() == "menu":
                menu()
            elif selection_choice.lower() == "exit":
                print("Session ended.")
                return
            else:
                print("Invalid selection, please try again")

            selection_choice = input("\nEnter selection: ")

    print("Session ended.")


if __name__ == "__main__":
    main()
