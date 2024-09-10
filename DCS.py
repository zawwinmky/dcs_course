# for counter in range(11):
#     print("*");

# list=[10,20,30,40]
# for i in list:
#     print("Number", i);


# num1=int(input("Enter for number one"));
# num2=int(input("Enter for number two"));
# sum=num1 + num2;
# print("The sum of", num1, "and", num2, "is", sum);

#
# length=int(input("Enter length"))
# width=int(input("Enter width"))
# area = length * width
# print("The area of the rectangle is", area)
#
# import sys
# a="hello world"
# print(sys.getsizeof(a))
#
# b="Hello"
# c="World"
# d="This is", b, c
# print(d)
#
# print(type(d))
# e=f'{b} {c}'
# print(e)
# print(type(e))
#
# example_set={20,13,24,15,16,1,3,"Hello",False,"Hi","Happy","Hemmo","Happi",True}
# print(example_set)
#
# example_set.remove(False)
#
# print(example_set)
#
# print(sys.getsizeof(int(24)))
# print(sys.getsizeof("Hi"))
#
# print(d[2])

#
# my_set={1,3,2,5,10,20,60,40,30,7,4,5}
# print(my_set)
# # frozen_set=frozenset(my_set)
# # print(frozen_set)
# #
# # for i in frozen_set:
# #     print(i)
# #
# # import  sys
# # for i in range(10,100,10):
# #     print("This is ", i, hex(id(i)), sys.getsizeof(i))
#
# dictionary_list={"name":"Mg Mg","age":21,"is student":True}
#
# print(dictionary_list.get("is student"))
#
# dictionary_list.values()
#
# a=[1,2,3,4,5]
# a.extend(("Hello",4,5,6))
# print(a)
#
# a.insert(1,"Hello")
# print(a)
#
# a.append(10)
# print(a)
#
# a.insert(len(a),"Hey")
#
# print(a)
#
# a.pop(7)
#
# print(a)
#
# b=a.count("Hello")
# # del a[:]
# # a.clear()
# print(a.count(5))
# print(len(a))
# print(a.index("Hello",2,len(a)))
#
# blist=['a','b','c','d','e','f']
# del blist[1]
# print(blist)

# print(0.1 + 0.2 == 0.3)
# print(True ^ True)
#
# x=0
#
# if x<60:
#     x=x+1
#     y=x
#     print(y)
# else:
#     print("done")
#
# x=int(input("Enter test score"))
#
# if x>79 and x<=100:
#     print("Grade A")
# elif x>69 and x<80:
#     print("Grade B")
# elif x>59 and x<70:
#     print("Grade C")
# elif x>49 and x<60:
#     print("Grade D")
# elif x>0 and x<50:
#     print("Grade E")
# else:
#     print("Invalid marks")

#For question 1
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
result = num1 + num2
print("The sum of ", num1, "and", num2, "is", result )

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

