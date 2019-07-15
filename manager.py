import os
import platform

global listStd
#Making ListStd As Super Global Variable

listStd = ["Linh","My","Xuyen","Loan"]
#List of students

#Function for the student manager system
def manageStudent():
    x = "#"*30
    y = "="*28
    global bye 
    #Making Bye As Super Global Variable
    bye = "\n {}\n# {} #\n# ===> Brought To You By <===  #\n# ===> code-projects.org <===  #\n# {} #\n {}".format(x, y, y, x) 
    # Will Print GoodBye Message

    #Print welcome message and options for this program
    print("""WELCOME TO STUDENT MANAGEMENT SYSTEM
Enter 1: To view student's list
Enter 2: To add new student
Enter 3: To search student
Enter 4: To remove student
    """)

    #using exceptions for validation
    try:
        userInput = int(input("Please select an above option:"))
        #will take input from user
    except ValueError:
        exit("\nHi! That's not a number")
        #Error message
    else:
        print("\n")
        #print new line
    
    #Check using option
    #This option will print list of students
    if(userInput ==1):
        print("List Students\n")
        for students in listStd:
            print("=>{}".format(students))

    #This option will add new student in the list
    elif(userInput == 2):
        newStd = input("Enter new student:")
        #This condition checking the new student is already in list or not
        if(newStd in listStd):
            print("\nThis student {} already in the database".format(newStd))
            #Error message
        else:
            listStd.append(newStd)
            print("\n=>New Student {} successfully add\n".format(newStd))
            for students in listStd:
                print("=> {}".format(students))
                
    #This option will search student from the list
    elif(userInput == 3):
        srcStd = input("Enter student name to search:")
        #this condition searching the student
        if(srcStd in listStd):
            print("\n=>Record found of student {}".format(srcStd))
        else:
            print("\n=>No record found of student {}".format(srcStd))
            #error message

    #this option will remove student from the list
    elif(userInput == 4):
        rmStd = input("Enter student name to remove:")
        #this condition removing the student from the list
        if(rmStd in listStd):
            listStd.remove(rmStd)
            print("\n=>Student {} successfully deleted\n".format(rmStd))
            for students in listStd:
                print("=> {}".format(students))
        else:
            print("\n=>No record found of this student {}".format(rmStd))
            #error message
    
    #Validating user option
    elif(userInput < 1 or userInput >4):
        print("Please enter valid option")
        #error message

manageStudent()

def runAgain():
    runAgn = input("\nwant to run again y/n:")
    if(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        manageStudent()
        runAgain()
    else:
        quit(bye)

runAgain()



	





    
