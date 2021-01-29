# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-23 13:37:35
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-26 11:03:54
class Stack():
    def __init__(self):
        self.node_list = []

    def __str__(self):
        return str(self.node_list)

    def peek(self):
        return self.node_list[-1]
        
    def push(self, value):
        self.node_list.append(value)
        return self

    def pop(self):
        popped_node = self.node_list.pop()
        return popped_node

    def is_empty(self):
        return print(f"stack height is {len(self.node_list)}")

if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push('a')
    my_stack.push('b')
    print(my_stack)
