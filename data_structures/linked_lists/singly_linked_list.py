# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-20 13:47:52
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-23 13:20:36

class Node:
    def __init__(self, cargo):
        self.value = cargo
        self.next = None

    def __str__(self):
        display_dict = {
            'value': self.value,
            'next': self.next
        }
        return str(display_dict)
        

class LinkedList(Node):
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        values = []
        node = self.head
        while node != None:
            values.append(node.value)
            node = node.next
        return str(values)

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, value, location_index):
        position = int(location_index)
        if position < 0 or position > self.length:
            raise IndexError("list index out of range")
        elif position == 0:
            self.prepend(value)
        elif position == self.length:
            self.append(value)
        else:
            current_node = self.head
            adding_node = Node(value)
            for ind in range(position-1):
                current_node = current_node.next
            adding_node.next = current_node.next
            current_node.next = adding_node
            self.length += 1

    def remove(self, location_index):
        del_position = int(location_index)
        if del_position < 0 or del_position > self.length-1:
            raise IndexError("list index out of range")
        elif del_position == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            current_node = self.head
            for ind in range(del_position-1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.length -= 1

    def remove_by_value(self, value):
        pass

    def reverse(self):
        if self.length <= 1:
            return self.head
        else:
            first = self.head
            second = first.next
            first.next = None
            self.tail = first
            while second:
                temp = second.next
                second.next = first
                first = second
                second = temp
            self.head = first
            return self.__str__()


my_list = LinkedList('a')
my_list.append('b')
my_list.append('c')
my_list.append('d')
my_list.append('d')
my_list.append('f')
my_list.reverse()
print(my_list)