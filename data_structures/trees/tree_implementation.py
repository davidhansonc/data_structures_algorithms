# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-27 15:58:39
# @Last Modified by:   David Hanson
# @Last Modified time: 2021-01-31 20:56:35
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
        return str(self._traverse(self.root))


    def _traverse(self, node):
        tree = {
            'value': node.value
        }
        if node.right:
            tree['right node'] = self._traverse(node.right)
        else:
            tree['right node'] = 'None'
        if node.left:
            tree['left node'] = self._traverse(node.left)
        else:
            tree['left node'] = 'None'
        return tree


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


'''
    def remove(self, value):
        if self.root == None:
            return "tree is empty"
        # add case for node to remove is the root node
        else:
            parent_node = None
            current_node = self.root
            last_dir_taken = ""
            parent_of_node_found = None
            node_found = None
            while True:
                if value > current_node.value and node_found == None:
                    parent_node = current_node
                    current_node = current_node.right
                    last_dir_taken = "right"
                elif value < current_node.value and node_found == None:
                    parent_node = current_node
                    current_node = current_node.left
                    last_dir_taken = "left"

                elif value == current_node.value:
                    parent_of_node_found = parent_node
                    node_found = current_nod                                        e
                    # This statement deletes the node if it is a leaf
                    if current_node.right == None and current_node.left == None:
                        if last_dir_taken == "right":
                            parent_node.right = None
                        elif last_dir_taken == "left":
                            parent_node.left = None
                        return
                    # This statement deletes the node if it is not a leaf and only left child exists.
                    # Left child then replaces the node begin deleted.
                    elif current_node.right == None and last_dir_taken = "right":
                        parent_node.right = current_node.left
                        return
                    elif current_node.right == None and last_dir_taken = "left":
                        parent_node.left = current_node.left
                        return
                    # Case when right child exists...
                    else:
                        parent_node = current_node
                        current_node = current_node.right
                        last_dir_taken = "right"
                # elif node_found:
'''


tree = BinarySearchTree()
tree.insert(6)
tree.insert(4)
tree.insert(10)
print(tree)