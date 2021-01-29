# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-26 08:47:40
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-26 10:37:35
class Node():
    def __init__(self, value):
        self.value = value;
        self.next = None

    def __str__(self):
        return str(self.value)

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first == None:
            return str(None)
        else:
            print_list = []
            node = self.first
            while node:
                print_list.append(node.value)
                node = node.next
            return str(print_list[::-1])

    def peek(self):
        print(self.first)
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.last = new_node
            self.first = new_node
        else:
            temp = self.last
            self.last = new_node
            temp.next = new_node
        self.length += 1


    def dequeue(self):
        if self.length == 0:
            return None
        else:
            dequeued_node = self.first
            self.first = self.first.next
            self.length -= 1
            return dequeued_node

    def is_empty(self):
        if self.length == 0:
            return print("empty")
        else:
            return print("not empty, bro")

my_queue = Queue()
print(my_queue)
my_queue.peek()
my_queue.enqueue(46)
print(my_queue.first)
print(my_queue.last)
my_queue.enqueue('test')
print(my_queue.first)
print(my_queue.last)
my_queue.enqueue('test2')
my_queue.peek()
print(my_queue)
my_queue.dequeue()
my_queue.is_empty()
print(my_queue)
my_queue.dequeue()
print(my_queue)
my_queue.dequeue()
print(my_queue)
my_queue.is_empty()
my_queue.peek()
