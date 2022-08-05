from Management import Management
m = Management()
def printMenu():
    print("-----------------------------------------------------")
    print("               STUDENT MANAGEMENT                    ")
    print("-----------------------------------------------------")
    print("1. Add a new student.")
    print("2. Edit the information of a student by ID.")
    print("3. Search the information of a student by ID.")
    print("4. Delete the information of a student by ID.")
    print("5. List the information of all student.")
    print("6. Sort student by ID")
    print("7. Exit.")
    number = int(input("Enter number: "))
    return number

def main():
    while(1==1):
        number = printMenu()
        if number == 1:
            m.enterStudent()
        elif number == 2:
            id = input("\nEnter Student ID: ")
            m.editStudent(id)
        elif number == 3:
            id = input("\nEnter Student ID: ")
            m.showStudentInfo(m.searchID(id))
        elif number == 4:
            temp = input("\nEnter Student ID: ")
            m.deleteStudent(temp)
        elif number == 5:  
            m.showStudentlist(m.getStudentList())
        elif number == 7:
            print("\n     SEE YOU AGAIN!!!     \n")
            break
        else:
            print("\nThere is has no this function!\n")
    
main()

