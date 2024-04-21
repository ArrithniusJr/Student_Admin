import os, platform

# clear screen/terminal
def clear():
	if platform.system == "Windows":
		os.system("cls")
	else:
		os.system("clear")

# the main method
def main():
	clear()
	print("STUDENT ADMIN(Sciences)\n\nHow can we help you?\n1. Login\n2. Register\n3. Exit")
	menu_option = int(input("\nChoose from options: "))
	if menu_option == 1:
		# clear screen here
		# open login page
		login()
	elif menu_option == 2:
		# clear, log register
		register()
	elif menu_option == 3:
		exit()
	else:
		print("Invalid input")

# login
def login():
	"""
		Create a login function which a user will enter their details and will be verified on the file, 
		if user does not exist then take a user to the registration function.
	"""

# registration
def register():
	"""
		_Create a register function which will take Full names of the user and also an ID number.
		_The system will generate the username by taking the first 8 digits of the ID number, and 
		    will generate a pin or password by taking the last 4 digits of the ID number.
		_Verify if the user already exist, if not then save new user.
	"""
	clear()
	print("REGISTRATION PORTAL(Page 1 of 3)\n\n**************************************\nPERSONAL DETAILS:\n")
	first_name = input("Enter your name: ")
	last_name = input("Enter your last name: ")

	id_number = int(input("Enter your ID Number(13 digits): "))
	phone_number = int(input("Enter your Phone Numbers(10 digits): "))
	while True:
		if id_number >= 1000000000000 and id_number <= 9999999999999:
			username = str(id_number)[:8]
			password = str(id_number)[-4:]
			break
		else:
			id_number = int(input("Invalid ID Number, Please enter your ID Number(13 digits): "))

		if phone_number >= 1000000000 and phone_number <= 9999999999:
			phone_number = str(phone_number)
		else:
			phone_number = int(input("Invalid Phone Numbers, re-enter(10 digits): "))

	gender = input("Gender:\n1. Male\n2. Female\n")
	if gender == "1":
		gender = "Male"
	else:
		gender = "Female"

	eth_group = input("Ethnic Group:\n1. Black\n2. White\n3. Indian\n4. Coloured\n")
	if eth_group == "1":
		eth_group = "Black"
	elif eth_group == "2":
		eth_group = "White"
	elif eth_group == "3":
		eth_group = "Indian"
	else:
		eth_group = "Coloured"

	clear()
	print("REGISTRATION PORTAL(Page 2 of 3)\n\n**************************************\nEDUCATINAL DETAILS:\n")
	school_name = input("Where did you attend Matric(Gr12): ")
	print("\nEnter your Grade 12 Marks")
	eng = int(input("\nEnglish grades(%): "))
	h_language = int(input("\nHome Language grades(%): "))
	maths = int(input("\nMathematics grades(%): "))
	science = int(input("\nPhysical Science grades(%): "))
	l_science = int(input("\nLife Science grades(%): "))
	other_sub = int(input("\nOther Subjects grades(%): "))
	other_sub2 = int(input("\nOther Subjects grades(%): "))

	avr = (((eng + h_language + maths + science + l_science + other_sub + other_sub2) / 7) * 100)

	clear()
	print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nQUALIFICATION DETAILS:\n")
	course_sel = int(input("Select a course to register:\n1. Bachelor of Science [B.Sc] (Computer Science)\n2. Bachelor of Science [B.Sc] (Mathematics)\n3. Bachelor of Science [B.Sc] (Zoology)\n4. Bachelor of Science [B.Sc] (Botany)\n5. Bachelor of Science [B.Sc] (Biotechnology)\n6. Bachelor of Science [B.Sc] (Microbiology)\n7. Bachelor of Science [B.Sc] (Information Technology)\n8. Bachelor of Science [B.Sc]\n9. Bachelor of Science [B.Sc] Hons. (Mathematics)\n10. Bachelor of Science [B.Sc] Hons (Chemistry)\n11. Bachelor of Science [B.Sc] Hons (Physics)\n12. Bachelor of Science [B.Sc] (Statistics)\n14. Bachelor of Science [B.Sc] (Electronics)\n15. Bachelor of Science [B.Sc] Hons (Zoology)\n"))

	if course_sel == 1:
		course_name = "Bachelor of Science in Computer Science"
		overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 60%. \n\nOVERVIEW: BSc Computer Science deals with the theoretical knowledge and skills in the field of computer science and its applications in the real world for various uses."
		modules = "\n\nMODULES:\n- Basics of Computer Science\n- Object-Oriented programming using C++\n- Introduction to Data Structure\n- Database Management\n- Python Programming\n- Introduction of Software Engineering\n- Mobile Application Development\n- Programming with Java"

		if avr >= 60:
			clear()
			print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
			course_selection = int(input("\nRegister this course?\n1. Yes\n2. No\n"))
			if course_selection == 1:
				clear()
				print("**************************************\nYou have Successfully registred for\n" + course_name + "\n**************************************")
				enter = input("\nClick enter to continue")
				if enter == '':
					main()

	elif course_sel == 2:
		# Course 2
		pass

	elif course_sel == 3:
		# Course 3
		pass

	elif course_sel == 4:
		# Course 4
		pass

	elif course_sel == 5:
		# Course 5
		pass

	elif course_sel == 6:
		# Course 6
		pass

	elif course_sel == 7:
		# Course 7
		pass

	elif course_sel == 8:
		# course 8
		pass

	elif course_sel == 9:
		# Course 9
		pass

	elif course_sel == 10:
		# Course 10
		pass

	elif course_sel == 11:
		# Course 11
		pass

	elif course_sel == 12:
		# Course 12
		pass

	elif course_sel == 13:
		# Course 13 
		pass

	elif course_sel == 14:
		# Course 14
		pass

	elif course_sel == 15:
		# Course 15
		pass


if __name__ == "__main__":
	main()