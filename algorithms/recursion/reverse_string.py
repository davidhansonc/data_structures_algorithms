# -*- coding: utf-8 -*-
# @Author: David Hanson
# @Date:   2021-01-31 19:50:36
# @Last Modified by:   David Hanson
# @Last Modified time: 2021-01-31 20:05:57

def string_reverse(stringy):
    if len(stringy) == 1:
        return stringy[0]
    return stringy[-1] + string_reverse(stringy[:len(stringy)-1])


print(string_reverse("hello today is the Lord's day"))