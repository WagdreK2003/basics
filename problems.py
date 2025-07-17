#reverse the number

# num = 1234
# a= str(num)
# reverse = int(num[::-1])
# print(reverse)

# no = 789
# reverse = 0
# while (no > 0):
#     a = no % 10
#     reverse = reverse * 10 + a
#     no = no // 10
# print(reverse)

# n = 789
# reverse =0
# if (n < 0):
#     n = -1* n
#     print(n)

# while (n > 0):
#     a = n % 10
#     reverse = reverse * 10 + a
#     n = n // 10
#     reverse= -1*reverse
# print(reverse)

# num = -123
# rev = 0
# value = 1 
# if num < 0:
#     value = -1
#     num = abs(num)

# while num > 0:
#     num1 = num % 10
#     rev = rev * 10 + num1
#     num = num // 10
# rev *= value
# print(rev)

## mutate a string. 
# str = "collage"
# a= list(str)
# a=str.replace(str[3], "a")
# str="".join(a)
# print(a)


# str = "collage"
# l= list(str)
# l[3] = "a"
# str = " ".join(l)
# print(str)

# sum of no =target

# a = [2,3,5,7,8]
# target = 9
# l =len(a)
# for i in range(l):
#     for j in range(i+1, l):
#         if a[i] + a[j] == target:
#             print(i , j)

#or 
## binary search
# a = [2,3,5,7,8]
# l=sorted(a)
# print("original:", a)
# print("sorted:", l)
# target=9
# start=0
# end=len(l)-1
# found = False

# while start < end: 
#     summ = l[start] + l[end]
#     if (summ==target): 
#         print(f"{l[start]} + {l[end]} = {summ}")
#         found = True
#         start += 1  
#     elif(summ < target):
#         start+=1
#     else:
#         end-=1
# if not found:
#     print("no. not fond")

# diffrences
# a = [2,3,5,7,8]
# target = 9
# start = 0 
# end = len(a)-1
# d={}
# while end>=start:
#     if(a[start] + a[end]==target):
#         d[(a[start] + a[end])] = (start, end)
#         start =start+1
#         end= end-1
#     elif a[start]+a[end]<target:
#         start= start+1
#     else:
#         end = end- 1
# print(d)

# a = [2,3,5,7,8]
# target = 8
# d = {}
# for i in range(len(a)):
#     diff = target - a[i]
#     if diff in d:
#         print(f"Pair found: ({diff}, {a[i]})")
#     d[a[i]] = i

##1 = Silent
##2 = listen

# str1 = "silent"
# str2 = "listen"
# if len(str1) != len(str2):
#     print("False")
# else:
#     for i in str1:
#         if str1.count(i) != str2.count(i):
#             print("False")
#             break
#     else:
#         print("True")


# #leap year
# def s_year(year):
#     leap=False
    
#     if (year %4==0):
#         if(year %100==0):
#             if(year %400==0):
#                 leap=True
#             else:
#                 leap = False
#         else:
#             leap =True
#     else:
#         leap=False

#     return leap

# year = int(input("Enter the year:"))
# print(s_year(year))

# n = int(input())
# students = [["Alice", 50],
#     ["Bob", 45.5],
#     ["Charlie", 45.5],
#     ["David", 55],
#     ["Eve", 60],
#     ["Frank", 50]]
# for _ in range(n):
#     name = input()
#     grade = float(input())
#     students.append([name, grade])
#     grades = sorted(list(set([student[1] for student in students])))
#     second_lowest = grades[1]
#     second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest])
#     for name in second_lowest_students:
#         print(name)
        

# n = int(input("enter the students: "))
# students=[]
students = [["Alice", 50],
    ["Bob", 45.5],
    ["Charlie", 45.5],
    ["David", 55],
    ["Eve", 60],
    ["Frank", 50]]

grades = sorted(list(set([student[1] for student in students])))
print(grades)
sec_low = grades[1]
sec_low_students = sorted([student[0] for student in students if student[1] == sec_low])
for name in sec_low_students:
    print(name)
