# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-27 15:58:39
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-28 10:37:25
import pdb

class Node():

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


    def __str__(self):
        node_dict = {
            'value': self.value,
            'left': self.left,
            'right': self.right
        }
        return str(node_dict)


class BinarySearchTree():

    def __init__(self):
        self.root = None
        self.node_number = 0


    def __str__(self):
        pass


    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            traverse = self.root
            while traverse.left != new_node and traverse.right != new_node:
                if value > traverse.value:
                    if traverse.right == None:
                        traverse.right = new_node
                    else:
                        traverse = traverse.right
                elif value < traverse.value:
                    if traverse.left == None:
                        traverse.left = new_node
                    else:
                        traverse = traverse.left
                elif value == traverse.value:
                    return "no duplicates allowed"
        self.node_number += 1
        return


    def lookup(self, value):
        if self.root == None:
            return "tree is empty"
        else:
            traverse = self.root
            try:
                while True:
                    if value > traverse.value:
                        traverse = traverse.right
                    elif value < traverse.value:
                        traverse  = traverse.left
                    elif value == traverse.value:
                        return traverse
            except AttributeError:
                return "item not found"


    def remove(self, value):
        if self.root == None:
            return "tree is empty"
        # add case for node to remove is the root node
        else:
            parent_node = None
            current_node = self.root
            last_dir_taken = ""
            while True:
                if value > current_node.value:
                    parent_node = current_node
                    current_node = current_node.right
                    last_dir_taken = "right"
                elif value < current_node.value:
                    parent_node = current_node
                    current_node  = current_node.left
                    last_dir_taken = "left"

                elif value == current_node.value:
                    # This statement deletes the node if it is a leaf
                    if current_node.right == None and current_node.left == None:
                        if last_dir_taken == "right":
                            parent_node.right = None
                        elif last_dir_taken == "left":
                            parent_node.left = None
                        return
                    # This statement deletes the node if it is not a leaf...


my_tree = BinarySearchTree()
my_tree.insert(9)
my_tree.insert(4)
my_tree.insert(2)
my_tree.insert(2)
my_tree.insert(10)
my_tree.insert(3)
# my_tree.remove(3)
