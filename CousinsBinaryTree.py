# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#-----------------------------------------DFS, Time = O(no of nodes), Space= O(height of the tree)-----------------
# class Solution:
#     def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
#         if root == None:
#             return False
#         self.x_parent = None
#         self.y_parent = None
#         self.x_lvl = None
#         self.y_lvl = None

#         self.dfs (root = root, parent=None, lvl = 0, x=x, y=y)
#         return self.x_parent != self.y_parent and self.x_lvl == self.y_lvl

#     def dfs(self, root: Optional[TreeNode], parent:Optional[TreeNode],lvl: int, x: int, y: int)-> None:
#         # base case
#         if root == None:
#             return
        
#         # logic
#         if root.val == x:
#             self.x_parent = parent
#             self.x_lvl = lvl
#             return # Dont go further if found
#         if root.val == y:
#             self.y_parent = parent
#             self.y_lvl = lvl
#             return
            

#         self.dfs(root = root.left, parent=root, lvl = lvl+1, x=x, y=y)
#         self.dfs(root = root.right, parent=root, lvl = lvl+1, x=x, y=y)

#------------------------------------------------BFS-------------------------------------------------------------
from queue import Queue
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root == None:
            return False
        x_found = False
        y_found = False
        q = Queue()
        q.put(root)

        while not q.empty():
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                if curr.val == x:
                    x_found = True
                if curr.val == y:
                    y_found = True
                if curr.left != None and curr.right != None:
                    if curr.left.val == x and curr.right.val == y:
                        return False
                    if curr.left.val == y and curr.right.val == x:
                        return False
                if curr.left != None:
                    q.put(curr.left)
                if curr.right != None:
                    q.put(curr.right)
            if x_found == True and y_found==True:
                return True
            if x_found == True or y_found == True:
                return False
        
        return False

        

