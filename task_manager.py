#=====importing libraries===========
import time

MONTHS = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

#=====defining functions===========

def reg_user():
    # get new user, password and validate them 
    # before to insert values into the user.txt file
    # loop until check that username is available
    while True:
        is_free = True
        new_user = input("\nREGISTER A USER\n\nNew Username: ")
        # check if user already exist
        with open("user.txt", "r") as users:
            for line in users:
                if new_user == line.split(", ")[0]:
                    print("This username is already taken! Try again!")
                    is_free = False
                    break
        if is_free:
            break
    new_password = input("Enter the password: ")
    password_check = input("Re-enter the password: ")
    if new_password == password_check:
        # open the file and write inside
        with open("user.txt", "a") as accounts:
            accounts.write(f"\n{new_user}, {new_password}\n")
        print(f"\nUser '{new_user}' added succesfully!")
    else:
        # if the passwords don't match, print out a message
        print("\nThe passwords don't match! \nYou are going back to the main menu.")


def add_task():
    print("\nADD A NEW TASK\n")
    # get datas as user input
    user_of_task = input("What's the name of the user whom the task is assigned to? ")
    title_of_task = input("Enter the title of the task: ")
    description_of_task = input("Enter a description of the task: ")
    due_date_of_task = input("Enter the due date of the task (e.g. 01 Jan 2023): ")
    # retrieve the current day from time module
    today = time.strftime("%d %b %Y")
    # open file and add in it the task
    with open("tasks.txt", "a") as file:
        file.write(f"\n{user_of_task}, {title_of_task}, {description_of_task}, {today}, {due_date_of_task}, No")
    # print out the results
    print(f"""
Task succesfully added!

User: {user_of_task}
Title: {title_of_task}
Description: {description_of_task} 
Current date: {today}
Due Date: {due_date_of_task}            
            """)


def view_all():
    # open the file to read each task
    with open("tasks.txt", "r") as file:
        # display a break line
        print("____________________________________________________________________________")
        # loop inside each task, split it and read
        # the data to print it out
        for line in file:
            line_elements = line.split(", ")
            user = line_elements[0]
            title = line_elements[1]
            description = line_elements[2]
            starting_date = line_elements[3]
            due_date = line_elements[4]
            is_finish = line_elements[5]
            # display the results
            print(f"""\nTask: \t\t\t{title}
Assigned to: \t\t{user}
Date assigned: \t\t{starting_date}
Due date: \t\t{due_date}
Task Complete? \t\t{is_finish}
Task description:
 {description}
____________________________________________________________________________""")


def view_mine():
    # add a check if user has at least a task
    is_task = False
    # open the file to read each task
    with open("tasks.txt", "r") as file:
        # display a break line
        print("____________________________________________________________________________")
        # loop inside each task, split it and read
        # the data to print it out
        for count, line in enumerate(file, start=1):
            line_elements = line.split(", ")
            user = line_elements[0]
            if user == username:
                is_task = True
                title = line_elements[1]
                description = line_elements[2]
                starting_date = line_elements[3]
                due_date = line_elements[4]
                is_finish = line_elements[5]
                # display the results
                print(f"""\nTask number: \t\t{count}
Task: \t\t\t{title}
Assigned to: \t\t{user}
Date assigned: \t\t{starting_date}
Due date: \t\t{due_date}
Task Complete? \t\t{is_finish}
Task description:
 {description}
____________________________________________________________________________""")
    # if the user has no task, print it out
    if not is_task:
        print("\nYou have no task.\n")
    # if user has a task, let him pick one of it
    else:
        select_task = int(input("\nEnter the number of the task to pick it or '-1' to come back to the main menu: "))
        if select_task != -1:
            # open the file, read the lines and assign these to data variale
            with open("tasks.txt", "r+") as file:
                data = file.readlines()
                for count, line in enumerate(data, start=1):
                    if count == select_task:
                        picked_line = data[count-1].split(", ")
                        assigned_to = picked_line[0]
                        # check if the task is assigned to the username
                        if assigned_to == username:
                            # ask what user want to do
                            edit_choice = int(input("\nEnter '1' if you wanto to mark the task as completed or Enter '2' if you want to edit (only the uncompleted task): "))
                            if edit_choice == 1:
                                # remove previous data and insert the new
                                picked_line.pop(-1)
                                picked_line.append("Yes\n")
                                picked_line = ", ".join(picked_line)
                                data[count-1] = picked_line
                                file.seek(0)
                                for line in data:
                                    file.write(line)
                                print("\nEdit done succesfully!")
                                # check if the task isn't complete yet
                            elif edit_choice == 2 and picked_line[-1] != "Yes\n":
                                # ask the choice
                                what_to_edit = int(input("\nEnter '1' to edit the name of the user to whom the task is assigned or '2' to change de due date: "))
                                if what_to_edit == 1:
                                    # ask the new name
                                    modified_name = input(f"\nThe current task is assigned to {assigned_to}.\nEnter the name of the user you to whom assign the task: ")
                                    # remove previous data and insert the new
                                    picked_line.pop(0)
                                    picked_line.insert(0, modified_name)
                                    picked_line = ", ".join(picked_line)
                                    data[count-1] = picked_line
                                    file.seek(0)
                                    for line in data:
                                        file.write(line)
                                    print("\nEdit done succesfully!")

                                elif what_to_edit == 2:
                                    date_due = picked_line[-2]
                                    # ask the new deadline
                                    modified_date = input(f"\nThe current due date is {date_due}.\nEnter the new deadline (eg. 04 Jan 2023): ")
                                    # remove previous data and insert the new
                                    picked_line.pop(-2)
                                    picked_line.insert(-1, modified_date)
                                    picked_line = ", ".join(picked_line)
                                    data[count-1] = picked_line
                                    file.seek(0)
                                    for line in data:
                                        file.write(line)
                                    print("\nEdit done succesfully!")
                                    
                            else:
                                print("\nInvalid input.")
                        else:
                            print("\nInvalid input.")




