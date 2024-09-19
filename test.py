
#For question 5
print("This is for Question No.5")
print("The functions are called and tested in question no.6")

#the function used to get the number of students and their marks
def get_marks():
    student_number = int(input("Enter the numbers of student"))
    mark_list = []
    if student_number > 0:
        for x in range(student_number):
            mark = int(input("Enter the mark of the student"))
            if mark < 0 or mark > 100:
                print("Enter valid mark")
                mark_list.append(int(input("Enter the mark of the student")))
            else:
                mark_list.append(mark)
        return mark_list
    else:
        print("The number of students must be greater than 0")

# Function to get the total marks of the students
def total(marks):
    total_mark = 0
    for x in marks:
        total_mark += x
    return total_mark

#function to get the average marks of the students

def average(marks):
    total_mark = 0
    number_of_students= len(marks)
    for mark in marks:
        total_mark += mark
    return total_mark/number_of_students

#function to get the number of passed students

def passed(marks):
    number_of_passed_student=[]
    for mark in marks:
        if mark >= 50:
            number_of_passed_student.append(mark)
    return len(number_of_passed_student)

#function to get the number of failed students

def failed(marks):
    number_of_failed_students=[]
    for mark in marks:
        if mark <50:
            number_of_failed_students.append(mark)
    return len(number_of_failed_students)

#function to find the max number in a list

def max_num(marks):
    maximum_number = marks[0]
    for mark in marks:
        if mark > maximum_number:
            maximum_number = mark
    return maximum_number

#function to find the min number in a list

def min_num(marks):
    minimum_number = marks[0]
    for mark in marks:
        if mark < minimum_number:
            minimum_number = mark
    return minimum_number


#For question 6
print("This is for Question No.6")
def get_choice():
    data_empty = 1
    while True:
        print()
        print()
        print("""Choose from 1 to 9 
1. To input sudent marks
2. To display the number of students
3. To display Total score
4. To display Average score
5. To display Maximum score
6. To display Minimum score
7. To display Number of student who Passed the exam
8. To display Number of student who Failed the exam
9. To Exit program""")
        print()
        choice = int(input("Choose form the above option"))
        if 1 < choice < 9 and data_empty ==1:   #to ensure the students marks are entered first
            print("You need to enter the students marks first")
        elif choice == 1 and data_empty == 1:  #to input the marks of the students
            data_empty = 0
            mark_list = get_marks()
            print()
            print(f"The marks of the students{mark_list}")
        elif choice == 1 and data_empty == 0: #not to input the data again
            print()
            print("The data already exists")
        elif 1 < choice < 9 and data_empty == 0: #to ensure the input is between 1 and 9 and the data is not empty
            if choice == 2:
                print()
                print(f"The total number of students: {len(mark_list)}")
            elif choice == 3:
                print()
                print(f"The total scores of the students: {total(mark_list)}")
            elif choice == 4:
                print()
                print(f"The average score {average(mark_list)}")
            elif choice == 5:
                print()
                print(f"The maximum mark is {max_num(mark_list)}")
            elif choice == 6:
                print()
                print(f"The minimum mark is {min_num(mark_list)}")
            elif choice == 7:
                print ()
                print(f"The number of passed students {passed(mark_list)}")
            elif choice == 8:
                print()
                print(f"The number of failed students {failed(mark_list)}")
            else:
                print("Invalid input")
        elif choice == 9: #to exit the loop
            print()
            print("Thank you!")
            break
        else: #for selection less than 1 and greater then 9
            print()
            print("Invalid choice, pls select between 1 to 9")
get_choice()