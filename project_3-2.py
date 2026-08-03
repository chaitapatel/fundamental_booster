students = []

def add_student():
    print("\n Add Student ")
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    subjects_input = input("Enter Subjects (comma separated): ")
    subjects = set()
    for subject in subjects_input.split(","):
        subjects.add(subject.strip())
    student_info = (student_id, dob)
    student = {
        "student_info": student_info,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": list(subjects)
    }
    students.append(student)
    print("\nStudent Added Successfully!\n")

def display_students():
    if len(students) == 0:
        print("\nNo Student Records Found!\n")
        return
    print("\n ALL STUDENTS ")
    for student in students:
        student_id = student["student_info"][0]
        print(f"\nStudent ID : {student_id}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Grade      : {student['grade']}")
        print(f"DOB        : {student['student_info'][1]}")
        print(f"Subjects   : {', '.join(student['subjects'])}")

def update_student():
    sid = input("\nEnter Student ID to Update: ")
    found = False
    for student in students:
        if student["student_info"][0] == sid:
            found = True
            print("\n1. Update Age")
            print("2. Update Subjects")
            choice = input("Choose Option: ")
            if choice == "1":
                student["age"] = int(input("Enter New Age: "))
                print("Age Updated Successfully!")
            elif choice == "2":
                s = set()
                for sub in input("Enter New Subjects (comma separated): ").split(","):
                    s.add(sub.strip())
                student["subjects"] = list(s)
                print("Subjects Updated Successfully!")
            else:
                print("Invalid Choice!")
            break
    if not found:
        print("Student ID Not Found!")

def delete_student():
    sid = input("\nEnter Student ID to Delete: ")
    found = False
    for i in range(len(students)):
        if students[i]["student_info"][0] == sid:
            del students[i]
            found = True
            print("Student Deleted Successfully!")
            break
    if not found:
        print("Student ID Not Found!")

def display_subjects():
    all_subjects = set()
    for student in students:
        for sub in student["subjects"]:
            all_subjects.add(sub)
    if len(all_subjects) == 0:
        print("\nNo Subjects Available!\n")
        return
    print("\n UNIQUE SUBJECTS ")
    for subject in all_subjects:
        print(subject)

def show_string_formatting_demo():
    print("\n STRING FORMATTING DEMO ")
    name = "Demo Student"
    age = 20
    print(f"F-String: Name = {name}, Age = {age}")
    print("Format Method: Name = {}, Age = {}".format(name, age))
    print("Percent Formatting: Name = %s, Age = %d" % (name, age))

print("=" * 50)
print("WELCOME TO STUDENT DATA ORGANIZER")
print("=" * 50)
show_string_formatting_demo()

while True:
    print("\n MENU ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_subjects()
    elif choice == "6":
        print("\nThank You For Using Student Data Organizer!")
        print("Good Bye!")
        break
    else:
        print("Invalid Choice! Please Try Again.")
