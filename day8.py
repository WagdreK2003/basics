# program to find the factorial of n.
# def fact(n):
#     fac= 1
#     for i in range(1, n+1):
#         fac=fac*i
#     print(fac)
# fact(5)

#permutation
# def perm(n, r):
#     facn = 1
#     facr = 1
#     for i in range(1, n + 1):
#         facn *= i
#     for j in range(1, r + 1):
#         facr *= j
#     perm = facn // facr
#     print(perm)
# perm(5, 3)

# # or

# def fact(n):
#     fac= 1
#     for i in range(1, n+1):
#         fac=fac*i
#     return fac
# n=6
# r=6
# num=fact(n)
# d=fact(n-r)
# per=num // d
# print(per)


# combination
# def comb(n, r):
#     facn = 1
#     facr = 1
#     facnr = 1
#     for i in range(1, n + 1):
#         facn *= i
#     for j in range(1, r + 1):
#         facr *= j
#     for k in range(1, n - r + 1):
#         facnr *= k
#     comb = facn // (facr * facnr)
#     print(comb)
# comb(5, 3)

# #or

# def fact(n):
#     fac= 1
#     for i in range(1, n+1):
#         fac=fac*i
#     return fac
# n=5
# r=3
# num=fact(n)
# c=fact(r)
# d=fact(n-r)
# com = num // (c * d)
# print(com)

#recursion
# print numbers from 1 to 10 using recursion.
# def print_numbers(n):
#     if n>10:
#         return
#     print(n)
#     print_numbers(n + 1)
# print_numbers(1)

# sum of first n natural numbers using recursion.
# def sumn(n):
#     if n<=0:
#         return 0
#     return n + sumn(n-1)
# print(sumn(5))

#write a recursive function to calculate the sum of first n natural numbers.
# def sumn(n):
#     if n == 0 or n ==1:
#         return 1
#     return n * sumn(n - 1)
# print(sumn(5))

#permutation using recursion.
# def perm(n, r):
#     if r == 0:
#         return 1
#     return n * perm(n - 1, r - 1)
# print(perm(5, 3))

# combination using recursion.
# def comb(n, r):
#     if r == 0 or r == n:
#         return 1
#     return comb(n - 1, r - 1) + comb(n - 1, r)
# print(comb(5, 3))

#file I/O
# myfile = open("demo.txt","w")
# myfile.write("Hello, this is a test file.")
# myfile.write(" This file is created for testing file I/O operations in Python.")
# myfile = open("demo.txt")
# data=myfile.readline() 
# print(data)
# myfile.close()

# myfile = open("demo.txt","a")
# myfile.write("\nok\n")
# myfile.write("good\n")
# print(myfile)
# myfile.close()

# .remove
# import os
# os.remove("demo.txt")

# #create a file "practice.txt". replace python with java script in this program
# myfile = open("practice.txt", "w")
# myfile.write("\nHi everyone.\n")
# myfile.write("\nWe are learning file handlingI/O.\n")
# myfile.write("\nusing Python.\n")
# myfile.write("I like programming in python.\n")
# print(myfile)
# myfile.close()

# myfile = open("practice2.txt", "r")
# data = myfile.read()
# myfile = open("practice2.txt", "w")
# myfile.write("\nHi everyone.\n")
# myfile.write("\nWe are learning file handlingI/O.\n")
# myfile.write("\nusing python.\n")
# myfile.write("I like programming in python.\n")
# new_content = data.replace("python", "javascript")
# myfile.write(new_content)
# print(new_content)
# myfile.close()

# # find the word learning.
# myfile = open("practice2.txt", "r")
# data = myfile.read()
# myfile = open("practice2.txt", "w")
# myfile.write("\nHi everyone.\n")
# myfile.write("\nWe are learning file handlingI/O.\n")
# myfile.write("\nusing python.\n")
# myfile.write("I like programming in python.\n")
# new_content = data.find("learning")
# print(new_content)
# myfile.close()