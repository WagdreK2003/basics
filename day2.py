# string- immutable in nature
# collection of characters

# concatinaton
# a= "hello"
# b= "world"
# print(a+b)
# print(a+" "+b)

#slicing - accessing parts of a string
# str[starting_idx : ending_idx]   last index is not included

# name = "khushi"
# ## starting a substring
# startingsub = name[0:4]
# startingsub1 = name[:4]
# print(startingsub)
# print(startingsub1)

# ##ending a substring
# str1 = name[4:5]
# str2 = name[4:len(name)]
# str3 = name[4:]
# print(str1)
# print(str2)
# print(str3)

## negative index
#  K  H  U  S  H  I
# -6 -5 -4 -3 -2 -1

#  name = "khushi"
#  str1 = name[-1:-3:-1]     # str[starting_idx : ending_idx: return_positive]
#  str2 = name[-4:len(name)]
#  str3 = name[-4:]
#  str4 = name[-3:-1:-1]   no output
#  print(str1)
#  print(str2)
#  print(str3)
#  print(str4)

##que1
# name = str(input("enter first name: "))
# print(f"{name}")
# print(len(name))

##que2
# a = "maam"
# print("true" if a[0]== a[-1] else "false")

##que3
# str1 = (input("word for palandrom: "))
# print("true" if str1==str1[-1:-len(str1)-1:-1] else "false")

# ostr = input("Enter a string to check: ")
# reverse= ostr[-1:len(ostr)-1:-1]
# print(reverse)

#string in-build function
#endwith() - check wether it end with given string or not
#capitalize() - chapital first letter
#replac("old_word","new_word") - replace old string with new
#find() - gives the index of first letter of string inside in paranthesis
#swapcase()- change capital to small and vice-versa
#upper()
#lower()
#count()- give no. of time the letter/ string occurs

##ques1
# word = "today's topic is string in python"

# word = input("Enter your name: ")
# print(word.find("a"))
# print(word.count("a"))

##ques2
# name = input("Enter your name: ")
# print(f"{name}")
# if(name==name.upper()):
#     print("name is in uppercase")
# elif(name==name.lower()):
#     print("name is in lower")
# else:
#     print("mixed cases")

# print("true" if name.upper() else "false")

##ques3
# str1 = input("enter mail ID:")
# if(str1.endswith(".com") and str1.find("@")!=-1):
#     print("valid")
# else:
#     print("Invaild")
    
##conditional statements
# if()
# elif()
# else
# nested if else

##ques1
# num = int(input("enter the number: "))
# if (num % 2 !=0):
#     print("no. is odd")
# else:
#     print("no. is even")

##ques2
# uname = input("enter username: ")
# if(" " in uname):
#     print("Invalid username")
# elif(len(uname)<4):
#     print("Too short")
# else:
#     print("username accepted")

##ques3
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# if(a>b and a>c):
#     print("greater no. is " , a)
# elif(b>c):
#     print("greater no. is" , b)
# else:
#     print("greater no. is " ,c)
# ans = max(a, b,c)
# print(f"{ans}")

##ques4
# num = int(input("no. :"))
# if (num%7==0):
#     print("number is multiple of 7")
# else:
#     print("number is not multiple of 7")