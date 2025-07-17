#swapping two variables using third variable
# a= 5
# b = 10
# temp = a
# a=b
# b=temp
# print("After swapping: a =", a, ", b =", b)

#swapping two variables without using third variable
# a= 5
# b = 10
# a=a+b
# b=a-b
# a=a-b
# print("After swapping: a =", a, ", b =", b)

# bubble sort

# n = [64, 34, 25, 12, 22, 11, 90]
# print("unsorted array: ",n)
# for i in range(len(n)):
#     for j in range(0, len(n)-i-1):
#         if n[j] > n[j+1]:
#             n[j], n[j+1] = n[j+1], n[j]
# print("Sorted array is:", n)

#or 

# def bubble_sort(arr):
#     n = len(arr)-1
#     print("Unsorted array:", arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# print("Sorted array is:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))

#insertion sort
# def insertion_sort(arr):
#     print("Unsorted array:", arr)
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#     return arr
# print("Sorted array is:", insertion_sort([64, 34, 25, 12, 22, 11, 90]))

# selection sort
# def selection_sort(arr):
#     n = len(arr)
#     print("Unsorted array:", arr)
#     for i in range(0, n):
#         mindex = i
#         for j in range(i+1, n):
#             if arr[j] < arr[mindex]:
#                 mindex = j
#         arr[i], arr[mindex] = arr[mindex], arr[i]
#     return arr
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("Sorted array is:" , (selection_sort(arr)))