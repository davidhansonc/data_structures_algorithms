# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-19 10:58:37
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-19 11:52:28
def merge_sorted_lists(list1, list2):
    if list1 == []:
        return list2
    elif list2 == []:
        return list1
    else:
        merged_list = []
        index1 = 0
        index2 = 0
        while not (index1 > len(list1)-1 or index2 > len(list2)-1):
            add = min(list1[index1], list2[index2])
            if add == list1[index1]:
                index1 += 1
            else:
                index2 += 1
            merged_list.append(add)
            if index1 > len(list1)-1:
                merged_list.extend(list2[index2:])
            if index2 > len(list2)-1:
                merged_list.extend(list1[index1:])
    return merged_list



print(merge_sorted_lists([0, 3, 4, 31], [4, 6, 30, 85, 104, 394]))
