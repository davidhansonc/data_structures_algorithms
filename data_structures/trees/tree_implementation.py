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
        # Deletes root node when there are no children
        if self.root.left == None and self.root.right == None:
            self.root = None
        else:
            parent_node = None
            current_node = self.root
            last_dir_taken = ""
            while True:
                # The following two statements traverse through the tree to locate node
                if value > current_node.value: 
                    parent_node = current_node
                    current_node = current_node.right
                    last_dir_taken = "right"
                elif value < current_node.value:
                    parent_node = current_node
                    current_node = current_node.left
                    last_dir_taken = "left"
                # These statements deal with the removal once node is found
                elif value == current_node.value:
                    # Node to delete is a leaf
                    if current_node.right == None and current_node.left == None:
                        if last_dir_taken == "right":
                            parent_node.right = None
                        elif last_dir_taken == "left":
                            parent_node.left = None
                        return
                    # Node to delete has only left children
                    elif current_node.right == None and last_dir_taken == "right":
                        parent_node.right = current_node.left
                        return
                    elif current_node.right == None and last_dir_taken == "left":
                        parent_node.left = current_node.left
                        return
                    # Node to delete has no left grandchildren
                    elif current_node.right.left == None and last_dir_taken == "right":
                        parent_node.right = current_node.right
                        return
                    elif current_node.right.left == None and last_dir_taken == "left":
                        parent_node.left = current_node.right
                        return
                    # Node to delete has a left grandchild
                    elif current_node.right.left and last_dir_taken == "right":
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