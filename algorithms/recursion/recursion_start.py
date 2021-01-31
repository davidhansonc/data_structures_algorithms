# -*- coding: utf-8 -*-
# @Author: David Hanson
# @Date:   2021-01-30 23:30:31
# @Last Modified by:   David Hanson
# @Last Modified time: 2021-01-31 13:41:39
counter = 0

def inception():
    global counter
    print(counter)
    if counter > 3:
        return "done!"
    counter += 1
    return inception()

inception()