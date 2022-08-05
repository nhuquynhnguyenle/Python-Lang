import math
from Student import Student

class Management:
        listStudent = []
        def enterStudent(self):
                name = input("Name: ")
                birthday = input("Birthday: ")
                gender = input("Gender: ")
                id = input("ID: ")
                major = input("Major: ")
                st = Student(name, birthday, id, gender, major)
                self.listStudent.append(st)
        
        def showStudentlist(self,listStudent):
                print("{:<8} {:<18} {:<8} {:<8} {:<18}".format("ID", "Name", "Birhtday", "Gender", "Major"))
                for st in listStudent:
                        print("{:<8} {:<18} {:<18} {:<8} {:<18}" .format(st.studentID, st.studentName, st.studentBirthday, st.studentGender, st.studentMajor))
                print("\n")
        def showStudentInfo(self,student):
                print("{:<8} {:<18} {:<8} {:<8} {:<18}".format("ID", "Name", "Birhtday", "Gender", "Major"))
                print("{:<8} {:<18} {:<18} {:<8} {:<18}" .format(student.studentID, student.studentName, student.studentBirthday, student.studentGender, student.studentMajor))

        def searchID(self,id):
                for st in self.listStudent:
                        if id == st.studentID:
                                return st                       

        def editStudent(self,id):
                student = self.searchID(id)
                while(1==1):
                        print("/n     What information you want to update?     /n")
                        print("1. Update student name.")
                        print("2. Update student Birthday.")
                        print("3. Update student gender.")
                        print("4. Update student major.")
                        print("5. Exit.")
                        number = int(input("Choose: "))
                        if number == 1:
                                student.studentName = input("Edit student name: ")
                        elif number == 2:
                                student.studentBirthday = input("Edit student birthday: ")
                        elif number == 3:
                                student.studentGender = input("Edit student gender: ")
                        elif number == 4:
                                student.studentMajor = input("Edit student major: ")
                        elif number == 5:
                                print("\n     Return main menu    \n")
                                break
                        else:
                                print("\nThis function is not available\n")
                                
        def deleteStudent(self,id):
                student = self.searchID(id)
                self.listStudent.remove(student)
        
        def getStudentList(self):
                return self.listStudent
