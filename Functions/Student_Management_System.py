import json

# Add Student

student_detail = {}

def Add_Student():
    Stu_Roll = int(input("Enter Student Roll no :"))
    Student_Name = input("Enter Student Name :")

    student_detail['Roll No'] = Stu_Roll
    student_detail['Name'] = Student_Name

    # Save Detail in json file

    with open("Students.json","w") as file:
        json.dump(student_detail, file)

# Show Student

def Show_Student():
    for key,value in student_detail.items():
        print(f"{key} : {value}")


Add_Student()
Show_Student()



