'''
Authors: Odysseus Kirikopoulos
Copyright notice: The following program is protected from the Greek law, act 2121/1993
(C) ALL RIGHTS RESERVED - ODYSSEUS ABRAHAM KIRIKOPOULOS - 2021
Version: 1.4 stable
WARNING: The following program was created for educational purposes only
'''

#Variable
task_1_1 = ""
task_2_1 = ""
task_3_1 = ""
task_4_1 = ""
task_5_1 = ""
list_1_name = "Not defined"
task_1_2 = ""
task_2_2 = ""
task_3_2 = ""
task_4_2 = ""
task_5_2 = ""
list_2_name = "Not defined"
task_1_3 = ""
task_2_3 = ""
task_3_3 = ""
task_4_3 = ""
task_5_3 = ""
list_3_name = "Not defined"
operation = "Not defined"
list_choosen = "Not defined"
task_choosen = "Not defined"
quit_option = "n"


#Startup
print("Lanching...\n")
print("Author: Odysseus-Abraham Kirikopoulos")
print("Copyrigh notice: (C) ALL RIGHTS RESERVED - ODYSSEUS ABRAHAM KIRIKOPOULOS - 2021")
print("Build Version: 1.4 Stable\n\n\n")

#Greet
print("~~~ MY TO-DO LIST ~~~")
print("You are in the main menu. What would you like to do?")

#Operations
while(operation != "6"):
	print("\n\n1) Create a list\n2) Create a new task\n3) View a list\n4) Delete a task\n5) Exit")
	operation = input("Select an operation: ")

	#Complete operations 
	while True:
	#Operation: Create a new list
		if(operation == "1"):
			if(list_1_name == "Not defined"):
				list_1_name = input("\nName your new list: ")
				print(list_1_name , "created!")
				break
			if(list_2_name == "Not defined"):
				list_2_name = input("\nName your new list: ")
				print(list_2_name , "created!")
				break
			if(list_3_name == "Not defined"):
				list_3_name = input("\nName your new list: ")
				print(list_3_name , "created!")
				break
			if(list_1_name and list_2_name and list_3_name != "Not defined"):
				print("\Error: MaxAmmountOfListsReached")
				break

	#Operation: Create a new task
		if(operation == "2"):
			list_choosen = input(f"\nIn which list you want to create the task?\n[{list_1_name}]\n[{list_2_name}]\n[{list_3_name}]\n")
			if(list_choosen == "Not defined"):
				print("\nError: ListNotUsable")
				list_choosen = ""
				break
			if(list_choosen == list_1_name):
				if(task_1_1 == ""):
					task_1_1 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_2_1 == ""):
					task_2_1 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_3_1 == ""):
					task_3_1 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_4_1 == ""):
					task_4_1 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_5_1 == ""):
					task_5_1 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
			if(list_choosen == list_2_name):
				if(task_1_2 == ""):
					task_1_2 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_2_2 == ""):
					task_2_2 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_3_2 == ""):
					task_3_2 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_4_2 == ""):
					task_4_2 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_5_2 == ""):
					task_5_2 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
			if(list_choosen == list_3_name):
				if(task_1_3 == ""):
					task_1_3 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_2_3 == ""):
					task_2_3 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_3_3 == ""):
					task_3_3 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_4_3 == ""):
					task_4_3 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
				elif(task_5_3 == ""):
					task_5_3 = input("\nEnter your task: ")
					print("Task created successfully!")
					break
					list_choosen = ""
		
	#Operation: View list
		if(operation == "3"):
			list_choosen = input("\nWhat list do you want to open?\n[" + list_1_name + "]\n[" + list_2_name + "]\n[" + list_3_name + "]\n")
			if(list_choosen == "Not defined"):
				print("\nError: ListNotUsable")
				list_choosen = ""
				break
			if(list_choosen == list_1_name):
				print("1) " + task_1_1 + "\n2) " + task_2_1 + "\n3) " + task_3_1 + "\n4) " + task_4_1 + "\n5) " + task_5_1)
				break 
			if(list_choosen == list_2_name):
				print("1) " + task_1_2 + "\n2) " + task_2_2 + "\n3) " + task_3_2 + "\n4) " + task_4_2 + "\n5) " + task_5_2)
				break
			if(list_choosen == list_3_name):
				print("1) " + task_1_3 + "\n2) " + task_2_3 + "\n3) " + task_3_3 + "\n4) " + task_4_3 + "\n5) " + task_5_3)
				break

		#Operation: Delete a task
		if(operation == "4"):
			list_choosen = input("\nWhat list do you want to open?\n[" + list_1_name + "]\n[" + list_2_name + "]\n[" + list_3_name + "]\n")
			if(list_choosen == "Not defined"):
				print("\nError: ListNotUsable")
				list_choosen = ""
				break
			if(list_choosen != list_1_name or list_2_name or list_3_name):
				print("We couldn't find that list")
				break
			if(list_choosen == list_1_name):
				task_choosen = input("\nWhich task would you like to delete?\n[" + task_1_1 + "]\n[" + task_2_1 + "]\n[" + task_3_1 + "]\n[" + task_4_1 + "]\n[" + task_5_1 + "]\n")
				if(task_choosen == task_1_1):
					task_1_1 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_2_1):
					task_2_1 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_3_1):
					task_3_1 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_4_1):
					task_4_1 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_5_1):
					task_5_1 = ""
					print("Task has been deleted")
					break
			if(list_choosen == list_2_name):
				task_choosen = input("\nWhich task would you like to delete?\n[" + task_1_2 + "]\n[" + task_2_2 + "]\n[" + task_3_2 + "]\n[" + task_4_2 + "]\n[" + task_5_2 			+ "]\n")
				if(task_choosen == task_1_2):
					task_1_2 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_2_2):
					task_2_2 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_3_2):
					task_3_2 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_4_2):
					task_4_2 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_5_2):
					task_5_2 = "" 
					print("Task has been deleted")
					break
			if(list_choosen == list_3_name):
				task_choosen = input("\nWhich task would you like to delete?\n[" + task_1_3 + "]\n[" +task_2_3 + "]\n[" + task_3_3 + "]\n[" + task_4_3 + "]\n[" + task_5_3 			+ "]\n")
				if(task_choosen == task_1_3):
					task_1_3 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_2_3):
					task_2_3 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_3_3):
					task_3_3 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_4_3):
					task_4_3 = ""
					print("Task has been deleted")
					break
				if(task_choosen == task_5_3):
					task_5_3 = ""
					print("Task has been deleted")
					break
			
	#Operation: Exit
		if(operation == "5"):
			quit_option = input("Are you sure? Everything will be deleted.\nYes[y] | No [n]\n")
			if(quit_option == "y"):
				print("Deleting all tasks...")
				task_1_1 = ""
				task_2_1 = ""
				task_3_1 = ""
				task_4_1 = ""
				task_5_1 = ""
				task_1_2 = ""
				task_2_2 = ""
				task_3_2 = ""
				task_4_2 = ""
				task_5_2 = ""
				task_1_3 = ""
				task_2_3 = ""
				task_3_3 = ""
				task_4_3 = ""
				task_5_3 = ""
				print("Deleting all lists...")
				list_1_name = "Not defined"
				list_2_name = "Not defined"
				list_3_name = "Not defined"
				print("Everything has been deleted")
				print("Exiting the application...")
				operation = "6"
				break
			if(quit_option == "n"):
				print("Restoring...")
				break
