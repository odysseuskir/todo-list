"""
Authors: Odysseus-Abraham Kirikopoulos
This script is protected by the GNU Public License 3.0. Refer source as "Odysseus-Abraham Kirikopoulos" when distributing the software.
Version: 1.7
"""

list_1 = {"task1": ["", "", "", "", "", ""], "task2": ["", "", "", "", "", ""], "task3": ["", "", "", "", "", ""], "task4": ["", "", "", "", "", ""],
          "task5": ["", "", "", "", "", ""]}  # Lists storing the tasks
list_1_name = None  # The list's name
list_2 = {"task1": ["", "", "", "", "", ""], "task2": ["", "", "", "", "", ""], "task3": ["", "", "", "", "", ""], "task4": ["", "", "", "", "", ""],
          "task5": ["", "", "", "", "", ""]}
list_2_name = None
list_3 = {"task1": ["", "", "", "", "", ""], "task2": ["", "", "", "", "", ""], "task3": ["", "", "", "", "", ""], "task4": ["", "", "", "", "", ""],
          "task5": ["", "", "", "", "", ""]}
list_3_name = None
operation_tree = None # The selected operation parent from the user (Example: Delete is the parent of delete a task or a list)
operation = None  # The selected operation from the user
list_chosen = None  # The selected list to complete an operation
task_chosen = None  # The selected task to complete an operation
subtask_chosen = 0  # The selected subtask to complete an operation


def refresh_pr_list():  # Refreshes the list of tasks

    global print_task_l1
    global print_task_l2
    global print_task_l3

    print_task_l1 = f"\nTask 1: {list_1['task1'][0]} | Priority: {list_1['task1'][4]} | Due date: {list_1['task1'][5]}\n -> {list_1['task1'][1]}\n -> {list_1['task1'][2]}\n -> {list_1['task1'][3]}\nTask 2: {list_1['task2'][0]} | Priority: {list_1['task2'][4]} | Due date: {list_1['task2'][5]}\n -> {list_1['task2'][1]}\n -> {list_1['task2'][2]}\n -> {list_1['task2'][3]}\nTask 3: {list_1['task3'][0]} | Priority: {list_1['task3'][4]} | Due date: {list_1['task3'][5]}\n -> {list_1['task3'][1]}\n -> {list_1['task3'][2]}\n -> {list_1['task3'][3]}\nTask 4: {list_1['task4'][0]} | Priority: {list_1['task4'][4]} | Due date: {list_1['task4'][5]}\n -> {list_1['task4'][1]}\n -> {list_1['task4'][2]}\n -> {list_1['task4'][3]}\nTask 5: {list_1['task5'][0]} | Priority: {list_1['task5'][4]} | Due date: {list_1['task5'][5]}\n -> {list_1['task5'][1]}\n -> {list_1['task5'][2]}\n -> {list_1['task5'][3]}\n"
    print_task_l2 = f"\nTask 1: {list_2['task1'][0]} | Priority: {list_2['task1'][4]} | Due date: {list_2['task1'][5]}\n -> {list_2['task1'][1]}\n -> {list_2['task1'][2]}\n -> {list_2['task1'][3]}\nTask 2: {list_2['task2'][0]} | Priority: {list_2['task2'][4]} | Due date: {list_2['task2'][5]}\n -> {list_2['task2'][1]}\n -> {list_2['task2'][2]}\n -> {list_2['task2'][3]}\nTask 3: {list_2['task3'][0]} | Priority: {list_2['task3'][4]} | Due date: {list_2['task3'][5]}\n -> {list_2['task3'][1]}\n -> {list_2['task3'][2]}\n -> {list_2['task3'][3]}\nTask 4: {list_2['task4'][0]} | Priority: {list_2['task4'][4]} | Due date: {list_2['task4'][5]}\n -> {list_2['task4'][1]}\n -> {list_2['task4'][2]}\n -> {list_2['task4'][3]}\nTask 5: {list_2['task5'][0]} | Priority: {list_2['task5'][4]} | Due date: {list_2['task5'][5]}\n -> {list_2['task5'][1]}\n -> {list_2['task5'][2]}\n -> {list_2['task5'][3]}\n"
    print_task_l3 = f"\nTask 1: {list_3['task1'][0]} | Priority: {list_3['task1'][4]} | Due date: {list_3['task1'][5]}\n -> {list_3['task1'][1]}\n -> {list_3['task1'][2]}\n -> {list_3['task1'][3]}\nTask 2: {list_3['task2'][0]} | Priority: {list_3['task2'][4]} | Due date: {list_3['task2'][5]}\n -> {list_3['task2'][1]}\n -> {list_3['task2'][2]}\n -> {list_3['task2'][3]}\nTask 3: {list_3['task3'][0]} | Priority: {list_3['task3'][4]} | Due date: {list_3['task3'][5]}\n -> {list_3['task3'][1]}\n -> {list_3['task3'][2]}\n -> {list_3['task3'][3]}\nTask 4: {list_3['task4'][0]} | Priority: {list_3['task4'][4]} | Due date: {list_3['task4'][5]}\n -> {list_3['task4'][1]}\n -> {list_3['task4'][2]}\n -> {list_3['task4'][3]}\nTask 5: {list_3['task5'][0]} | Priority: {list_3['task5'][4]} | Due date: {list_3['task5'][5]}\n -> {list_3['task5'][1]}\n -> {list_3['task5'][2]}\n -> {list_3['task5'][3]}\n"


