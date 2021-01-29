# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-18 14:22:02
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-18 15:26:03
class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}


    def __str__(self):
        return str(self.__dict__)


    def get(self, index):
        return self.data[index]


    def append(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length


    def pop_end(self):
        bye_bye = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return bye_bye


    def delete(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


new_array = MyArray()