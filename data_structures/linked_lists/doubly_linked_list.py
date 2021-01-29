# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-20 13:47:52
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-22 16:40:20

class Node:
    def __init__(self, cargo):
        self.value = cargo
        self.previous = None
        self.next = None

    def __str__(self):
        display_dict = {
            'value': self.value,
            'previous': self.previous.value,
            'next': self.next.value
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
        new_node.previous = self.tail
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
            if position <= self.length / 2 - 1:
                print('going forward!!')
                current_node = self.head
                adding_node = Node(value)
                for ind in range(position-1):
                    current_node = current_node.next
                print(current_node)
                following_node = current_node.next
                following_node.previous = adding_node
                current_node.next = adding_node
                adding_node.previous = current_node
                adding_node.next = following_node
                self.length += 1
            else:
                print('going backward!!')
                current_node = self.tail
                adding_node = Node(value)
                for ind in range(self.length-1, position+1, -1):
                    current_node = current_node.previous
                following_node = current_node.previous
                following_node.next = adding_node
                current_node.previous = adding_node
                adding_node.previous = following_node
                adding_node.next = current_node
                self.length += 1

    def remove(self, location_index):
        del_position = int(location_index)
        if del_position < 0 or del_position > self.length-1:
            raise IndexError("list index out of range")
        elif del_position == 0:
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
        else:
            if del_position <= self.length / 2 - 1:
                current_node = self.head
                for ind in range(del_position-1):
                    current_node = current_node.next
                current_node.next = current_node.next.next
                current_node.next.previous = current_node
                self.length -= 1
            else:
                current_node = self.tail
                for ind in range(self.length-1, del_position+1, -1):
                    current_node = current_node.previous
                current_node.previous = current_node.previous.previous
                current_node.previous.next = current_node
                self.length -= 1

    def remove_by_value(self, value):
        pass

    # def reverse(self):
    #     rebuild = self.head
    #     temp = self.tail
    #     while rebuild != None:
    #         rebuild = temp
    #         rebuild.next = temp.previous
    #         rebuild.previous = temp.next

    #         rebuild = rebuild.next
    #         temp = temp.previous
    #     self.tail = rebuild




my_list = LinkedList('a')
my_list.append('b')
my_list.append('c')
my_list.append('d')
my_list.append('e')
my_list.append('f')
my_list.append('g')
my_list.append('h')
my_list.append('i')
my_list.insert('forward', 2)
my_list.insert('backward', 6)
my_list.remove(2)
my_list.remove(6)
print(my_list)
