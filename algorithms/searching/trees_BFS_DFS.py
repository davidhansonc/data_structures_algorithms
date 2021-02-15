# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-27 15:58:39
# @Last Modified by:   David Hanson
# @Last Modified time: 2021-01-31 20:56:35
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
        if self.root == None:
            return 'Empty Tree'
        else:
            return str(self._traverse(self.root))


    def _traverse(self, node):
        tree = {
            'value': node.value
        }
        if node.left:
            tree['left node'] = self._traverse(node.left)
        else:
            tree['left node'] = 'None'
        if node.right:
            tree['right node'] = self._traverse(node.right)
        else:
            tree['right node'] = 'None'
        return tree


    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            self.__traverse_to_insert(new_node, self.root)
        self.node_number += 1
        return


    def __traverse_to_insert(self, node_to_insert, origin_node):
        current_node = origin_node
        while current_node.left != node_to_insert and current_node.right != node_to_insert:
            if node_to_insert.value > current_node.value:
                if current_node.right == None:
                    current_node.right = node_to_insert
                else:
                    current_node = current_node.right
            elif node_to_insert.value < current_node.value:
                if current_node.left == None:
                    current_node.left = node_to_insert
                else:
                    current_node = current_node.left
            elif value == current_node.value:
                return


    def lookup(self, value):
        if self.root == None:
            return "tree is empty"
        else:
            return self.__traverse_to_lookup(value, self.root)


    def __traverse_to_lookup(self, value_to_add, origin_node):
            current_node = origin_node
            while current_node:
                if value_to_add > current_node.value:
                    current_node = current_node.right
                elif value_to_add < current_node.value:
                    current_node  = current_node.left
                elif value_to_add == current_node.value:
                    return current_node
            return "item not found"

    
    def remove(self, value):
        parent_node = None
        current_node = self.root
        last_direction_taken = ""
        while current_node:
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
                return current_node
        return print("item not in tree")


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
    

    def breadth_first_search_iter(self):
        node = self.root
        queue = [self.root]
        collection = []
        while len(queue) > 0:
            collection.append(node.value)
            queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if len(queue) > 0:
                node = queue[0]
        return collection

    
    def breadth_first_search_rec(self):
        return self._bfs_r([self.root], [])

    
    def _bfs_r(self, queue, result_list):
        node = queue[0]
        result_list.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right: 
            queue.append(node.right)
        queue.pop(0)
        if len(queue) > 0:
            return self._bfs_r(queue, result_list)
        else:
            return result_list
                

    def dfs_inorder_rec(self):
        return self._dfs_inorder_traversal(self.root, [])

    
    def _dfs_inorder_traversal(self, node, result_list):
        if node.left:
            self._dfs_inorder_traversal(node.left, result_list)
        result_list.append(node.value)
        if node.right:
            self._dfs_inorder_traversal(node.right, result_list)
        return result_list
    

    def dfs_preorder_rec(self):
        return self._dfs_preorder_traversal(self.root, [])
    

    def _dfs_preorder_traversal(self, node, result_list):
        result_list.append(node.value)
        if node.left:
            self._dfs_preorder_traversal(node.left, result_list)
        if node.right:
            self._dfs_preorder_traversal(node.right, result_list)
        return result_list
    

    def dfs_postorder_rec(self):
        return self._dfs_postorder_traversal(self.root, [])
    

    def _dfs_postorder_traversal(self, node, result_list):
        if node.left:
            self._dfs_postorder_traversal(node.left, result_list)
        if node.right:
            self._dfs_postorder_traversal(node.right, result_list)
        result_list.append(node.value)
        return result_list
                

    def get_leaves(self):
        return self._leaves_r(self.root, [])

    
    def _leaves_r(self, node, leaves):
        if node.left:
            self._leaves_r(node.left, leaves)
        else:
            leaves.append(node.value)
        if node.right:
            self._leaves_r(node.right, leaves)
        return leaves


tree = BinarySearchTree()
tree.insert(10)
tree.insert(15)
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(2)
tree.insert(6)
tree.insert(9)
tree.insert(8)
tree.insert(20)
tree.insert(14)
tree.insert(18)
tree.insert(22)
print(tree)
print('\n')
print(tree.dfs_inorder_rec())
print(tree.dfs_preorder_rec())
print(tree.dfs_postorder_rec())
print(tree.breadth_first_search_iter())
print(tree.breadth_first_search_rec())
print(tree.get_leaves())