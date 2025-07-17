# deque.
# append
# appendleft
# pop 
# popleft
#peek()
#isEmpty()


# from collections import deque
# dq = deque("madam")
# print(dq)

# while len(dq) > 1:
#     if dq.pop()!=dq.popleft():
#         flag=False
#     else:
#         flag=True

# if(flag == True):
#     print("palindrome")
# else:
#     print("not palindrome")


# from collections import deque
# def is_palindrome(word):
#     dq = deque(word)
#     while len(dq) > 1:
#         if dq.popleft() != dq.pop():
#             return False
#     return True

# word = input("enter the word: ")
# if is_palindrome(word):
#     print(f"{word} is Palindrome")
# else:
#     print(f"{word} is not a palindrome")

#Back Tracking
#binary tree

# class node:
#     def __init__(self, node, lnode=None, rnode=None):
#         self.node = node
#         self.lnode = lnode
#         self.rnode = rnode

# root=node(2)

# root.lnode=node(7)
# root.rnode=node(5)

# root.lnode.lnode=node(2)
# root.lnode.rnode=node(6)

# root.rnode.lnode=node(4)
# root.rnode.rnode=node(9)

# def preorder(node):
#     if(node):
#         print(node.node, end=" ")
#         preorder(node.lnode)
#         preorder(node.rnode)

# preorder(root)

# class node:
#     def __init__(self, node, lnode=None, rnode=None):
#         self.node = node
#         self.lnode = lnode
#         self.rnode = rnode

# root=node(2)

# root.lnode=node(7)
# root.rnode=node(5)

# root.lnode.lnode=node(2)
# root.lnode.rnode=node(6)

# root.rnode.lnode=node(4)
# root.rnode.rnode=node(9)

# def inorder(node):
#     if(node):
#         inorder(node.lnode, end =" ")
#         print(node.node)
#         inorder(node.rnode)

# inorder(root)


# class node:
#     def __init__(self, node, lnode=None, rnode=None):
#         self.node = node
#         self.lnode = lnode
#         self.rnode = rnode

# root=node(2)

# root.lnode=node(7)
# root.rnode=node(5)

# root.lnode.lnode=node(2)
# root.lnode.rnode=node(6)

# root.rnode.lnode=node(4)
# root.rnode.rnode=node(9)

#postorder

# def postorder(node):
#     if(node):
#         postorder(node.lnode)
#         postorder(node.rnode)
#         print(node.node, end=" ")

# postorder(root)
# print()


# inorder

# def inorder(node):
#     if(node):
#         inorder(node.lnode)
#         print(node.node, end=" ")
#         inorder(node.rnode)

# inorder(root)
# print()

#prorder

# def preorder(node):
#     if(node):
#         print(node.node, end=" ")
#         preorder(node.lnode)
#         preorder(node.rnode)

# preorder(root)
# print()