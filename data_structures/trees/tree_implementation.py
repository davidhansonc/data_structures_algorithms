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
        if self.root == None:
            return 'Empty Tree'
        else:
            return str(self.__traverse(self.root))


    def __traverse(self, node):
        tree = {
            'value': node.value
        }
        if node.right:
            tree['right node'] = self.__traverse(node.right)
        else:
            tree['right node'] = 'None'
        if node.left:
            tree['left node'] = self.__traverse(node.left)
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
                    return
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
        parent_node = None
        current_node = self.root
        last_direction_taken = ""
        while True:
            # Deletes root node when there are no children
            if self.root.left == None and self.root.right == None:
                self.root = None
                return
            # The following two statements traverse through the tree to locate node
            elif value > current_node.value: 
                parent_node = current_node
                current_node = current_node.right
                last_direction_taken = "right"
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
                last_direction_taken = "left"
            # These statements deal with the removal once node is found
            elif value == current_node.value:
                self.__node_removal(parent_node, current_node, last_direction_taken)
                return


    def __node_removal(self, parent_node, current_node, prev_direction):
        # Node to delete is a leaf
        if current_node.right == None and current_node.left == None:
            if prev_direction == "right":
                parent_node.right = None
            elif prev_direction == "left":
                parent_node.left = None
        # Node to delete has only left children
        elif current_node.right == None and prev_direction == "right":
            parent_node.right = current_node.left
        elif current_node.right == None and prev_direction == "left":
            parent_node.left = current_node.left
        # Node to delete has no left grandchildren
        elif current_node.right.left == None and prev_direction == "right":
            parent_node.right = current_node.right
        elif current_node.right.left == None and prev_direction == "left":
            parent_node.left = current_node.right
        # Node to delete has a left grandchild
        elif current_node.right.left and prev_direction == "right":
            special_node = current_node.right.left
            parent_node.right = special_node
            special_node.right = current_node.right
            special_node.left = current_node.left
            current_node.right.left = None
        return



tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(14)
tree.insert(20)
tree.insert(18)
tree.insert(22)
print(tree)
tree.remove(15)
print('\n')
print(tree)