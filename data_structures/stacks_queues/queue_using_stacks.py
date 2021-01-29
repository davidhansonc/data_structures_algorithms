# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-26 10:46:38
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-26 12:29:49
class Queue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first = []
        self.last = []
        

    def __str__(self):
        return str(self.first)


    def enqueue(self, value):
        """
        Push element value to the back of queue.
        :type value: int
        :rtype: None
        """
        self.first = []
        self.last.append(value)
        temp = self.last[:]
        while temp:
            self.first.append(temp.pop())


    def dequeue(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        removed = self.first.pop()
        self.last = []
        temp = self.first[:]
        while temp:
            self.last.append(temp.pop())
        return removed


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.first[-1]
        

    def is_empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        pass        


# Your Queue object will be instantiated and called as such:
obj = Queue()
obj.enqueue('test')
obj.enqueue('test2')
obj.enqueue('test3')
obj.enqueue('test4')
obj.enqueue('test5')
print(obj)
param_2 = obj.dequeue()
obj.enqueue('test6')
print(param_2)
print(obj)
param_3 = obj.peek()
print(param_3)
# param_4 = obj.is_empty()