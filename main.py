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
	print("STUDENT ADMIN\n\nHow can we help you?\n1. Login\n2. Register\n3. Exit")
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
	print("REGISTRATION PORTAL\n\n**************************************\nPersonal Details:\n")
	full_name = input("Enter your name: ")

	while True:
		id_number = input("Enter your ID Number(13 digits): ")
		if id_number >= 10000000000000 or id_number <= 9999999999999:
			# username = id_number[:8]
			username = str(id_number)
			username = username[:8]
			print("Eight", username)
			password = id_number[4:]
			print("Last", password)
		else:
			print("Invalid ID Number")
			id_number = int(input("Enter your ID Number(13 digits: "))

	gender = input("Gender: 1. Male\n2. Female\n")
	if gender == "1":
		gender = "Male"
	else:
		gender == "Female"



if __name__ == "__main__":
	main()