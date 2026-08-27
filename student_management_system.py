students = []

student1 = {
    'id': 23,
    'name': 'jerry',
    'age': 20,
    'course': 'maths',
    'marks': 89
}

student2 = {
    'id': 67,
    'name': 'joan',
    'age': 20,
    'course': 'politics',
    'marks': 87
}

student3 = {
    'id': 98,
    'name': 'maria',
    'age': 21,
    'course': 'science',
    'marks': 96
}

students.extend([student1, student2, student3])

while True:

    print("\n--- Student Management System ---")
    print("1.Add")
    print("2.View")
    print("3.Search")
    print("4.Update")
    print("5.Delete")
    print("6.Exit")

    choice = int(input("Enter your choice:"))

    # add
    if choice == 1:

        student = {
            "id": int(input("Enter ID: ")),
            "name": input("Enter name: "),
            "age": int(input("Enter age: ")),
            "course": input("Enter course: "),
            "marks": int(input("Enter marks: "))
        }

        students.append(student)

        print("Student added successfully!")

    # view
    elif choice == 2:

        for student in students:

            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            print()

    # search
    elif choice == 3:

        search_id = int(input("enter the student id to search:"))

        found = False

        for student in students:

            if student["id"] == search_id:

                print(student)

                found = True
                break

        if found == False:

            print("Student not found!")

    # update
    elif choice == 4:

        search_id = int(input("enter the student id to update:"))

        found = False

        for student in students:

            if student["id"] == search_id:

                new_id = int(input("Enter new id:"))
                new_name = input("enter new name:")
                new_age = int(input("enter new age:"))
                new_course = input("enter new course:")
                new_mark = int(input("enter a mark:"))

                student["id"] = new_id
                student["name"] = new_name
                student["age"] = new_age
                student["course"] = new_course
                student["marks"] = new_mark

                print("updated")

                found = True
                break

        if found == False:

            print("Student not found")

    # delete
    elif choice == 5:

        search_id = int(input("enter the student id to delete:"))

        found = False

        for student in students:

            if student["id"] == search_id:

                students.remove(student)

                print("Student data deleted")

                found = True
                break

        if found == False:

            print("Student id not found!")

    # exit
    elif choice == 6:

        print("Exit")
        break

    else:

        print("Invalid choice")







