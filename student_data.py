student= {

}
def  add_student(student):
    roll=input("Enter roll no of student: ")
    if roll in student:
        print("Roll no already exists")
    else:
        student[roll]={}
        name = input("Enter name of the student: ")
        student[roll]["name"]=name
        age = int(input("Enter age of the student: "))
        while age<=0 :
            print("Age should be greater than 0")
            age = int(input("Enter age of the student: "))
        student[roll]["age"]=age
        
        marks = int(input("Enter marks of the student: "))
        while not ( marks>=0 and marks<=100):
            print("Marks should be in range 0 to 100")
            marks = int(input("Enter marks of the student: "))
        student[roll]["marks"]=marks
        
    
def display(student):
    if len(student) == 0:
        print("The dictionary is empty!")
    else:
        for stud in student:
            print(f"Roll_no:",stud)
            print(f"Name:",student[stud]["name"])
            print(f"Age:",student[stud]["age"])
            print(f"Marks:",student[stud]["marks"])

def search_student(student,roll_no):
    print(f"Roll_no:",roll_no)
    print(f"Name:",student[roll_no]["name"])
    print(f"Age:",student[roll_no]["age"]) 
    print(f"Marks:",student[roll_no]["marks"])

def update_marks(student, roll_no):
    marks= int(input("Enter marks to update: "))
    while not ( marks>=0 and marks<=100):
        print("Marks should be in range 0 to 100")
        marks = int(input("Enter marks of the student: "))
    student[roll_no]["marks"]=marks
    search_student(student,roll_no)

def delete_student(student, roll_no):
    del student[roll_no]
    display(student)
while True:
    print("-------------MENU-------------")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Enter 6 to Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
       add_student(student)
    elif choice == "2":
         display(student)
    elif choice == "3":
        roll_no =input("Enter student roll no to search: ")
        if roll_no in student:
            search_student(student,roll_no)
        else:
            print("Roll no does not exist")
    elif choice == "4":
        roll_no =input("Enter student roll no to update marks: ")
        if roll_no in student:
            update_marks(student, roll_no)
        else:
            print("Roll no does not exist")
    elif choice == "5":
        roll_no =input("Enter student roll no to delete student: ")
        if roll_no in student:
            delete_student(student, roll_no)
        else:
            print("Roll no does not exist")
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

