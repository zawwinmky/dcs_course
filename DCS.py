#For question 1
# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# result = num1 + num2
# print("The sum of ", num1, "and", num2, "is", result )
#
# #For question 2
# mark_1 = int(input("Enter first mark"))
# mark_2 = int(input("Enter second mark"))
# mark_3 = int(input("Enter third mark"))
# final_mark = mark_1 + mark_2 + mark_3
# if final_mark >= 50:
#     print("Pass")
# elif final_mark <0:
#     print("Invalid mark")
# else:
#     print("Fail")
#
# #For question 3
# first_number = float(input("Enter the first number"))
# second_number = float(input("Enter the second number"))
# if first_number > second_number :
#     print("The first number is larger than the second number")
# else:
#     print("The second number is larger than the first number")
from dis import disco
#For question 4
from itertools import count
#
# for i in range(10):
#     print("Welcome to DCS")
#
#
# #For question 5
# ticket_number=int(input("Enter the numbers of tickets"))
# ticket_price=20
#
# if ticket_number > 25 :
#     print("You cannot buy 25 tickets in a single transaction")
# elif ticket_number >= 20:
#     discount =0.8
#     total_price = ticket_number * ticket_price * discount
#     print("The total cost for", ticket_number, "tickets is", total_price, "USD")
# elif ticket_number >=10 :
#     discount=0.9
#     total_price = ticket_number * ticket_price * discount
#     print("The total cost for", ticket_number, "tickets is", total_price, "USD")
# elif ticket_number >0 :
#     total_price = ticket_number * ticket_price
#     print("The total cost for", ticket_number, "tickets is", total_price, "USD")
# else:
#     print("Invalid ticket numbers")

#For question 6

# number=0
# while number <3:
#     num_1=float(input("Enter first number"))
#     num_2=float(input("Enter second number"))
#     print("The result is:", num_1 * num_2)
#     number += 1

#For question 7

mark = int(input("Enter your marks"))
if mark < 0 or mark > 100:
    print("Invalid marks")
elif mark >=75 :
    print("Pass with credit")
elif mark >=40:
    print("Pass without credit")
else:
    print("Fail")