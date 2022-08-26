'''
Authors: Odysseus-Abraham Kirikopoulos
This script is protected by the GNU Public License 3.0. Refer source as "Odysseus-Abraham Kirikopoulos" when distributing the software.
Version: 1.6 Beta
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
list_choosen = "Not defined" #The selected list to complete and operation
task_choosen = "Not defined" #The selected task to complete and operation

#Startup
print("Author: Odysseus-Abraham Kirikopoulos")
print('This script is protected by the GNU Public Lisence 3.0. Refer to source as "Odysseus-Abraham Kirikopoulos" when distributing the software.')
print("Build Version: 1.6 Beta\n\n\n")

#Greet
print("~~~ MY TO-DO LIST ~~~")
print("Select an operation")

#Operations
while True: #Infinete loop
	
	operation_tree = input("\nSelect the type of operation:\n(1) Create\n(2) Delete/Check off\n(3) Rename\n(4) View\n\n")

	if operation_tree == "1":
		operation = input("\n(1) Create a list\n(2) Create a task\n(3) Create a subtask\n\n")

		#Operation: Create a new list
		if(operation == "1"):
			if(list_1_name == "Not defined"): #Checking which list is not occupied in order to create a list
				list_1_name = input("\nName your new list: ")
				print(list_1_name , "created!")
			elif(list_2_name == "Not defined"):
				list_2_name = input("\nName your new list: ")
				print(list_2_name , "created!")
			elif(list_3_name == "Not defined"):
				list_3_name = input("\nName your new list: ")
				print(list_3_name , "created!")
			elif(list_1_name and list_2_name and list_3_name != "Not defined"): #In case there are 3 lists, no more can be created
				print("Err:MaxListsReached")

		#Operation: Create a new task
		elif(operation == "2"):

			list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n") #The user is choosing a list to create the task

			if(list_choosen == "Not defined"): #If the option is an non-occupied list, an error will return
				print("\nError: ListNotUsable")

			elif(list_choosen == list_1_name): #Going into the list
				
				if(list_1["task1"][0] == ""): #Checking an non-occupied task to create the new one
					list_1["task1"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_1["task2"][0] == ""):
					list_1["task2"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_1["task3"][0] == ""):
					list_1["task3"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_1["task4"][0] == ""):
					list_1["task4"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_1["task5"][0] == ""):
					list_1["task5"][0] = input("\nEnter your task: ")
					print("Task created successfully!")
					
			elif(list_choosen == list_2_name):

				if(list_2["task1"][0] == ""):
					list_2["task1"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_2["task2"][0] == ""):
					list_2["task2"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_2["task3"][0] == ""):
					list_2["task3"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_2["task4"][0] == ""):
					list_2["task4"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_2["task5"][0] == ""):
					list_2["task5"][0] = input("\nEnter your task: ")
					print("Task created successfully!")
			
			elif(list_choosen == list_3_name):
				if(list_3["task1"][0] == ""):
					list_3["task1"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_3["task2"][0] == ""):
					list_3["task2"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_3["task3"][0] == ""):
					list_3["task3"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_3["task4"][0] == ""):
					list_3["task4"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				elif(list_3["task5"][0] == ""):
					list_3["task5"][0] = input("\nEnter your task: ")
					print("Task created successfully!")

				else: #If the input is not applicable, an error will pop up
					print("Err:ListNotFound")

		#Create a subtask
		elif operation == "3":

			list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n") #The user is choosing a list to create the task

			if(list_choosen == "Not defined"): #If the option is an non-occupied list, an error will return
				print("\nError: ListNotUsable")

			elif(list_choosen == list_1_name): #Going into the list
				
				task_choosen = input("Select a task: ")

				if task_choosen == list_1["task1"][0]:

					if list_1["task1"][1] == "":
						list_1["task1"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_1["task1"][2] == "":
						list_1["task1"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_1["task1"][3] == "":
						list_1["task1"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_1["task2"][0]:

					if list_1["task2"][1] == "":
						list_1["task2"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_1["task2"][2] == "":
						list_1["task2"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_1["task2"][3] == "":
						list_1["task2"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_1["task3"][0]:

					if list_1["task3"][1] == "":
						list_1["task3"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_1["task3"][2] == "":
						list_1["task3"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_1["task3"][3] == "":
						list_1["task3"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_1["task4"][0]:

					if list_1["task4"][1] == "":
						list_1["task4"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_1["task4"][2] == "":
						list_1["task4"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_1["task4"][3] == "":
						list_1["task4"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_1["task5"][0]:

					if list_1["task5"][1] == "":
						list_1["task5"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_1["task5"][2] == "":
						list_1["task5"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_1["task2"][3] == "":
						list_1["task5"][3] = input("\nEnter your task: ")
						print("Task created successfully!")
					
			elif(list_choosen == list_2_name): #Going into the list
				
				task_choosen = input("Select a task: ")

				if task_choosen == list_2["task1"][0]:

					if list_2["task1"][1] == "":
						list_2["task1"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_2["task1"][2] == "":
						list_2["task1"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_2["task1"][3] == "":
						list_2["task1"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_2["task2"][0]:

					if list_2["task2"][1] == "":
						list_2["task2"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_2["task2"][2] == "":
						list_2["task2"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_2["task2"][3] == "":
						list_2["task2"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_2["task3"][0]:

					if list_2["task3"][1] == "":
						list_2["task3"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_2["task3"][2] == "":
						list_2["task3"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_2["task3"][3] == "":
						list_2["task3"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_2["task4"][0]:

					if list_2["task4"][1] == "":
						list_2["task4"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_2["task4"][2] == "":
						list_2["task4"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_2["task4"][3] == "":
						list_2["task4"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_1["task5"][0]:

					if list_2["task5"][1] == "":
						list_2["task5"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_2["task5"][2] == "":
						list_2["task5"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_2["task2"][3] == "":
						list_2["task5"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

			elif(list_choosen == list_3_name): #Going into the list
				
				task_choosen = input("Select a task: ")

				if task_choosen == list_3["task1"][0]:

					if list_3["task1"][1] == "":
						list_3["task1"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_3["task1"][2] == "":
						list_3["task1"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_3["task1"][3] == "":
						list_3["task1"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_3["task2"][0]:

					if list_3["task2"][1] == "":
						list_3["task2"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_3["task2"][2] == "":
						list_3["task2"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_3["task2"][3] == "":
						list_3["task2"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_3["task3"][0]:

					if list_3["task3"][1] == "":
						list_3["task3"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_3["task3"][2] == "":
						list_3["task3"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_3["task3"][3] == "":
						list_3["task3"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_3["task4"][0]:

					if list_3["task4"][1] == "":
						list_3["task4"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_3["task4"][2] == "":
						list_3["task4"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_3["task4"][3] == "":
						list_3["task4"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

				elif task_choosen == list_3["task5"][0]:

					if list_3["task5"][1] == "":
						list_3["task5"][1] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_3["task5"][2] == "":
						list_3["task5"][2] = input("\nEnter your task: ")
						print("Task created successfully!")

					elif list_3["task2"][3] == "":
						list_3["task5"][3] = input("\nEnter your task: ")
						print("Task created successfully!")

	if operation_tree == "2":

		operation = input("\n(1) Check off a task\n(2) Check off a subtask\n(3) Delete a list\n(4) Delete a task\n\n")

		if operation == "1":

			list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")

			if(list_choosen == "Not defined"): #If option is non-occupied then an error pops up
				print("\nError: ListNotUsable")
				list_choosen = ""
				

			elif(list_choosen == list_1_name): 
				task_choosen = input(f"\nSelect a task: {list_1}\n")

				if(task_choosen == ""): #If option is non-occupied then an error pops up
					print("Err:TaskNotUsable")
					

				elif(task_choosen == list_1["task1"][0]): #Deleting task
					list_1["task1"][0] += " [Done]"
					print("Task has been deleted")
					

				elif(task_choosen == list_1["task2"][0]):
					list_1["task2"][0] += " [Done]"
					print("Task has been deleted")
					

				elif(task_choosen == list_1["task3"][0]):
					list_1["task3"][0] += " [Done]"
					print("Task has been deleted")
					

				elif(task_choosen == list_1["task4"][0]):
					list_1["task4"][0] += " [Done]"
					print("Task has been deleted")
					

				elif(task_choosen == list_1["task5"][0]):
					list_1["task5"][0] += " [Done]"
					print("Task has been deleted")
					

				else: #If the input is not applicable, an error will pop up
					print("Err:TaskNotFound") 
					

			elif(list_choosen == list_2_name):
				task_choosen = input(f"\nSelect a task: {list_2}\n")

				if(task_choosen == ""):
					print("Err:TaskNotUsable")
					

				elif(task_choosen == list_2["task1"][0]):
					list_2["task1"][0] += " [Done]"
					print("Task has been deleted")

				elif(task_choosen == list_2["task2"][0]):
					list_2["task2"][0] += " [Done]"
					print("Task has been deleted")

				elif(task_choosen == list_2["task3"][0]):
					list_2["task3"][0] += " [Done]"
					print("Task has been deleted")

				elif(task_choosen == list_2["task4"][0]):
					list_2["task4"][0] += " [Done]"
					print("Task has been deleted")

				elif(task_choosen == list_2["task5"][0]):
					list_2["task5"][0] += " [Done]"
					print("Task has been deleted")

				else:
					print("Err:TaskNotFound")

			elif(list_choosen == list_1_name):
				task_choosen = input(f"\nSelect a task: {list_3}\n")

				if(task_choosen == ""):
					print("Err:TaskNotUsable")

				elif(task_choosen == list_3["task1"][0]):
					list_3["task1"][0] += " [Done]"
					print("Task has been deleted")

				elif(task_choosen == list_3["task2"][0]):
					list_3["task2"][0] += " [Done]"
					print("Task has been deleted")

				elif(task_choosen == list_3["task3"][0]):
					list_3["task3"][0] += " [Done]"
					print("Task has been deleted")

				elif(task_choosen == list_3["task4"][0]):
					list_3["task4"][0] += " [Done]"
					print("Task has been deleted")

				elif(task_choosen == list_3["task5"][0]):
					list_3["task5"][0] += " [Done]"
					print("Task has been deleted")

				else:
					print("Err:TaskNotFound")

			else: #If the input is not applicable, an error will pop up
				print("Err:ListNotFound")

		if operation == "2":
			list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")

			if list_choosen == list_1_name:

				task_choosen = input(f"\nSelect a task: {list_1}\n")

				if task_choosen == list_1["task1"][0]:

					subtask_choosen = input("\nSelect a subtask: " + list_1["task1"])

					if subtask_choosen == list_1["task1"][1]:

						list_1["task1"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task1"][2]:

						list_1["task1"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task1"][3]:

						list_1["task1"][3] += " [Done]"
						print("Success")

					else:
						
						print("Error")

				if task_choosen == list_1["task2"][0]:

					subtask_choosen = input("Select a subtask: " + list_1["task2"])

					if subtask_choosen == list_1["task2"][1]:

						list_1["task2"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task2"][2]:

						list_1["task2"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task2"][3]:

						list_1["task2"][3] += " [Done]"
						print("Success")

					else:

						print("Error")

				if task_choosen == list_1["task3"][0]:

					subtask_choosen = input("Select a subtask: " + list_1["task3"])

					if subtask_choosen == list_1["task3"][1]:

						list_1["task3"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task3"][2]:

						list_1["task3"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task3"][3]:

						list_1["task3"][3] += " [Done]"

					else:

						print("Error")

				if task_choosen == list_1["task4"][0]:

					subtask_choosen = input("Select a subtask " + list_1["task4"])

					if subtask_choosen == list_1["task4"][1]:

						list_1["task4"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task4"][2]:

						list_1["task4"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task4"][3]:

						list_1["task4"][3] += " [Done]"
						print("Success")

					else:

						print("Error")
				
				if task_choosen == list_1["task5"][0]:

					subtask_choosen = input("Select a subtask " + list_1["task5"])

					if subtask_choosen == list_1["task5"][1]:

						list_1["task5"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task4"][2]:

						list_1["task5"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task4"][3]:

						list_1["task5"][3] += " [Done]"
						print("Success")

					else:

						print("Error")

				if task_choosen == list_1["task1"][0]:

					subtask_choosen = input("\nSelect a subtask: " + list_1["task1"])

					if subtask_choosen == list_1["task1"][1]:

						list_1["task1"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task1"][2]:

						list_1["task1"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task1"][3]:

						list_1["task1"][3] += " [Done]"
						print("Success")

					else:
						
						print("Error")

				if task_choosen == list_1["task2"][0]:

					subtask_choosen = input("Select a subtask: " + list_1["task2"])

					if subtask_choosen == list_1["task2"][1]:

						list_1["task2"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task2"][2]:

						list_1["task2"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task2"][3]:

						list_1["task2"][3] += " [Done]"
						print("Success")

					else:

						print("Error")

				if task_choosen == list_1["task3"][0]:

					subtask_choosen = input("Select a subtask: " + list_1["task3"])

					if subtask_choosen == list_1["task3"][1]:

						list_1["task3"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task3"][2]:

						list_1["task3"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task3"][3]:

						list_1["task3"][3] += " [Done]"

					else:

						print("Error")

				if task_choosen == list_1["task4"][0]:

					subtask_choosen = input("Select a subtask " + list_1["task4"])

					if subtask_choosen == list_1["task4"][1]:

						list_1["task4"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task4"][2]:

						list_1["task4"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task4"][3]:

						list_1["task4"][3] += " [Done]"
						print("Success")

					else:

						print("Error")
				
				if task_choosen == list_1["task5"][0]:

					subtask_choosen = input("Select a subtask " + list_1["task5"])

					if subtask_choosen == list_1["task5"][1]:

						list_1["task5"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task4"][2]:

						list_1["task5"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_1["task4"][3]:

						list_1["task5"][3] += " [Done]"
						print("Success")

					else:

						print("Error")


				if task_choosen == list_3["task1"][0]:

					subtask_choosen = input("\nSelect a subtask: " + list_3["task1"])

					if subtask_choosen == list_3["task1"][1]:

						list_3["task1"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_3["task1"][2]:

						list_3["task1"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_3["task1"][3]:

						list_3["task1"][3] += " [Done]"
						print("Success")

					else:
						
						print("Error")

				if task_choosen == list_3["task2"][0]:

					subtask_choosen = input("Select a subtask: " + list_3["task2"])

					if subtask_choosen == list_3["task2"][1]:

						list_2["task2"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_3["task2"][2]:

						list_3["task2"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_3["task2"][3]:

						list_3["task2"][3] += " [Done]"
						print("Success")

					else:

						print("Error")

				if task_choosen == list_3["task3"][0]:

					subtask_choosen = input("Select a subtask: " + list_3["task3"])

					if subtask_choosen == list_3["task3"][1]:

						list_3["task3"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_3["task3"][2]:

						list_3["task3"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_3["task3"][3]:

						list_3["task3"][3] += " [Done]"

					else:

						print("Error")

				if task_choosen == list_3["task4"][0]:

					subtask_choosen = input("Select a subtask " + list_3["task4"])

					if subtask_choosen == list_3["task4"][1]:

						list_2["task4"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_3["task4"][2]:

						list_2["task4"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_3["task4"][3]:

						list_2["task4"][3] += " [Done]"
						print("Success")

					else:

						print("Error")
				
				if task_choosen == list_3["task5"][0]:

					subtask_choosen = input("Select a subtask " + list_3["task5"])

					if subtask_choosen == list_3["task5"][1]:

						list_3["task5"][1] += " [Done]"
						print("Success")

					elif subtask_choosen == list_3["task4"][2]:

						list_3["task5"][2] += " [Done]"
						print("Success")

					elif subtask_choosen == list_3["task4"][3]:

						list_3["task5"][3] += " [Done]"
						print("Success")

					else:

						print("Error")

		#Delete a list
		if operation == "3":
			list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")

			if list_choosen == list_1_name:
				list_1_name = "Not Defined"
				list_1 = {"task1": "", "task2": "", "task3": "", "task4": "", "task5": ""}

			if list_choosen == list_2_name:
				list_2_name = "Not Defined"
				list_2 = {"task1": "", "task2": "", "task3": "", "task4": "", "task5": ""}

			if list_choosen == list_3_name:
				list_3_name = "Not defined"
				list_3 = {"task1": "", "task2": "", "task3": "", "task4": "", "task5": ""}

		#Operation: Delete a task
		if(operation == "4"):
			list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")

			if(list_choosen == "Not defined"): #If option is non-occupied then an error pops up
				print("\nError: ListNotUsable")
				list_choosen = ""
				

			elif(list_choosen == list_1_name): 
				task_choosen = input(f"\nSelect a task: {list_1}\n")

				if(task_choosen == ""): #If option is non-occupied then an error pops up
					print("Err:TaskNotUsable")
					

				elif(task_choosen == list_1["task1"][0]): #Deleting task
					list_1["task1"][0] = ""
					list_1["task1"][1] = ""
					list_1["task1"][2] = ""
					list_1["task1"][3] = ""
					print("Task has been deleted")
					

				elif(task_choosen == list_1["task2"][0]):
					list_1["task2"][0] = ""
					list_1["task2"][1] = ""
					list_1["task2"][2] = ""
					list_1["task2"][3] = ""
					print("Task has been deleted")
					

				elif(task_choosen == list_1["task3"][0]):
					list_1["task3"][0] = ""
					list_1["task3"][1] = ""
					list_1["task3"][2] = ""
					list_1["task3"][3] = ""
					print("Task has been deleted")
					

				elif(task_choosen == list_1["task4"][0]):
					list_1["task4"][0] = ""
					list_1["task4"][1] = ""
					list_1["task4"][2] = ""
					list_1["task4"][3] = ""
					print("Task has been deleted")
					

				elif(task_choosen == list_1["task5"][0]):
					list_1["task5"][0] = ""
					list_1["task5"][1] = ""
					list_1["task5"][2] = ""
					list_1["task5"][3] = ""
					print("Task has been deleted")
					

				else: #If the input is not applicable, an error will pop up
					print("Err:TaskNotFound") 
					

			elif(list_choosen == list_2_name):
				task_choosen = input(f"\nSelect a task: {list_2}\n")

				if(task_choosen == ""):
					print("Err:TaskNotUsable")
					

				elif(task_choosen == list_2["task1"][0]):
					list_2["task1"][0] = ""
					list_2["task1"][1] = ""
					list_2["task1"][2] = ""
					list_2["task1"][3] = ""
					print("Task has been deleted")

				elif(task_choosen == list_2["task2"][0]):
					list_2["task2"][0] = ""
					list_2["task2"][1] = ""
					list_2["task2"][2] = ""
					list_2["task2"][3] = ""
					print("Task has been deleted")

				elif(task_choosen == list_2["task3"][0]):
					list_2["task3"][0] = ""
					list_2["task3"][1] = ""
					list_2["task3"][2] = ""
					list_2["task3"][3] = ""
					print("Task has been deleted")

				elif(task_choosen == list_2["task4"][0]):
					list_2["task4"][0] = ""
					list_2["task4"][1] = ""
					list_2["task4"][2] = ""
					list_2["task4"][3] = ""
					print("Task has been deleted")

				elif(task_choosen == list_2["task5"][0]):
					list_2["task5"][0] = ""
					list_2["task5"][1] = ""
					list_2["task5"][2] = ""
					list_2["task5"][3] = ""
					print("Task has been deleted")

				else:
					print("Err:TaskNotFound")

			elif(list_choosen == list_1_name):
				task_choosen = input(f"\nSelect a task: {list_3}\n")

				if(task_choosen == ""):
					print("Err:TaskNotUsable")

				elif(task_choosen == list_3["task1"][0]):
					list_3["task1"][0] = ""
					list_3["task1"][1] = ""
					list_3["task1"][2] = ""
					list_3["task1"][3] = ""
					print("Task has been deleted")

				elif(task_choosen == list_3["task2"][0]):
					list_3["task2"][0] = ""
					list_3["task2"][1] = ""
					list_3["task2"][2] = ""
					list_3["task2"][3] = ""
					print("Task has been deleted")

				elif(task_choosen == list_3["task3"][0]):
					list_3["task3"][0] = ""
					list_3["task3"][1] = ""
					list_3["task3"][2] = ""
					list_3["task3"][3] = ""
					print("Task has been deleted")

				elif(task_choosen == list_3["task4"][0]):
					list_3["task4"][0] = ""
					list_3["task4"][1] = ""
					list_3["task4"][2] = ""
					list_3["task4"][3] = ""
					print("Task has been deleted")

				elif(task_choosen == list_3["task5"][0]):
					list_3["task5"][0] = ""
					list_3["task5"][1] = ""
					list_3["task5"][2] = ""
					list_3["task5"][3] = ""
					print("Task has been deleted")

				else:
					print("Err:TaskNotFound")

			else: #If the input is not applicable, an error will pop up
				print("Err:ListNotFound")

	if operation_tree == "3":

		operation = input("\n(1) Rename a list\n(2) Rename a task\n\n")

		if operation == "1":

			list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")

			if(list_choosen == "Not defined"): #If option is non-occupied then an error pops up
				print("\nError: ListNotUsable")
				list_choosen = ""

			elif(list_choosen == list_1_name): #Printing the list
				list_1_name = input(f"Name the list (previous name: {list_1_name}): ")

			elif(list_choosen == list_2_name):
				list_2_name = input(f"Name the list (previous name: {list_2_name}): ")
					

			elif(list_choosen == list_3_name):
				list_3_name = input(f"Name the list (previous name: {list_3_name}): ")
					

			else: #If the input is not applicable, an error will pop up
				print("Err:ListNotFound")

		if operation == "2":
			
			list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")

			if(list_choosen == "Not defined"): #If option is non-occupied then an error pops up
				print("\nError: ListNotUsable")
				list_choosen = ""
				

			elif(list_choosen == list_1_name): 
				task_choosen = input(f"\nSelect a task: {list_1}\n")

				if(task_choosen == ""): #If option is non-occupied then an error pops up
					print("Err:TaskNotUsable")
					

				elif(task_choosen == list_1["task1"][0]): #Renaming task
					list_1["task1"][0] = input("Name the task: ")					

				elif(task_choosen == list_1["task2"][0]):
					list_1["task2"][0] = input("Name the task: ")

				elif(task_choosen == list_1["task3"][0]):
					list_1["task3"][0] = input("Name the task: ")

				elif(task_choosen == list_1["task4"][0]):
					list_1["task4"][0] = input("Name the task: ")					

				elif(task_choosen == list_1["task5"][0]):
					list_1["task5"][0] = input("Name the task: ")

				else: #If the input is not applicable, an error will pop up
					print("Err:TaskNotFound") 
					

			elif(list_choosen == list_2_name): 
				task_choosen = input(f"\nSelect a task: {list_1}\n")

				if(task_choosen == ""): #If option is non-occupied then an error pops up
					print("Err:TaskNotUsable")
					

				elif(task_choosen == list_2["task1"][0]): #Renaming task
					list_2["task1"][0] = input("Name the task: ")					

				elif(task_choosen == list_2["task2"][0]):
					list_2["task2"][0] = input("Name the task: ")

				elif(task_choosen == list_2["task3"][0]):
					list_2["task3"][0] = input("Name the task: ")

				elif(task_choosen == list_2["task4"][0]):
					list_2["task4"][0] = input("Name the task: ")					

				elif(task_choosen == list_2["task5"][0]):
					list_2["task5"][0] = input("Name the task: ")

				else: #If the input is not applicable, an error will pop up
					print("Err:TaskNotFound")

			elif(list_choosen == list_3_name): 
				task_choosen = input(f"\nSelect a task: {list_1}\n")

				if(task_choosen == ""): #If option is non-occupied then an error pops up
					print("Err:TaskNotUsable")
					

				elif(task_choosen == list_3["task1"][0]): #Renaming task
					list_3["task1"][0] = input("Name the task: ")					

				elif(task_choosen == list_1["task2"][0]):
					list_3["task2"][0] = input("Name the task: ")

				elif(task_choosen == list_1["task3"][0]):
					list_3["task3"][0] = input("Name the task: ")

				elif(task_choosen == list_1["task4"][0]):
					list_3["task4"][0] = input("Name the task: ")					

				elif(task_choosen == list_1["task5"][0]):
					list_3["task5"][0] = input("Name the task: ")

				else: #If the input is not applicable, an error will pop up
					print("Err:TaskNotFound") 
 

	#Operation: View list
	if operation_tree == "4":
		list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n\n") #User selects list

		if(list_choosen == "Not defined"): #If option is non-occupied then an error pops up
			print("\nError: ListNotUsable")
			list_choosen = ""
			

		elif(list_choosen == list_1_name): #Printing the list
			print(list_1)
				

		elif(list_choosen == list_2_name):
			print(list_2)
				

		elif(list_choosen == list_3_name):
			print(list_3)
				

		else: #If the input is not applicable, an error will pop up
			print("Err:ListNotFound")

	elif operation == "0": #User exiting
		break

	else:
		print("Err:InvalidOperation") #If operation selected isn't applicable an error pops up
		 

			
exit_key = input("Press any key to exit\n")