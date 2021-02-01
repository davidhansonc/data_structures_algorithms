# -*- coding: utf-8 -*-
# @Author: David Hanson
# @Date:   2021-01-31 14:16:27
# @Last Modified by:   David Hanson
# @Last Modified time: 2021-01-31 19:25:45

# recursive approach:
def fibonacci_recursive(index):
    if index < 2:
        return index
    return fibonacci_recursive(index-1) + fibonacci_recursive(index-2)


# iterative approach:
def fibonacci_iterative(n):
    if n < 2:
        return n
    else:
        array = [0, 1]
        for i in range(2, n + 1):
            array.append(array[i-1] + array[i-2])
        return array[-1]


print(fibonacci_iterative(0))  #0
print(fibonacci_iterative(1))  #1
print(fibonacci_iterative(5))  #5
print(fibonacci_iterative(7))  #13
print(fibonacci_iterative(10)) #55
print(fibonacci_iterative(12)) #144

print(fibonacci_recursive(0))  #0
print(fibonacci_recursive(1))  #1
print(fibonacci_recursive(5))  #5
print(fibonacci_recursive(7))  #13
print(fibonacci_recursive(10)) #55
print(fibonacci_recursive(12)) #144