'''
Authors: Odysseus-Abraham Kirikopoulos
This script is protected by the GNU Public License 3.0. Refer source as "Odysseus-Abraham Kirikopoulos" when distributing the software.
Version: 1.6.1 Prebuild 5
WARNING: The following program was created for educational purposes only
'''

list_1 = {"task1": ["", "", "", ""], "task2": ["", "", "", ""], "task3": ["", "", "", ""], "task4": ["", "", "", ""], "task5": ["", "", "", ""]} #Lists storing the tasks
list_1_name = "Not defined" #The list's name
list_2 = {"task1": ["", "", "", ""], "task2": ["", "", "", ""], "task3": ["", "", "", ""], "task4": ["", "", "", ""], "task5": ["", "", "", ""]}
list_2_name = "Not defined"
list_3 = {"task1": ["", "", "", ""], "task2": ["", "", "", ""], "task3": ["", "", "", ""], "task4": ["", "", "", ""], "task5": ["", "", "", ""]}
list_3_name = "Not defined"
operation_tree = "Not defined" #The selected operation parent from the user (Example: Delete is the parent of delete a task or a list)
operation = "Not defined" #The selected operation from the user
list_chosen = "Not defined" #The selected list to complete an operation
task_chosen = "Not defined" #The selected task to complete an operation
subtask_chosen = 0 #The selected subtask to complete an operation

def refresh_pr_list(): #Refreshes the list of tasks

	global print_task_l1
	global print_task_l2
	global print_task_l3

	print_task_l1 = f"\nTask 1: {list_1['task1'][0]}\n -> {list_1['task1'][1]}\n -> {list_1['task1'][2]}\n -> {list_1['task1'][3]}\nTask 2: {list_1['task2'][0]}\n -> {list_1['task2'][1]}\n -> {list_1['task2'][2]}\n -> {list_1['task2'][3]}\nTask 3: {list_1['task3'][0]}\n -> {list_1['task3'][1]}\n -> {list_1['task3'][2]}\n -> {list_1['task3'][3]}\nTask 4: {list_1['task4'][0]}\n -> {list_1['task4'][1]}\n -> {list_1['task4'][2]}\n -> {list_1['task4'][3]}\nTask 5: {list_1['task5'][0]}\n -> {list_1['task5'][1]}\n -> {list_1['task5'][2]}\n -> {list_1['task5'][3]}\n"
	print_task_l2 = f"\nTask 1: {list_2['task1'][0]}\n -> {list_2['task1'][1]}\n -> {list_2['task1'][2]}\n -> {list_2['task1'][3]}\nTask 2: {list_2['task2'][0]}\n -> {list_2['task2'][1]}\n -> {list_2['task2'][2]}\n -> {list_2['task2'][3]}\nTask 3: {list_2['task3'][0]}\n -> {list_2['task3'][1]}\n -> {list_2['task3'][2]}\n -> {list_2['task3'][3]}\nTask 4: {list_2['task4'][0]}\n -> {list_2['task4'][1]}\n -> {list_2['task4'][2]}\n -> {list_2['task4'][3]}\nTask 5: {list_2['task5'][0]}\n -> {list_2['task5'][1]}\n -> {list_2['task5'][2]}\n -> {list_2['task5'][3]}\n"
	print_task_l3 = f"\nTask 1: {list_3['task1'][0]}\n -> {list_3['task1'][1]}\n -> {list_3['task1'][2]}\n -> {list_3['task1'][3]}\nTask 2: {list_3['task2'][0]}\n -> {list_3['task2'][1]}\n -> {list_3['task2'][2]}\n -> {list_3['task2'][3]}\nTask 3: {list_3['task3'][0]}\n -> {list_3['task3'][1]}\n -> {list_3['task3'][2]}\n -> {list_3['task3'][3]}\nTask 4: {list_3['task4'][0]}\n -> {list_3['task4'][1]}\n -> {list_3['task4'][2]}\n -> {list_3['task4'][3]}\nTask 5: {list_3['task5'][0]}\n -> {list_3['task5'][1]}\n -> {list_3['task5'][2]}\n -> {list_3['task5'][3]}\n"


