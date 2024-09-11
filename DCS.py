# DCS 146 (SSM-16042) Assignment

# For question 1
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")

#For question 2
mark_1 = int(input("Enter first mark"))
mark_2 = int(input("Enter second mark"))
mark_3 = int(input("Enter third mark"))
final_mark = mark_1 + mark_2 + mark_3
if final_mark >= 50:
    print("Pass")
elif final_mark <0:
    print("Invalid mark")
else:
    print("Fail")

#For question 3
first_number = float(input("Enter the first number"))
second_number = float(input("Enter the second number"))
if first_number > second_number :
    print("The first number is larger than the second number")
elif first_number == second_number:
    print("They are the same")
else:
    print("The second number is larger than the first number")


#For question 4

from dis import disco
from itertools import count

for i in range(10):
    print("Welcome to DCS")


#For question 5
ticket_number=int(input("Enter the numbers of tickets"))
ticket_price=20

if ticket_number > 25 :
    print("You cannot buy 25 tickets in a single transaction")
elif ticket_number >= 20:
    discount =0.8
    total_price = ticket_number * ticket_price * discount
    print("The total cost for", ticket_number, "tickets is", total_price, "USD")
elif ticket_number >=10 :
    discount=0.9
    total_price = ticket_number * ticket_price * discount
    print("The total cost for", ticket_number, "tickets is", total_price, "USD")
elif ticket_number >0 :
    total_price = ticket_number * ticket_price
    print("The total cost for", ticket_number, "tickets is", total_price, "USD")
else:
    print("Invalid ticket numbers")

#For question 6
number = 0
while number < 3 :
    num_1=float(input("Enter first number"))
    num_2=float(input("Enter second number"))
    print("The result is:", num_1 * num_2)
    number += 1

#For question 7
mark = int(input("Enter your marks"))
if mark < 0 or mark > 100 :
    print("Invalid marks")
elif mark >=75 :
    print("Pass with credit")
elif mark >=40:
    print("Pass without credit")
else:
    print("Fail")


#For question 8
count = 0
result = 0
while count < 10:
    number = int(input("Enter your number"))
    result += number
    count += 1
print("The result is", result)



#For question 10
bill_amount=float(input("Enter your bill amount"))

if bill_amount > 200 :
    print("You need to pay using credit card")
else:
    print("You can pay with cash")

#For question 9

number_of_diners=int(input("Enter the number of dinners"))
amount_of_bill=float(input("Enter the amount of bill "))

if number_of_diners < 1 or number_of_diners > 12:
    print("Number of dinners must be between 1 and 12")
elif amount_of_bill < 10 or amount_of_bill > 500:
    print("Amount of bill must be between 10 and 500 USD")
else:
    cost_per_person= amount_of_bill / number_of_diners
    print(f"The average cost for one person is {cost_per_person}USD")