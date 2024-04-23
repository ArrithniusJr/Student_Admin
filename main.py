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
    # Registration page 01
    reg_01()

    # Registration page 02
    grade = reg_02()

    # Registration page 03
    reg_03(grade)

def reg_01():
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

def reg_02():
    clear()
    print("REGISTRATION PORTAL(Page 2 of 3)\n\n**************************************\nEDUCATIONAL DETAILS:\n")
    school_name = input("Where did you attend Matric(Gr12): ")
    print("\nEnter your Grade 12 Marks")
    eng = int(input("\nEnglish grades(%): "))
    h_language = int(input("\nHome Language grades(%): "))
    maths = int(input("\nMathematics grades(%): "))
    science = int(input("\nPhysical Science grades(%): "))
    l_science = int(input("\nLife Science grades(%): "))
    other_sub = int(input("\nOther Subjects grades(%): "))
    other_sub2 = int(input("\nOther Subjects grades(%): "))

    avg = ((eng + h_language + maths + science + l_science + other_sub + other_sub2) / 7)

    return avg

def reg_03(avg):
    clear()
    print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nQUALIFICATION DETAILS:\n")
    course_sel = int(input("Select a course to register:\n1. Bachelor of Science [B.Sc] (Computer Science)\n2. Bachelor of Science [B.Sc] (Mathematics)\n3. Bachelor of Science [B.Sc] (Zoology)\n4. Bachelor of Science [B.Sc] (Botany)\n5. Bachelor of Science [B.Sc] (Biotechnology)\n6. Bachelor of Science [B.Sc] (Microbiology)\n7. Bachelor of Science [B.Sc] (Information Technology)\n8. Bachelor of Science [B.Sc]\n9. Bachelor of Science [B.Sc] Hons. (Mathematics)\n10. Bachelor of Science [B.Sc] Hons (Chemistry)\n11. Bachelor of Science [B.Sc] Hons (Physics)\n12. Bachelor of Science [B.Sc] (Statistics)\n14. Bachelor of Science [B.Sc] (Electronics)\n15. Bachelor of Science [B.Sc] Hons (Zoology)\n16. Exit"))

    match course_sel:
        case 1:
            course_name = "Bachelor of Science in Computer Science"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 60%. \n\nOVERVIEW: BSc Computer Science deals with the theoretical knowledge and skills in the field of computer science and its applications in the real world for various uses."
            modules = "\n\nMODULES:\n- Basics of Computer Science\n- Object-Oriented programming using C++\n- Introduction to Data Structure\n- Database Management\n- Python Programming\n- Introduction of Software Engineering\n- Mobile Application Development\n- Programming with Java"

            if avg >= 60:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registred for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
                else:
                    reg_03(avg)
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 2:
            course_name = "Bachelor of Science in Mathematics"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 55%. \n\nOVERVIEW: BSc Mathematics provides a comprehensive understanding of mathematical theories and their practical applications in various fields."
            modules = "\n\nMODULES:\n- Calculus\n- Algebra\n- Differential Equations\n- Probability and Statistics\n- Numerical Methods\n- Linear Algebra\n- Real Analysis\n- Complex Analysis"

            if avg >= 55:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registred for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 3:
            course_name = "Bachelor of Science in Zoology"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 58%. \n\nOVERVIEW: BSc Zoology focuses on the study of animals, their behavior, physiology, and interactions with ecosystems."
            modules = "\n\nMODULES:\n- Introduction to Zoology\n- Animal Physiology\n- Evolutionary Biology\n- Ecology\n- Genetics\n- Animal Behavior\n- Comparative Anatomy\n- Conservation Biology"

            if avg >= 58:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registred for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 4:
            course_name = "Bachelor of Science in Botany"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 56%. \n\nOVERVIEW: BSc Botany focuses on the study of plants, their structure, function, growth, evolution, and their relationships with other organisms and the environment."
            modules = "\n\nMODULES:\n- Plant Anatomy\n- Plant Physiology\n- Plant Taxonomy\n- Plant Ecology\n- Plant Biotechnology\n- Economic Botany\n- Medicinal Plants\n- Plant Pathology"

            if avg >= 56:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registred for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 5:
            course_name = "Bachelor of Science in Biotechnology"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 62%. \n\nOVERVIEW: BSc Biotechnology integrates biology and technology to create products and technologies aimed at improving human life and the environment."
            modules = "\n\nMODULES:\n- Cell Biology\n- Genetics\n- Molecular Biology\n- Bioinformatics\n- Bioprocess Engineering\n- Immunology\n- Biomedical Engineering\n- Environmental Biotechnology"

            if avg >= 62:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registred for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 6:
            course_name = "Bachelor of Science in Microbiology"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 60%. \n\nOVERVIEW: BSc Microbiology focuses on the study of microorganisms such as bacteria, viruses, fungi, and parasites, and their impact on human health, agriculture, and the environment."
            modules = "\n\nMODULES:\n- Microbial Physiology\n- Medical Microbiology\n- Environmental Microbiology\n- Industrial Microbiology\n- Immunology\n- Virology\n- Microbial Genetics\n- Food Microbiology"

            if avg >= 60:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registred for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 7:
            course_name = "Bachelor of Science in Information Technology"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 65%. \n\nOVERVIEW: BSc Information Technology focuses on the study of computer-based information systems and their application in real-world scenarios."
            modules = "\n\nMODULES:\n- Introduction to Information Technology\n- Database Management Systems\n- Web Development\n- Network Administration\n- Cybersecurity\n- Software Engineering\n- Mobile Application Development\n- Cloud Computing"

            if avg >= 65:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registered for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 8:
            course_name = "Bachelor of Science"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 50%. \n\nOVERVIEW: BSc is a general degree program offering a broad range of subjects across various disciplines in science."
            modules = "\n\nMODULES:\n- Mathematics\n- Physics\n- Chemistry\n- Biology\n- Environmental Science\n- Statistics\n- Computer Science\n- Elective Courses"

            if avg >= 50:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister for this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registered for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)

        case 9:
            course_name = "Bachelor of Science Hons. in Mathematics"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science Honours)\n\nDURATION: 4 years\n\nREQUIREMENT: Any candidate with NQF level 5 and a total of 70%. \n\nOVERVIEW: BSc Hons. Mathematics offers an advanced study of mathematical theories and their applications."
            modules = "\n\nMODULES:\n- Advanced Calculus\n- Abstract Algebra\n- Differential Geometry\n- Mathematical Analysis\n- Number Theory\n- Topology\n- Mathematical Modeling\n- Elective Courses"

            if avg >= 70:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister for this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registered for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 10:
            course_name = "Bachelor of Science Hons. in Chemistry"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science Honours)\n\nDURATION: 4 years\n\nREQUIREMENT: Any candidate with NQF level 5 and a total of 68%. \n\nOVERVIEW: BSc Hons. Chemistry offers an in-depth study of chemical principles, reactions, and their applications."
            modules = "\n\nMODULES:\n- Organic Chemistry\n- Inorganic Chemistry\n- Physical Chemistry\n- Analytical Chemistry\n- Biochemistry\n- Polymer Chemistry\n- Environmental Chemistry\n- Industrial Chemistry"

            if avg >= 68:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister for this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registered for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 11:
            course_name = "Bachelor of Science Hons. in Physics"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science Honours)\n\nDURATION: 4 years\n\nREQUIREMENT: Any candidate with NQF level 5 and a total of 72%. \n\nOVERVIEW: BSc Hons. Physics offers advanced study in various branches of physics, including classical mechanics, electromagnetism, quantum mechanics, and relativity."
            modules = "\n\nMODULES:\n- Classical Mechanics\n- Electromagnetism\n- Quantum Mechanics\n- Thermodynamics\n- Statistical Mechanics\n- Astrophysics\n- Nuclear Physics\n- Solid State Physics"

            if avg >= 72:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister for this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registered for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 12:
            course_name = "Bachelor of Science in Statistics"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 60%. \n\nOVERVIEW: BSc Statistics focuses on the collection, analysis, interpretation, and presentation of data."
            modules = "\n\nMODULES:\n- Probability Theory\n- Statistical Inference\n- Regression Analysis\n- Time Series Analysis\n- Multivariate Analysis\n- Experimental Design\n- Statistical Computing\n- Data Visualization"

            if avg >= 60:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister for this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registered for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 13:
            course_name = "Bachelor of Science in Environmental Science"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 58%. \n\nOVERVIEW: BSc Environmental Science focuses on the study of the environment and solutions to environmental issues."
            modules = "\n\nMODULES:\n- Environmental Chemistry\n- Ecology\n- Environmental Policy\n- Climate Change\n- Sustainability\n- Conservation Biology\n- Environmental Impact Assessment\n- Waste Management"

            if avg >= 58:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister for this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registered for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 14:
            course_name = "Bachelor of Science in Electronics"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science)\n\nDURATION: 3 years\n\nREQUIREMENT: Any candidate with NQF level 4 and a total of 62%. \n\nOVERVIEW: BSc Electronics focuses on the study of electronic circuits, devices, and systems."
            modules = "\n\nMODULES:\n- Circuit Analysis\n- Digital Electronics\n- Analog Electronics\n- Semiconductor Devices\n- Microcontrollers\n- Communication Systems\n- Power Electronics\n- Embedded Systems"

            if avg >= 62:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister for this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registered for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 15:
            course_name = "Bachelor of Science Hons. in Zoology"
            overview = "\nDEGREE: Undergraduate (Bachelor of Science Honours)\n\nDURATION: 4 years\n\nREQUIREMENT: Any candidate with NQF level 5 and a total of 64%. \n\nOVERVIEW: BSc Hons. Zoology offers advanced study in the field of zoology, including the study of animal behavior, physiology, ecology, and evolution."
            modules = "\n\nMODULES:\n- Advanced Zoology\n- Animal Behavior\n- Comparative Anatomy\n- Evolutionary Biology\n- Conservation Biology\n- Marine Biology\n- Entomology\n- Field Research"

            if avg >= 64:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                course_selection = int(input("\nRegister for this course?\n1. Yes\n2. No\n"))
                if course_selection == 1:
                    clear()
                    print("**************************************\nYou have Successfully registered for\n" + course_name + "\n**************************************")
                    enter = input("\nClick Enter To Continue")
                    main()
            else:
                clear()
                print("REGISTRATION PORTAL(Page 3 of 3)\n\n**************************************\nYou have selected:\n" + course_name + "\n" + overview + " " + modules)
                print("\nYou DO NOT QUALIFY for this course")
                enter = input("\nClick ENTER To Continue")
                reg_03(avg)
        case 16:
            exit()
        case _:
            print("Invalid input")

if __name__ == "__main__":
    main()