def list_select(): #Allows the user to select a list

	global list_chosen

	list_chosen = str(input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n"))

	if list_chosen == list_1_name:
		list_chosen = list_1
	
	elif list_chosen == list_2_name:
		list_chosen = list_2

	elif list_chosen == list_3_name:
		list_chosen = list_3

def task_select(): #Allows the user to select a task

	global task_chosen

	list_select()
	
	if list_chosen == list_1:

		task_chosen = input(f"\nSelect a task: {print_task_l1}\n")
	
	elif list_chosen == list_2:

		task_chosen = input(f"\nSelect a task: {print_task_l2}\n")

	elif list_chosen == list_3:

		task_chosen = input(f"\nSelect a task: {print_task_l3}\n")

def subtask_select():

	global subtask_chosen

	task_select()

	subtask_chosen = input(f"\nSelect a subtask: ")

	subtask_chosen = int(subtask_chosen)

#Startup
print("To-Do List Copyright (C) 2022 Odysseus-Abraham Kirikopoulos\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it under certain conditions.") #Prints the GNU Public License 3.0
print("Build Version: 1.6.1 Prebuild 5\nBuild under development\n\n\n") #Prints the build version

#Greet
print("~~~ MY TO-DO LIST ~~~")

#Operations
while True: #Infinete loop
	
	operation_tree = input("\nSelect the type of operation:\n(1) Create\n(2) Delete/Check off\n(3) Rename\n(4) View\nTo exit press 0\n\n") #Asks the user to select an operation

	if operation_tree == "0": #User exiting
		break

	elif operation_tree == "1": #User creating a list or a (sub)task
		operation = input("\n(1) Create a list\n(2) Create a task\n(3) Create a subtask\n\n")

		#Create a new list
		if operation == "1":

			if(list_1_name == "Not defined"): #Checking which list is not occupied in order to create a list

				list_1_name = input("\nName your new list: ")
				print(f"{list_1_name} created")

			elif(list_2_name == "Not defined"):

				list_2_name = input("\nName your new list: ")
				print(f"{list_2_name} created")

			elif(list_3_name == "Not defined"):

				list_3_name = input("\nName your new list: ")
				print(f"{list_3_name} created")

			elif(list_1_name and list_2_name and list_3_name != "Not defined"): #In case there are 3 lists, no more can be created

				print("Err:MaxListsReached")

			refresh_pr_list()

		#Create a new task
		elif operation == "2":

			list_select()

			if list_chosen["task1"][0] == "": #Checking an non-occupied task to create the new one
				list_chosen["task1"][0] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif list_chosen["task2"][0] == "" : #Checking an non-occupied task to create the new one
				list_chosen["task2"][0] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif list_chosen["task3"][0] == "" : #Checking an non-occupied task to create the new one
				list_chosen["task3"][0] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif list_chosen["task4"][0] == "" : #Checking an non-occupied task to create the new one
				list_chosen["task4"][0] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif list_chosen["task5"][0] == "" : #Checking an non-occupied task to create the new one
				list_chosen["task5"][0] = input("\nEnter your task: ")
				print("Task created successfully!")

			else:
				print("Err:MaxTasksReached") #In case there are 5 tasks, no more can be created

			refresh_pr_list()

		#Create a subtask
		elif operation == "3":

			task_select()

			if list_chosen[task_chosen][1] == "":
				list_chosen[task_chosen][1] = input("\nEnter your task: ")
				print("\nTask created successfully!")

			elif list_chosen[task_chosen][2] == "":
				list_chosen[task_chosen][2] = input("\nEnter your task: ")
				print("\nTask created successfully!")

			elif list_chosen[task_chosen][3] == "":
				list_chosen[task_chosen][3] = input("\nEnter your task: ")
				print("\nTask created successfully!")

			refresh_pr_list()

	if operation_tree == "2": #User deleting/checking off a list or a (sub)task

		operation = input("\n(1) Check off a task\n(2) Check off a subtask\n(3) Delete a list\n(4) Delete a task\n\n")

		#Chech off a task
		if operation == "1":

			task_select()									

			list_chosen[task_chosen][0] += " [Done]"
			print("Task has been checked off")

			refresh_pr_list()

		#Check off a subtask
		if operation == "2":

			subtask_select()

			list_chosen[task_chosen][subtask_chosen] += " [Done]"
			print("Subtask has been checked off")

			refresh_pr_list()

		#Delete a list
		if operation == "3":

			list_select()

			if list_chosen == list_1:
				list_1_name = list_2_name
				list_2_name = list_3_name
				list_3_name = "Not defined"
				list_1 = list_2
				list_2 = list_3
				list_3 = {"task1":["","","",""],"task2":["","","",""],"task3":["","","",""],"task4":["","","",""],"task5":["","","",""]}
				print("List deleted successfully")

			elif list_chosen == list_2:
				list_2_name = list_3_name
				list_3_name = "Not defined"
				list_2 = list_3
				list_3 = {"task1":["","","",""],"task2":["","","",""],"task3":["","","",""],"task4":["","","",""],"task5":["","","",""]}
				print("List deleted successfully")

			elif list_chosen == list_3:
				list_3_name = "Not defined"
				list_3 = {"task1": ["", "", "", ""], "task2": ["", "", "", ""], "task3": ["", "", "", ""], "task4": ["", "", "", ""], "task5": ["", "", "", ""]}
				print("List deleted successfully")

			refresh_pr_list()

		#Delete a task
		if operation == "4" :
				
				task_select()

				list_chosen[task_chosen][0] = ""
				list_chosen[task_chosen][1] = ""
				list_chosen[task_chosen][2] = ""
				list_chosen[task_chosen][3] = ""		

				refresh_pr_list()			

	if operation_tree == "3": #User editing a list or a task

		operation = input("\n(1) Rename a list\n(2) Rename a task\n\n")
		
		#Rename a list
		if operation == "1":

			list_select()

			if list_chosen == list_1: #Printing the list
				list_1_name = input(f"Rename the list (previous name: {list_1_name}): ")

			elif list_chosen == list_2:
				list_2_name = input(f"Rename the list (previous name: {list_2_name}): ")
					
			elif list_chosen == list_3:
				list_3_name = input(f"Rename the list (previous name: {list_3_name}): ")

			refresh_pr_list()
			
		#Rename a task
		if operation == "2":
			
			task_select()

			list_chosen[task_chosen][0] = input(f"Rename the task: ")				

			refresh_pr_list()	

	if operation_tree == "4": #User viewing a list
		
		list_select()

		if list_chosen == list_1: #Printing the list
			print(print_task_l1)
				
		elif list_chosen == list_2:
			print(print_task_l2)

		elif list_chosen == list_3:
			print(print_task_l3)
			
exit_key = input("\nTo exit, press Enter\n") #Exiting the program


#This program is protected by the GNU General Public License v3.0 | ODYSSEUS-ABRAHAM KIRIKOPOULOS | 2022 | SOME RIGHTS RESERVED