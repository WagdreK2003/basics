# OOP
# class and object
# class = data, purpose.
# class student:
#     name="khushi"
#     def __init__(self):
#         print(self)
# s1=student()
# print(s1)

# __init__ function
# class student:
#     def __init__(self, name):
#         self.name = name
#         # print(self.name)
# s1=student("khushi")
# print(f"s1 = {s1.name}")

# s2 = student("khush")
# print(f"s2 = {s2.name}")

# constractor
# del keyword : used to delete object properties orobject itself.


# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 =m1
#         self.m2 =m2
#         self.m3 =m3

#     def get__avg(self):
#         avg=(self.m1+self.m2+self.m3)/3
#         print(avg)

# s1 = Student("khushi", 54, 65, 76)
# s1.get__avg()

# s2 = Student("mrunal", 55, 67, 79)
# s2.get__avg()

# s3 = Student("janvai", 56, 68, 79)
# s3.get__avg()

#static method
# 4 pillars of OOP
# 1.abstraction 2. encapsulation 3. inheritance 4. polymorphism

# class car:
#     def __init__(self, clutch, acc, brake): 
#         self.clutch = clutch
#         self.acc = acc
#         self.brake = brake
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         self.brake = False
#         print("Car is moving")
#     def stop(self):
#         self.clutch = False
#         self.acc = False
#         self.brake = True
#         print("Car stopped")
    
# c1=car(True, True, False)
# c1.start()
# c1=car(False, False, True)
# c1.stop()
# print(c1.clutch)

# encapsulation
# class Account:
#     def __init__(self, username, password):
#         self.__username = username
#         self.__password = password

#     def getdata(self):
#         self.__get_details__()

#     def __get_details__(self):
#         print(f"Username: {self.__username}")
#         print(f"Password: {self.__password}")

# a1 = Account("khushi", "1234")
# a1.getdata()

# create account class with 2 attributes balance and account_number. create methods for password that is hideen, debit(), credit() & printing the balance getbalance()
# class Account:
#     def __init__(self, account_number, balance=0):
#         self.__account_number = account_number
#         self.__balance = balance
    
#     def debit(self, amount):
#         self.__balance -= amount

#     def credit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         print(f"Account Number: {self.__account_number}")
#         print(f"Current Balance: {self.__balance}")

# a1 = Account("123456789", 1000)
# a1.get_balance()

# create account class with 2 attributes balance and account_number. create methods for password that is hideen, debit(), credit() & printing the balance getbalance()
# class Account:
#     def __init__(self, account_number, acc_pass, balance=0):
#         self.__account_number = account_number
#         self.__balance = balance
#         self.__acc_pass = acc_pass
    
#     def debit(self, amount, password):
#         if amount > self.__balance:
#             print("Insufficient balance")
#             return     
#         self.__check_password(password)
#         self.__balance -= amount

#     def credit(self, amount, password):
#         if amount < 0:
#             print("Amount to credit must be positive")
#             return
#         self.__check_password(password)
#         self.__balance += amount

#     def get_balance(self, password):
#         self.__check_password(password)
#         print(f"Account Number: {self.__account_number}")
#         print(f"Current Balance: {self.__balance}")

#     def __check_password(self, password):
#         self.__acc_pass = password
#         if self.__acc_pass != password:
#             print("Incorrect password")
            
# a1 = Account("123456789", "pass123", 1000)
# a1.get_balance("pass123")
# a1.credit(500, "pass123")
# a1.get_balance("pass123")
# a1.debit(200, "pass123")

#inheritance
# polymorphism
# class complex_number:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
    
#     def get_output(self):
#         print(f"{self.real} + {self.imag}i")

#     def __add__(self, other):
#         numimag = self.real + other.real
#         numreal = self.imag + other.imag    
#         return complex_number(numimag, numreal)
    
# c1 = complex_number(2, 3)
# c2 = complex_number(4, 5)
# c3 = c1 + c2
# c3.get_output()

# define a circle class to create a circle with radius r using the constructor.
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def display(self):
#         print(f"radius of circle = {self.r}")
#     def area(self):
#         area = 3.14 * (self.r)**2
#         print(f"area of circle {area}")
#     def perimeter(self):
#         perimeter = 2 * 3.14 * (self.r)
#         print(f"perimeter of circle {perimeter} ")
# c = Circle(12)
# c.display()
# c.perimeter()
# c.area()

