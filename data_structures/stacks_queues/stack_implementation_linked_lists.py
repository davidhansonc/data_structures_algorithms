# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-23 13:37:35
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-25 21:45:57
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.height = 0

    def __str__(self):
        if self.top == None:
            return str(None)
        else:
            print_list = []
            node = self.top
            while node:
                print_list.append(node.data)
                node = node.next
            return str(print_list[::-1])

    def peek(self):
        return self.top
        
    def push(self, value):
        self.height += 1
        node = Node(value)
        if self.height == 1:
            self.top = node
            self.bottom = node
        else:
            temp = self.top
            self.top = node
            self.top.next = temp
        return self

    def pop(self):
        if self.height < 1:
            return None
        elif self.height == 1:
            popped_node = self.top
            self.top = None
            self.bottom = None
            self.height = 0
        else:
            popped_node = self.top
            self.top = self.top.next
            self.height -= 1
        return popped_node

    def is_empty(self):
        if self.height == 0:
            return print("stack is empty")
        else:
            return print(f"stack height is {self.height}")

my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
print(my_stack)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack)
my_stack.is_empty()
my_stack.push('hello')
print(my_stack)