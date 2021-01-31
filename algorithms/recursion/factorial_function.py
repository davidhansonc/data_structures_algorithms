# -*- coding: utf-8 -*-
# @Author: David Hanson
# @Date:   2021-01-31 13:45:32
# @Last Modified by:   David Hanson
# @Last Modified time: 2021-01-31 14:09:40

# recursive method:
def find_factorial_recursive(number):
    if number <= 1:
        return 1
    else:
        return number * find_factorial_recursive(number-1)


# iterative method
def find_factorial_iterative(number):
    num_step = number - 1
    while num_step > 0:
        number = number * num_step
        num_step -= 1
    return number



print(find_factorial_recursive(10))
print(find_factorial_iterative(10))