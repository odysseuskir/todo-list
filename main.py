'''
Authors: Odysseus-Abraham Kirikopoulos
This script is protected by the GNU Public License 3.0. Refer source as "Odysseus-Abraham Kirikopoulos" when distributing the software.
Version: 1.6.1 Prebuild 3
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
list_choosen = "Not defined" #The selected list to complete an operation
task_choosen = "Not defined" #The selected task to complete an operation

gnu_pubic_license_v3 = "Copyright (C) 2022 Odysseus-Abraham Kirikopoulos. This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under certain conditions." #The GNU Public License 3.0

def list_select(): #Allows the user to select a list

	global list_choosen

	list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")

def task_select(): #Allows the user to select a task

	global task_choosen

	list_select()
	
	if list_choosen == list_1_name:

		task_choosen = input(f"\nSelect a (sub)task: {list_1}\n")

	elif list_choosen == list_2_name:

		task_choosen = input(f"\nSelect a (sub)task: {list_2}\n")

	elif list_choosen == list_3_name:

		task_choosen = input(f"\nSelect a (sub)task: {list_3}\n")

#Startup
print(gnu_pubic_license_v3) #Prints the GNU Public License 3.0
print("Build Version: 1.6.2 Prebuild 3\nBuild under development\n\n\n") #Prints the build version

#Greet
print("~~~ MY TO-DO LIST ~~~")
print("Select an operation")

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

		#Create a new task
		elif operation == "2":

			list_select()

			if list_choosen["task1"][0] == "": #Checking an non-occupied task to create the new one
				list_choosen["task1"][0] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif list_choosen["task2"][0] == "" : #Checking an non-occupied task to create the new one
				list_choosen["task2"][0] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif list_choosen["task3"][0] == "" : #Checking an non-occupied task to create the new one
				list_choosen["task3"][0] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif list_choosen["task4"][0] == "" : #Checking an non-occupied task to create the new one
				list_choosen["task4"][0] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif list_choosen["task5"][0] == "" : #Checking an non-occupied task to create the new one
				list_choosen["task5"][0] = input("\nEnter your task: ")
				print("Task created successfully!")

		#Create a subtask
		elif operation == "3":

			task_select()

			if list_choosen[task_choosen][1] == "":
				list_choosen[task_choosen][1] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif list_choosen[task_choosen][2] == "":
				list_choosen[task_choosen][2] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif list_choosen[task_choosen][3] == "":
				list_choosen[task_choosen][3] = input("\nEnter your task: ")
				print("Task created successfully!")

	if operation_tree == "2": #User deleting/checking off a list or a (sub)task

		operation = input("\n(1) Check off a task\n(2) Check off a subtask\n(3) Delete a list\n(4) Delete a task\n\n")

		#Chech off a task
		if operation == "1":

			task_select()									

			list_choosen[task_choosen][0] += " [Done]"
			print("Task has been checked off")

		#Check off a subtask
		if operation == "2":

			task_select()									

			if task_choosen == task_choosen[1]:		

				list_choosen[task_choosen][1] += " [Done]"
				print("Subtask has been checked off")

			elif task_choosen == task_choosen[2]:

				list_choosen[task_choosen][2] += " [Done]"
				print("Subtask has been checked off")

			elif task_choosen == task_choosen[3]:

				list_choosen[task_choosen][3] += " [Done]"
				print("Subtask has been checked off")

		#Delete a list
		if operation == "3":

			list_select()

			if list_choosen == list_1_name:
				list_1_name = "Not Defined"
				list_1 = {"task1": "", "task2": "", "task3": "", "task4": "", "task5": ""}

			if list_choosen == list_2_name:
				list_2_name = "Not Defined"
				list_2 = {"task1": "", "task2": "", "task3": "", "task4": "", "task5": ""}

			if list_choosen == list_3_name:
				list_3_name = "Not defined"
				list_3 = {"task1": "", "task2": "", "task3": "", "task4": "", "task5": ""}

		#Delete a task
		if operation == "4" :
				
				task_select()

				list_choosen[task_choosen][0] = ""
				list_choosen[task_choosen][1] = ""
				list_choosen[task_choosen][2] = ""
				list_choosen[task_choosen][3] = ""					

	if operation_tree == "3": #User editing a list or a task

		operation = input("\n(1) Rename a list\n(2) Rename a task\n\n")
		
		#Rename a list
		if operation == "1":

			list_select()

			if list_choosen == list_1_name: #Printing the list
				list_1_name = input(f"Rename the list (previous name: {list_1_name}): ")

			elif list_choosen == list_2_name:
				list_2_name = input(f"Rename the list (previous name: {list_2_name}): ")
					
			elif list_choosen == list_3_name:
				list_3_name = input(f"Rename the list (previous name: {list_3_name}): ")
			
		#Rename a task
		if operation == "2":
			
			task_select()

			list_choosen[task_choosen][0] = input(f"Rename the task: ")					

	if operation_tree == "4": #User viewing a list
		
		list_select()

		if(list_choosen == list_1_name): #Printing the list
			print(list_1)
				
		elif(list_choosen == list_2_name):
			print(list_2)

		elif(list_choosen == list_3_name):
			print(list_3)
			
exit_key = input("\nTo exit, press Enter\n") #Exiting the program


#This program is protected by the GNU General Public License v3.0 | ODYSSEUS-ABRAHAM KIRIKOPOULOS | 2022 | SOME RIGHTS RESERVED