def list_select():  # Allows the user to select a list

    global list_chosen

    list_chosen = str(input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n"))

    if list_chosen == list_1_name:
        list_chosen = list_1

    elif list_chosen == list_2_name:
        list_chosen = list_2

    elif list_chosen == list_3_name:
        list_chosen = list_3

    else:
        print("Err:ListNotFound")


def task_select():  # Allows the user to select a task

    global task_chosen

    list_select()

    if list_chosen == list_1:

        task_chosen = input(f"\nSelect a task: {print_task_l1}\n")

    elif list_chosen == list_2:

        task_chosen = input(f"\nSelect a task: {print_task_l2}\n")

    elif list_chosen == list_3:

        task_chosen = input(f"\nSelect a task: {print_task_l3}\n")

    else:
        print("Err:ListNotFound")


def subtask_select(): # Allows the user to select a subtask

    global subtask_chosen

    task_select()

    subtask_chosen = input(f"\nSelect a subtask:\n")

    subtask_chosen = int(subtask_chosen)


# Startup
print("To-Do List GNU General Public License 3.0 2022 Odysseus-Abraham Kirikopoulos\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it under certain conditions.")  # Prints the GNU Public License 3.0
print("Build Version: 1.7\n\n")  # Prints the build version

# Greet
print("~~~ MY TO-DO LIST ~~~")

# Operations
while True:  # Infinite loop

    operation_tree = input("\nSelect the type of operation:\n(1) Create\n(2) Delete/Check off\n(3) Edit\n(4) View\nTo exit press 0\n\n")  # Asks the user to select an operation

    if operation_tree == "0":  # User exiting
        break

    elif operation_tree == "1":  # User creating a list or a (sub)task
        operation = input("\n -> (1) Create a list\n -> (2) Create a task\n -> (3) Create a subtask\n\n")

        # Create a new list
        if operation == "1":

            if list_1_name == None:  # Checking which list is not occupied in order to create a list

                list_1_name = input("\nName your new list: ")
                print(f"{list_1_name} created")

            elif list_2_name == None:

                list_2_name = input("\nName your new list: ")
                print(f"{list_2_name} created")

            elif list_3_name == None:

                list_3_name = input("\nName your new list: ")
                print(f"{list_3_name} created")

            elif (list_1_name and list_2_name and list_3_name != None):  # In case there are 3 lists, no more can be created

                print("Err:MaxListsReached")

            refresh_pr_list()

        # Create a new task
        elif operation == "2":

            list_select()

            if list_chosen["task1"][0] == "":  # Checking a non-occupied task to create the new one

                list_chosen["task1"][0] = input("\nEnter your task: ")
                print("\nTask created successfully!\n")

                list_chosen["task1"][4] = input("Enter the priority of the task (1-3): ")
                list_chosen["task1"][5] = input("Enter the due date for the task (DD/MM/YYYY): ")

            elif list_chosen["task2"][0] == "":

                list_chosen["task2"][0] = input("\nEnter your task: ")
                print("\nTask created successfully!\n")

                list_chosen["task2"][4] = input("Enter the priority of the task (1-3): ")
                list_chosen["task2"][5] = input("Enter the due date for the task (DD/MM/YYYY): ")

            elif list_chosen["task3"][0] == "":

                list_chosen["task3"][0] = input("\nEnter your task: ")
                print("\nTask created successfully!\n")

                list_chosen["task3"][4] = input("Enter the priority of the task (1-3): ")
                list_chosen["task3"][5] = input("Enter the due date for the task (DD/MM/YYYY): ")

            elif list_chosen["task4"][0] == "":

                list_chosen["task4"][0] = input("\nEnter your task: ")
                print("\nTask created successfully!\n")

                list_chosen["task4"][4] = input("Enter the priority of the task (1-3): ")
                list_chosen["task4"][5] = input("Enter the due date for the task (DD/MM/YYYY): ")

            elif list_chosen["task5"][0] == "":

                list_chosen["task5"][0] = input("\nEnter your task: ")
                print("\nTask created successfully!\n")

                list_chosen["task5"][4] = input("Enter the priority of the task (1-3): ")
                list_chosen["task5"][5] = input("Enter the due date for the task (DD/MM/YYYY): ")

            else:

                print("\nErr:MaxTasksReached")  # In case there are 5 tasks, no more can be created

            refresh_pr_list()

        # Create a subtask
        elif operation == "3":

            task_select()

            if list_chosen[task_chosen][1] == "":  # Checking non-occupied subtask to create the new one

                list_chosen[task_chosen][1] = input("\nEnter your task: ")
                print("\nSubtask created successfully!")

            elif list_chosen[task_chosen][2] == "":

                list_chosen[task_chosen][2] = input("\nEnter your task: ")
                print("\nSubtask created successfully!")

            elif list_chosen[task_chosen][3] == "":

                list_chosen[task_chosen][3] = input("\nEnter your task: ")
                print("\nSubtask created successfully!")

            else:  # In case there are 3 subtasks, no more can be created

                print("\nErr:MaxSubtasksReached")

            refresh_pr_list()

    if operation_tree == "2":  # User deleting/checking off a list or a (sub)task

        operation = input("\n -> (1) Check off a task\n -> (2) Check off a subtask\n -> (3) Delete a list\n -> (4) Delete a task\n\n")

        # Check off a task
        if operation == "1":
            task_select()

            list_chosen[task_chosen][0] += " [Done]"  # Adding "[Done]" to the end of the selected task
            print("Task checked off successfully!")

            refresh_pr_list()

        # Check off a subtask
        if operation == "2":
            subtask_select()

            list_chosen[task_chosen][subtask_chosen] += " [Done]"  # Adding "[Done]" to the end of the selected subtask
            print("Subtask checked off successfully!")

            refresh_pr_list()

        # Delete a list
        if operation == "3":

            list_select()

            if list_chosen == list_1:

                list_1_name = list_2_name  # Moving the name of the second list to the first one
                list_2_name = list_3_name  # Moving the name of the third list to the second one
                list_3_name = None  # Setting the name of the third list to None
                list_1 = list_2  # Moving the second list to the first one
                list_2 = list_3  # Moving the third list to the second one
                list_3 = {"task1": ["", "", "", "", "", ""], "task2": ["", "", "", "", "", ""], "task3": ["", "", "", "", "", ""], "task4": ["", "", "", "", "", ""],
                "task5": ["", "", "", "", "", ""]}
                print("List deleted successfully!")

            elif list_chosen == list_2:

                list_2_name = list_3_name
                list_3_name = None
                list_2 = list_3
                list_3 = {"task1": ["", "", "", "", "", ""], "task2": ["", "", "", "", "", ""], "task3": ["", "", "", "", "", ""], "task4": ["", "", "", "", "", ""],
                "task5": ["", "", "", "", "", ""]}
                print("List deleted successfully!")

            elif list_chosen == list_3:

                list_3_name = None
                list_3 = {"task1": ["", "", "", "", "", ""], "task2": ["", "", "", "", "", ""], "task3": ["", "", "", "", "", ""], "task4": ["", "", "", "", "", ""],
                "task5": ["", "", "", "", "", ""]}
                print("List deleted successfully!")

            else:

                print("Err:ListNotFound")

            refresh_pr_list()

        # Delete a task
        if operation == "4":
            task_select()

            list_chosen[task_chosen][0] = ""  # Setting a task blank
            list_chosen[task_chosen][1] = ""
            list_chosen[task_chosen][2] = ""
            list_chosen[task_chosen][3] = ""

            refresh_pr_list()

    if operation_tree == "3":  # User editing a list or a task

        operation = input("\n -> (1) Rename a list\n -> (2) Rename a task\n -> (3) Edit a task's priority\n\n")

        # Rename a list
        if operation == "1":

            list_select()

            if list_chosen == list_1:  # Renaming the list
                list_1_name = input(f"\nRename the list (previous name: {list_1_name}):\n")
                print("Renamed the list successfully!")

            elif list_chosen == list_2:
                list_2_name = input(f"\nRename the list (previous name: {list_2_name}):\n")
                print("Renamed the list successfully!")

            elif list_chosen == list_3:
                list_3_name = input(f"\nRename the list (previous name: {list_3_name}):\n")
                print("Renamed the list successfully!")

            else:
                print("\nErr:ListNotFound")

            refresh_pr_list()

        # Rename a task
        if operation == "2":
            task_select()

            list_chosen[task_chosen][0] = input(f"Rename the task: ")  # Renaming the task
            print("Renamed the task successfully!")

            refresh_pr_list()

        # Add priority to a task
        if operation == "3":

            task_select()

            list_chosen[task_chosen][4] = input("Edit the priority of the task (1-3): ") # Adding priority to the task

            refresh_pr_list()

            print("\nEdited priority to the task successfully!")

    if operation_tree == "4":  # User viewing a list

        list_select()

        if list_chosen == list_1:  # Printing the list selected
            print(print_task_l1)

        elif list_chosen == list_2:
            print(print_task_l2)

        elif list_chosen == list_3:
            print(print_task_l3)

        else:
            print("Err:ListNotFound")

exit_key = input()  # Exiting the program

# This program is protected by the GNU General Public License v3.0 | ODYSSEUS-ABRAHAM KIRIKOPOULOS | SOME RIGHTS RESERVED
