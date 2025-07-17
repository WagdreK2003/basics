# # define an employee class with attributes role, department, and salary. this class should have a method to print the details of the employee.
# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def __get_detail__(self):
#         print(f"Role: {self.role}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")
    
# e1 = Employee("Software Engineer", "IT", 60000)
# e1.__get_detail__()

# create an engineer class that inherits from employee class. and has additional attribute: name and age.
# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def __get_detail__(self):
#         print(f"Role: {self.role}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")

# class Engineer(Employee):
#     def __init__(self, name, age, role, department, salary):
#         super().__init__(role, department, salary)
#         self.name = name
#         self.age = age

#     def __get_Engineer_detail__(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         super().__get_detail__()

# e1 = Engineer("John Doe", 30, "Software Engineer", "IT", 60000)
# e1.__get_Engineer_detail__()

# Lamda functions
# example : add = lambda x, y: x + y
# mx = lambda x, y: x if x > y else y

# print the square of a number using lambda function
# square = lambda x:x**2
# print(square(5))

# you are given a list of numbers. use lambda function with the map() function to double each number in the list.
# num = [1,2,3,4,5]
# dub = list(map(lambda x: x * 2, num))
# print(dub)

# exception handling

# try:
#     for i in range(5):
#         print(f"{a}: ")
# except Exception as e:
#     print("invalid input", e)
#     print(e)

#wrong
# try:
#     age = 23
#     if(age > 18 or age < 60):
#         print("age is in range")
#     else:
#         raise BufferError("age not in range")
# except Exception as e:
#     print("Exception occurred:", e)
# finally:
#     print("This block always executes, regardless of exceptions.")

