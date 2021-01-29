# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-19 17:50:23
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-20 11:50:27
class hash_table():
    def __init__(self,size): #We initialize the size of our hash table(no. of buckets) with the size given to the class object
        self.size = size
        self.data = [None]*self.size #We initialize an array of size 'size' with None


    def __str__(self): #As in the array implementation, this method is used to print the attributes of the class object in a dictionary format
        return str(self.__dict__)

    def _hash(self, key): #Our custom hash function
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size #ord(key[i]) gives the unicode code point of the character key[i]
        return hash #The hash value obtained after applying the hash function to the key is returned

    def set(self, key, value):
        hash_loc = self._hash(key)
        if not self.data[hash_loc]:
            self.data[hash_loc] = [[key, value]]
        else:
            self.data[hash_loc].append([key, value])

    def get(self, key):
        hash_loc = self._hash(key)
        if len(self.data[hash_loc]) == 1:
            return self.data[hash_loc][0][1]
        else:
            for pair in self.data[hash_loc]:
                if pair[0] == key:
                    return pair[1]

    def keys(self):
        key_list = []
        for slot in self.data:
            for pair in slot:
                key_list.append(pair[0])
        return key_list

    def values(self):
        value_list = []
        for slot in self.data:
            for pair in slot:
                value_list.append(pair[1])
        return value_list

my_hash = hash_table(5)
my_hash.set('grapes', 10000)
my_hash.set('ted', 29292929)
my_hash.set('eat_chikin', 259)
my_hash.set('tuesday', 5)
my_hash.set('ski', 25)
my_hash.set('Ski', 25)
my_hash.set('Fri', 4)
print(my_hash)
print(my_hash.keys())
print(my_hash.values())
