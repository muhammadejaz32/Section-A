# #  class 1 Section A
# a = 5;
# print(a)

# print(type(a))
# b= 2.0;
# print(type(b),b)

# c,d,e = 1,6,9
# print(c)

# name = "  ahmad  ";
# print(name)
# print(name[2])
# print(name[0:4])
# print(name.upper())
# print(len(name))
# print(name.strip())
# print(len(name.strip()))
# print(name[:3])
# print(name[1:])

# r_no = '1'
# print(type(r_no))
# z = int(r_no)
# print(type(z),z)
# c  =float(z)
# print(type(c),c)


# if a>5:
#     print(a)
# else:
#     print(5)




# p =5;
# l =4
# print('operator')
# print(p+l)
# print(p-l)
# print(p*l)
# print(p**l)
# print(p/l)
# print(p//l)

# a = 5
# b = 4
# a //= 6;
#   a = a-6

# print(a)

# print(5>4)
# print(a!=b)

# print(a>b or a<b)


# #  class 2 Section A



# list1 = [1,"ahamd","section a", 9.0]
# print(list1)
# print(list1[2])
# print(list1[-3])
# print(list1[1:3])
# print(list1[:5])
# print(list1[1:])
# print(list1[:])
# print(list1[-1:-6:-1])

# list1.insert(3, "SE")
# print(list1)
# list1.append("nothing")
# print(list1)
# print(len(list1))
# list1.pop()
# print(list1)
# list1.pop(2)
# print(list1)
# list1.remove("SE")
# print(list1)
# # list1.clear()
# # print(list1)
# list1.reverse()
# print(list1)

# # del list1
# # print(list1)
# list2 = [1,4,7,2];
# list2.sort()
# print(list2)
# list3 = ["b","a","d","a"]
# list3.sort()
# print(list3)
# list4  =[1,6,3,["ahmad","SE"],[1.0,5.0]]
# print(list4[3][1])

# tuples = (8,4,"ejaz","SE")
# list1 = list(tuples)
# list1.insert(3,"computer")
# tuples = tuple(list1)
# print(tuples)
# tuples1 = (4,5,7,"ahmad",[9,1])
# print(tuples1)
# print(tuples1[4][1])

# set1  = {1,1, True, 0, False, 7.2};
# print(set1)
# set2 = {True, "ahmad"};
# set1.update(set2)
# print(set1)
# set1.union(set2)
# print(set1)
# set1.intersection(set2)
# print(set1)
# set1.add("SE")
# print(set1) 
# # pass value
# set1.remove("ahmad")
# print(set1)
# # pass value
# set1.discard(1)
# set1.pop()
# print(set1)
# # sum all the values of the set
# newset = {1,5,7,8,9,10}
# sumset = sum(newset)
# print("sum of set is : ", sumset)


# class 3 Section A

# a = 5
# a  = 3
# a = 2

# dic = {
#   "Std_ID":1,
#   "Name":"Saad",
#   "Name":"Ahmad",
#   "Section":"C"
# }
# dic1 = {
#    "Std_ID1":2,
#    "Name1":"Khizar",
#    "Section1":"A"
# }
# print(dic)
# print(dic["Name"])
# print(dic.values())
# print(dic.keys())

# dic["Section"] = "A"
# print(dic.values())
# dic["Department"] = "SE"
# print(dic)
# dic.pop("Std_ID")
# print(dic)
# dic["Subject"] = {"AI","DS","SE"}
# print(dic) 
# dic.update(dic1)
# print("value is updated",dic)




# if a > b:
#   print("a is greater than b")  
# else :
#   print("b is graeter ")

# is_loggin  = True
# if is_loggin:
#   print("direct to Dashboard")
# else: 
#   print("invalid password")

# print("A") if a < b else print("B")
# if a%2 == 0:
#   print("even")
# else:
#   print("odd")

# a = int (input("value "))

# a = 7
# b = 5
# c = 10

# if a < b:
#   print("statement")
# elif b < c:
#   print("b is less than c")
#   if a > b:
#     print("a is greater than b")
#   else:
#     print("else")

# else:
#   print("else condition") 
# name = input()
# marks = int(input());

# if marks >= 90:
#   print(name, marks)
#   print("Grade A")
# elif marks >= 80 and marks < 90
#   print

# list1 = [1,6,3,"section A", "SE"]
# print(list1[0])
# #  for (int i =0; i<=5; i+2)
# for i in range(0,5,2):
#     print(list1[i])

