##### DCS-146 (SSM-16042)


# For Question 1
def triangle_area (h,w):
    triangle = 0.5 * h * w
    return triangle

height = float(input("Enter height"))
width = float(input("Enter width"))

print(f"Triangle Area is {triangle_area(height,width)}")

#For Question 2
import math

def get_radius():
    return float(input("Enter the radius of the circle"))

def circle_area(r):
    return math.pi * r ** 2

radius = get_radius()
result = circle_area(radius)

print(f"The area of the circle is {result}")


#Question 3

def total_score(scores):
    total = 0
    for score in scores:
        total += score
    return total

scores_list=[10,20,30,40,50]

total_result = total_score(scores_list)
average = total_result / len(scores_list)
print(f"The total is {total_result} and the average is {average}")



#For question 4

def score_list():
    list = []
    for x in range(5):
        list.append(int(input("Enter score")))
    return list
def total_score(scores):
    total = 0
    for score in scores:
        total += score
    return total
print("The total score is ", total_score(score_list()))


#For question 5

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

mark_list = get_marks()
print("The marks of the students:", mark_list)
print("The sum of the marks", total(mark_list))
print("The average mark of the student is", average(mark_list))
print("The number of passed students", passed(mark_list))
print("The number of failed students", failed(mark_list))
print("The max num in", mark_list, "is", max_num(mark_list))
print("The min num in", mark_list, "is", min_num(mark_list))

#For question 6
def get_choice():
    while True:
        choice = int(input("""Choose from 1 to 9 
1. To input sudent marks
3. To display Total score
2.To display the number of students
4. To display Average score
5. To display Maximum score
6. To display Minimum score
7. To display Number of student who Passed the exam
8. To display Number of student who Failed the exam
9. Exit program"""))
        
        if choice == 1:
            print(f"The marks of the students: {get_marks()}")
        elif choice == 2:
            print("Something")
        elif choice == 3:
            print("Something")
        elif choice == 4:
            print("Something")
        elif choice == 5:
            print("Something")
        elif choice == 4:
            print("Something")
        elif choice == 6:
            print("Something")
        elif choice == 7:
            print("Something")
        elif choice == 8:
            print("Something")
        elif choice == 9:
            break
get_choice()