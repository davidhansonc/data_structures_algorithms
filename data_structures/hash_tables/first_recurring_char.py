# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-20 12:06:26
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-20 12:58:07
'''
Google Question
Given an array, return the first recurring character
Example 1 : array = [2,1,4,2,6,5,1,4]
It should return 2
Example 2 : array = [2,6,4,6,1,3,8,1,2]
It should return 6
Example 3 : array = [2, 3, 4, 5]
It should return undefined
'''

# speed efficient method
def first_recurring_char(array=[]):
    char_store = dict()
    for char in array:
        if char in char_store:
            first_char = char
            return first_char
        else:
            char_store[char] = 1
    return 'undefined'

# space efficient method
def first_recurring_char2(array=[]):
    first_repeat_index = len(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j] and j < first_repeat_index:
                first_repeat_index = j
    if first_repeat_index == len(array):
        return 'undefined'
    return array[first_repeat_index]


print(first_recurring_char2([2, 5, 5, 2, 3, 5, 1, 2, 4]))
print(first_recurring_char([2, 6, 4, 6, 1, 3, 8, 1, 2]))
print(first_recurring_char([2, 3, 4, 5]))