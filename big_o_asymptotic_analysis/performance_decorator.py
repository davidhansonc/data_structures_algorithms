# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-13 17:53:44
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-13 17:54:16
from time import time

def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = fn(*args, **kwargs)
    t2 = time()
    print(f'took {t2-t1}')
    return result
  return wrapper

@performance
def long_time():
    for i in range(10000):
        i*5

if __name__ == '__main__':
    long_time()