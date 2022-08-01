'''
Authors: Odysseus-Abraham Kirikopoulos
This script is protected by the GNU Public Lisence 3.0. Refer to source as "Odysseus-Abraham Kirikopoulos" when distributing the software.
Version: 1.5 Beta
WARNING: The following program was created for educational purposes only
'''

#Variable
list_1 = {"task1": "", "task2": "", "task3": "", "task4": "", "task5": ""}
list_1_name = "Not defined"
list_2 = {"task1": "", "task2": "", "task3": "", "task4": "", "task5": ""}
list_2_name = "Not defined"
list_3 = {"task1": "", "task2": "", "task3": "", "task4": "", "task5": ""}
list_3_name = "Not defined"
operation = "Not defined"
list_choosen = "Not defined"
task_choosen = "Not defined"

#Startup
print("Lanching...\n")
print("Author: Odysseus-Abraham Kirikopoulos")
print('This script is protected by the GNU Public Lisence 3.0. Refer to source as "Odysseus-Abraham Kirikopoulos" when distributing the software.')
print("Build Version: 1.5 Beta\n\n\n")

#Greet
print("~~~ MY TO-DO LIST ~~~")
print("Select an operation")

#Operations
while operation != 0:
	
	print("\n\n1) Create a list\n2) Create a new task\n3) View a list\n4) Delete a task\nTo exit type 0")
	operation = input("Select an operation: ")

	#Operation: Create a new list
	if(operation == "1"):
		if(list_1_name == "Not defined"):
			list_1_name = input("\nName your new list: ")
			print(list_1_name , "created!")
		if(list_2_name == "Not defined"):
			list_2_name = input("\nName your new list: ")
			print(list_2_name , "created!")
		if(list_3_name == "Not defined"):
			list_3_name = input("\nName your new list: ")
			print(list_3_name , "created!")
		if(list_1_name and list_2_name and list_3_name != "Not defined"):
			print("\Err:MaxListsReached")

	#Operation: Create a new task
	elif(operation == "2"):

		list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")

		if(list_choosen == "Not defined"):
			print("\nError: ListNotUsable")

		elif(list_choosen == list_1_name):
			
			if(list_1["task1"] == ""):
				list_1["task1"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_1["task2"] == ""):
				list_1["task2"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_1["task3"] == ""):
				list_1["task3"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_1["task4"] == ""):
				list_1["task4"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_1["task5"] == ""):
				list_1["task5"] = input("\nEnter your task: ")
				print("Task created successfully!")
				
		elif(list_choosen == list_2_name):

			if(list_2["task1"] == ""):
				list_2["task1"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_2["task2"] == ""):
				list_2["task2"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_2["task3"] == ""):
				list_2["task3"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_2["task4"] == ""):
				list_2["task4"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_2["task5"] == ""):
				list_2["task5"] = input("\nEnter your task: ")
				print("Task created successfully!")
		
		elif(list_choosen == list_3_name):
			if(list_3["task1"] == ""):
				list_3["task1"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_3["task2"] == ""):
				list_3["task2"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_3["task3"] == ""):
				list_3["task3"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_3["task4"] == ""):
				list_3["task4"] = input("\nEnter your task: ")
				print("Task created successfully!")

			elif(list_3["task5"] == ""):
				list_3["task5"] = input("\nEnter your task: ")
				print("Task created successfully!")

		else:
			print("Err:ListNotFound")


	#Operation: View list
	elif(operation == "3"):
		list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")

		if(list_choosen == "Not defined"):
			print("\nError: ListNotUsable")
			list_choosen = ""

		elif(list_choosen == list_1_name):
			print(list_1)

		elif(list_choosen == list_2_name):
			print(list_2)

		elif(list_choosen == list_3_name):
			print(list_3)

		else:
			print("Err:ListNotFound")


	#Operation: Delete a task
	elif(operation == "4"):
		list_choosen = input(f"\nSelect a list\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")

		if(list_choosen == "Not defined"):
			print("\nError: ListNotUsable")
			list_choosen = ""

		elif(list_choosen == list_1_name):
			task_choosen = input(f"\nSelect a task: {list_1}\n")

			if(task_choosen == ""):
				print("Err:TaskNotUsable")

			elif(task_choosen == list_1["task1"]):
				list_1["task1"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_1["task2"]):
				list_1["task2"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_1["task3"]):
				list_1["task3"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_1["task4"]):
				list_1["task4"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_1["task5"]):
				list_1["task5"] = ""
				print("Task has been deleted")

			else:
				print("Err:TaskNotFound")

		elif(list_choosen == list_2_name):
			task_choosen = input(f"\nSelect a task: {list_2}\n")

			if(task_choosen == ""):
				print("Err:TaskNotUsable")

			elif(task_choosen == list_2["task1"]):
				list_2["task1"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_2["task2"]):
				list_2["task2"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_2["task3"]):
				list_2["task3"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_2["task4"]):
				list_2["task4"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_2["task5"]):
				list_2["task5"] = ""
				print("Task has been deleted")

			else:
				print("Err:TaskNotFound")

		elif(list_choosen == list_1_name):
			task_choosen = input(f"\nSelect a task: {list_3}\n")

			if(task_choosen == ""):
				print("Err:TaskNotUsable")

			elif(task_choosen == list_3["task1"]):
				list_3["task1"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_3["task2"]):
				list_3["task2"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_3["task3"]):
				list_3["task3"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_3["task4"]):
				list_3["task4"] = ""
				print("Task has been deleted")

			elif(task_choosen == list_3["task5"]):
				list_3["task5"] = ""
				print("Task has been deleted")

			else:
				print("Err:TaskNotFound")

		else:
			print("Err:ListNotFound")

	else:
		print("Err:InvalidOperation")

			
exit_key = input("Press any key to exit\n")