#====Login Section====

# add a fancy logo :P
logo = '''

  _____         _      __  __                                   
 |_   _|_ _ ___| | __ |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
   | |/ _` / __| |/ / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
   | | (_| \__ \   <  | |  | | (_| | | | | (_| | (_| |  __/ |   
   |_|\__,_|___/_|\_\ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                |___/           

'''
print(logo)

# set a while loop until the inputs are right
while True:
    # get from user the username end password
    username = input("Username: ")
    # adding "\n" because of the file reading after
    # inserting a new user below
    ppw = input("Password: ")+"\n"

    # set this values as False for next verification
    permission = False
    is_username = False

    # check if the username and password are correct
    # by checking the document user.txt
    # if username and password are correct the user
    # will be allow to enter the panel and break the
    # while loop, otherwise they will be looped into
    # the verification.
    with open("user.txt") as accounts:
        for line in accounts:
            login = line.split(", ")
            if username == login[0] and ppw == login[1]:
                permission = True
                break
            elif username == login[0]:
                print("\nWrong password.\nTry Again\n")
                is_username = True
                break
    if permission:
        break
    elif not is_username:              
        print("\nNo username found.\nTry again.\n")

if permission:
    while True:
        # if the user is the admin, add a new option on menu
        # to display statistics and registration
        if username == "admin":
            menu = input('''\nSelect one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()
        # else, display normal menu
        else:
            menu = input('''\nSelect one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()
        # display only if you are the admin
        if menu == 'r' and username == "admin":
            reg_user()

        elif menu == 'a':
            add_task()


        elif menu == 'va':
            view_all()

        elif menu == 'vm':
            view_mine()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        # display only if you are the admin
        elif menu == 'ds' and username == "admin":
            #initialize the variables
            number_of_tasks = 0
            number_of_users = 0

            # get the number of tasks
            with open("tasks.txt", "r") as file:
                for count, line in enumerate(file, start=1):
                    number_of_tasks = count
            
            # get the number of users
            with open("user.txt", "r") as file:
                counter = 0
                for line in file:
                    if line != "\n":
                        counter += 1
                number_of_users = counter
            
            # display results
            print(f"\nSTATISTICS\n\nNumber of Tasks: \t{number_of_tasks}\nNumber of Users: \t{number_of_users}\n")

        # display only if you are the admin
        elif menu == 'gr' and username == "admin":
            #initialize the new file
            with open("task_overview.txt", "w") as to:
                # setup the variables
                how_many_tasks = 0
                completed_task = 0
                uncompleted_task = 0
                overdued = 0
                # open tasks.txt in reading mode
                with open("tasks.txt", "r") as file:
                    for count, line in enumerate(file, start=1):
                        # exclude the last empty line
                        if line != "\n":
                            data = line.split(", ")
                            # calculate the values
                            if data[-1] == "Yes\n":
                                completed_task += 1
                            else:
                                uncompleted_task += 1
                                # check current date vs due date thanks to months dictionary on top
                                # of this file
                                if time.strftime("%d %b %Y").split()[2] > data[-2].split()[2]:
                                    overdued += 1
                                elif time.strftime("%d %b %Y").split()[2] == data[-2].split()[2]:
                                    if MONTHS[time.strftime("%d %b %Y").split()[1]] > MONTHS[data[-2].split()[1]]:
                                        overdued += 1
                                    elif MONTHS[time.strftime("%d %b %Y").split()[1]] == MONTHS[data[-2].split()[1]]:
                                        if time.strftime("%d %b %Y").split()[0] > data[-2].split()[0]: 
                                            overdued += 1
                            
                    # write the file with the data
                to.write(f"""TASK OVERVIEW

Total number of Tasks: {count}
Task completed: {completed_task}
Task uncompleted: {uncompleted_task}
Task overdued: {overdued}
% of tasks uncompleted: {round((uncompleted_task/count)*100, 2)}%
% of tasks overdued: {round((overdued/count)*100, 2)}%""")
                    # print out the success
                print("\nTask Overview file generated!")

                        
            #initialize the new file
            with open("user_overview.txt", "w") as uo:
                # setup the variables
                how_many_tasks = 0
                how_many_users = 0
                task_per_user = ""
                # open tasks.txt in reading mode
                with open("tasks.txt", "r") as file:
                    for line in file:
                        if line != "\n":
                            how_many_tasks += 1  
                # open user in read mode                  
                with open("user.txt", "r") as file:
                    for line in file:
                        # exclude the last empty line
                        if line != "\n":
                            # setup the temporary variables for counting each user's data
                            how_many_users += 1
                            temp_num_task = 0
                            temp_completed = 0
                            temp_uncompleted = 0
                            temp_overdue = 0
                            data = line.split(", ")
                            with open("tasks.txt", "r") as task_file:
                                for line in task_file:
                                    if line != "\n":
                                        line_data = line.split(", ")
                                        if data[0] == line_data[0]:
                                            temp_num_task += 1
                                            if line_data[-1] == "Yes\n":
                                                temp_completed += 1
                                            else:
                                                temp_uncompleted += 1
                                                # check current date vs due date thanks to months dictionary on top
                                                # of this file
                                                if time.strftime("%d %b %Y").split()[2] > line_data[-2].split()[2]:
                                                    temp_overdue += 1
                                                elif time.strftime("%d %b %Y").split()[2] == line_data[-2].split()[2]:
                                                    if MONTHS[time.strftime("%d %b %Y").split()[1]] > MONTHS[line_data[-2].split()[1]]:
                                                        temp_overdue += 1
                                                    elif MONTHS[time.strftime("%d %b %Y").split()[1]] == MONTHS[line_data[-2].split()[1]]:
                                                        if time.strftime("%d %b %Y").split()[0] > line_data[-2].split()[0]: 
                                                            temp_overdue += 1
                                # add report depending on num_task of user
                                if temp_num_task == 0:
                                    task_per_user += f"""
{data[0].capitalize()}
\tTask assigned: {temp_num_task}
\t% of task on total: 0%
\t% of task completed: n.a.
\t% of task uncompleted: n.a.
\t% of task uncompleted and overdued: n.a.
"""
                                elif temp_uncompleted == 0:
                                    task_per_user += f"""
{data[0].capitalize()}
\tTask assigned: {temp_num_task}
\t% of task on total: {round((temp_num_task/how_many_tasks)*100, 2)}%
\t% of task completed: {round((temp_completed/temp_num_task)*100, 2)}%
\t% of task uncompleted: {round((temp_uncompleted/temp_num_task)*100, 2)}%
\t% of task uncompleted and overdued: 0%
"""
                                else:
                                    task_per_user += f"""
{data[0].capitalize()}
\tTask assigned: {temp_num_task}
\t% of task on total: {round((temp_num_task/how_many_tasks)*100, 2)}%
\t% of task completed: {round((temp_completed/temp_num_task)*100, 2)}%
\t% of task uncompleted: {round((temp_uncompleted/temp_num_task)*100, 2)}%
\t% of task uncompleted and overdued: {round((temp_overdue/temp_uncompleted)*100, 2)}%
"""
                        

                # write the file with the data
                uo.write(f"""USER OVERVIEW

Total number of users: {how_many_users}
Total number of tasks: {how_many_tasks}
{task_per_user}
""")
            # print out the success
            print("User Overview file generated!")     

        else:
            print("\nYou have made a wrong choice, Please Try again")
