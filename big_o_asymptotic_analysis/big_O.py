# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-13 17:38:12
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-15 15:14:56

from performance_decorator import performance

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', \
        'nigel', 'squirt', 'darla', 'hank']
large = ['nemo'] * 100000

# @performance
def find_nemo(array):
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found Nemo!')
            break

# find_nemo(large)  # O(n) --> Linear Time

box_list = [0, 1, 2, 3, 4, 5]
def log_first_two_boxes(boxes):
     print(boxes[0])  # O(1)
     print(boxes[1])  # O(1)

# log_first_two_boxes(box_list)  # O(2)

# Log all pairs of array
boxes = ['a', 'b', 'c', 'd', 'e']
def log_pairs(listy):
    for i in boxes:
        for j in boxes:
            print(i, j)
log_pairs(boxes)