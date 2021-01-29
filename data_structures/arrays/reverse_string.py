# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-19 10:22:34
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-19 10:56:52
my_string = 'abcde fgh'

def reverse_string(string):
    rev_str = ''
    for i in range(len(string)-1, -1, -1):
        rev_str += string[i]
    return rev_str

def reverse_string2(string):
    return string[::-1] 


print(reverse_string(my_string))
print(reverse_string2(my_string))