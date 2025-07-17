# # 2D arryay
# #pattern
# for i in range(3):
#    for j in range(4):
#        print("* " , end="" )
#    print()

# for rows in range(5):
#     for coln in range(rows+1):
#       print("* ", end="")
#     print()

# n = int(input("enter pattern no.: "))
# for rows in range (1, n+1):
#    for coln in range(1, rows+1):
#        print("* ", end="")
# print()

# for rows in range(5):
#     for coln in range(rows+1):
#         print(coln+1, end="")
#     print()

# n = 4
# for rows in range(n+1):
#     for coln in range(rows+1):
#         print(rows+1, end="")
#     print()

# n = 4
# for rows in range(n+1):
#     for coln in range(rows+1):
#         print(rows+1, end="")
#     print()

# str = "ABCDE"
# for rows in range(0, len(str)):
#     for coln in range(rows+1):
#         print(str[rows], end="")
#     print()

# n = 5
# for rows in range(1, n+1):
#     for coln in range(1, rows+1):
#         print(chr(rows+64), end="")
#     print()

# n = 4
# for rows in range(n+1):
#     for coln in range(rows+1):
#         print(rows+1, end="")
#     print()

# for rows in range(5, 0, -1):
#     for coln in range(rows):
#         print("* ", end="")
#     print()

# for rows in range(5, 0 ,-1):
#     for coln in range(rows, 0, -1):
#         print(coln, end="")
#     print()

# n = 5
# for rows in range(n, 0,-1):
#     for coln in range(rows-1, 0,-1):
#         print(" ", end="")
    
#     for str in range(n,rows-coln, -1):
#         print(rows,end="")
#     print()

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# n= 5 
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n-i):
#         print("*", end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(5, i,-1):
#         print(" ", end="")
#     for j in range(i,0,-1):
#         print("* " ,end="")
#     print()
# output:
# * * * * * 
#  * * * * 
#   * * *
#    * *
#     *

# n= 5 
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n-i ,0,-1):
#         print(n, end="")
#     print()
# output:
# 54321
#  4321
#   321
#    21
#     1

# n= 5 
# for i in range(0, n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(1, n-i+1):
#         print(j, end="")
#     print()
# output:
# 12345
#  1234
#   123
#    12
#     1

# output:
# 54321
#  5432
#   543
#    54
#     5

# n= 6 
# for i in range(1, n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(1, n-i+1):
#         print(i, end="")
#     print()

#     output:
#     11111
#      2222
#       333
#        44
#         5

# n= 6 
# for i in range(1, n):
#     for j in range(i):
#           print(" ", end="")
#     for j in range(1, n-i):
#           print(j, end="")
#     print()