# table = int(input("table"))
# for i in range(1,11):
#     # print(table, "*", i, "=", table*i)
#     if(i%2 != 0):
#         print(i)

# list1 = [1 ,3,4,"SA","SE","5th semster"]
# set1 = {True,3,6,1,8}
# tuple1 = (2,"SE", "SA")
# print(type(tuple1))
# print(tuple1)
# dic = {
#     'name':"Ahmad",
#     "R.No":1,
#     "Section":"A"
# }

# for keys, values in dic.items():
#     print(keys, values)


# i = 10
# while i>=1:
#     # i = i+1
#     print(i)
#     i-=1
# while True:
#     """
#     1:language
#     2:check payment
#     3:end
#     """
#     user_input = int(input("press any value "))
#     if(user_input==1):
#         print("language")
#     elif user_input==2:
#         print("check payment")
#     elif user_input == 3:
#         break
#     else:
#         print("invalid")

# i = 0
# while i<=10:
#     i +=1
#     if i==5:
#         continue
#     print(i)


# for i in range(10, 1, -1):
#     print(i)
# WAP to iterate through a string and count how many vowels it contains. 
# WAP to repeatedly ask for a password until the user enters the correct one. 
# Keep taking input from the user until they type “stop”.

# id  = 1 
# def student_records():
#     name = input("name ")
#     f_name = input("f name ")
#     print(id, name, f_name)
# print(id)

# student_records()


# def employee(id, name, designation):
#     print(id, name, designation)
# employee(1,"name","khan")


# def countdown(n):
#     if n<0:
#         print("end")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(20)


# class 6

# class student:
    # def __init__(self,name,Department):
    #     self.name= name
    #     self.Department= Department
    #     self.studentlist = []
    #     self.studentdep = []
    # def setdata(self):
    #     name = input("name ")
#         Department = input("department ")
#         self.studentlist.append(name)
#         self.studentlist.append(Department)
#     def getdata(self):
#         for student_name in self.studentlist:
#             print(student_name)
#         for student_dep in self.studentdep:
#             print(student_dep)
    

# s1 = student("ahamd","SE")
# s1.setdata()
# s1.getdata()
# s1.setdata()
# s1.getdata()

# class Employee:
#     def __init__(self):
#         self.employees = []

#     def add(self):
#         emp_id = input("Enter ID: ")
#         name = input("Enter Name: ")
#         self.employees.append((emp_id, name))
#         print(self.employees)

# emp = Employee()
# while True:
#     ch = int(input("ch"))
#     if ch==1:
#         emp.add()
#     elif ch==2:
#         break
#     else:
#         print("invalid")

# class student:
    # name = input("name ")
    # id1 = int(input("ID "))

#     def __init__(self, section, department):
#         self.lsit1 = []
#         self.section=section
#         self.department= department
#     def std(self):
#         name=input("name ")
#         id = int(input("id "))
#         self.section=input()
#         self.department=input()
#         self.lsit1.append((name, id))
#     def get(self):
#         print(self.section, self.department)
#         for i in self.lsit1:
#             print(i)

# std1 = student("a","se")
# std1.std()
# std2 = student("b","cs")
# std2.std()
# std2.std()
# std1.get()



# class 7


# class student:
#     def __init__(self):
#         self.__name = "ahmad"
#         self.__id = 123
#     def __setdata(self):
#         self.__name = input("name ")
#         self.__id = input("ID ")
#     def getdata(self):
#         self.__setdata()
#         print(f'name {self.__name} ID {self.__id}')
# st = student()
# st.getdata()


class cecos_employee:
    def __init__(self):
        self.name = "abc"
        self.id = 123
        self.address = "pesh"
        self.contact = 1234
        self.designation = "admin"
    def setdata(self):
        self.name = input("Name ")
        self.id = int(input("ID "))
        self.address = input("Address ")
        self.contact = int(input("Contact NUmber "))
        self.designation = input("designation ")
    def getdata(self):
        print(f'Name {self.name} ID {self.id} Address {self.address} COntact Number {self.contact} Designation {self.designation}')


class faculty:
    def __init__(self):
        self.department = "SE "
    def setfaculty_data(self):
        # self.setdata()
        self.department = input("Department ")
    def getfaculty_data(self):
        # self.getdata()
        print(f"Department {self.department}")

class admin(cecos_employee, faculty):
    def setadmin_data(self):
        self.setdata()
        self.setfaculty_data()
    def getadmin_data(self):
        self.getdata()
        self.getfaculty_data()


# admin1 = admin()
# admin1.setadmin_data()
# admin1.getadmin_data()
emp1 = cecos_employee()