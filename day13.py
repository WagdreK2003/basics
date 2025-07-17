# merge sort
# def merge_sort(arr):
#     if (len(arr) <= 1):
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)
# def merge(left, right):
#     result = []
#     i = j = 0
#     while (i < len(left) and j < len(right)):
#         if (left[i] < right[j]):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# arr = [38, 27, 43, 3, 9, 82, 10]
# sorted_arr = merge_sort(arr)
# print("Sorted array:", sorted_arr)

# #quick sort
# def quick_sort(a):
#     if (len(a) <=1):
#         return a 
#     pivot = a[len(a) // 2]
#     smaller = []
#     larger = []
#     for i in a:
#         if (i < pivot):
#             smaller.append(i)
#         elif (i > pivot):
#             larger.append(i)
#     return quick_sort(smaller) + [pivot] + quick_sort(larger)
# a = [38, 27, 43, 3, 9, 822, 90]
# sorted_a = quick_sort(a)
# print("Sorted array:", sorted_a)

# output = [3, 9, 27, 38, 43, 90, 822]
# 744,75,303,912.
# a = [38, 27, 43, 3, 9, 822, 90, 10, 5, 6, 1, 2, 4, 8, 7, 11, 12, 13, 14, 15]
# sum = 0*(len(a) + 1)
# print(sum)
# for i in range(len(a)):
