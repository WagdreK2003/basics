# linked list
# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# node1 = node(12)
# node2 = node(24)
# node3 = node(20)

# node1.next = node2
# node2.next = node3
# node3.next = None 

# head = node(1)
# head.next= node1

# nodemid=node(34)
# nodemid.next=node2
# node1.next= nodemid

# print(node2.data)

# currentable = head
# print(currentable)

# while currentable != None:
#     print(currentable.data)
#     currentable= currentable.next

# create a linked list with value 5, 10, 15, 20 , 25, 30 and print them.
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
# node1 = node(10)
# node2 = node(15)
# node3 = node(20)
# node4 = node(25)
# node5 = node(30)

# head=node(1)
# head.next=node1
# node1.next= node2
# node2.next= node3
# node3.next= node4
# node5.next= None

# currentable=head
# print(currentable)

# while currentable!=None:
#     print(currentable.data, end="->")
#     currentable=currentable.next

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
# node1 = node(10)
# node2 = node(15)
# node3 = node(20)
# node4 = node(25)
# node5 = node(30)

# head=node(1)
# head.next=node1
# node1.next= node2
# node2.next= node3
# node3.next= node4
# node4.next= None

# nodemid=node(34)
# nodemid.next=node2
# node1.next= nodemid


# currentable=head
# print(currentable)

# while currentable!=None:
#     print(currentable.data, end="->")
#     currentable=currentable.next

# class node:
#     def _init_(self,data):
#         self.data= data
#         self.next = None

# head = node(1)
# n2 = node(2)
# n3 = node(3)
# n4 = node(4)
# nMid = node(3)
# newHead= node(99)


# newHead.next = head
# head.next = n2
# # nNew.next = n2
# n2.next = n3
# n3.next = nMid

# nMid = n4

# n4.next= None

# currentNode = head
# while currentNode != None:
#     print(currentNode.data,end="->")
#     currentNode = currentNode.next
# print(None)

class Stack:
    def __init__(self):
        self.items = []
    
    def append_stack(self, data):
        self.items.append(data)

    def is_Empty(self):
        return len(self.items) == 0
    
    def peek_stack(self):
        if not Stack.is_Empty(self):
            return self.items[-1]
        else:
            print("Stack is empty")

    def pop_stack(self):
        if not Stack.is_Empty(self):
            return self.items.pop()
        else:
            print("Stack is empty")

    def display(self):
        print(f"Stack: {self.items}")

stk = Stack()

stk.append_stack(10)
stk.append_stack(20)
stk.display()
stk.pop_stack()
stk.display()

