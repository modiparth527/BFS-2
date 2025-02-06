# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.dfs(root=root, lvl=0)
        return self.result
    
    def dfs(self, root:Optional[TreeNode], lvl: int) -> None:
        if root is None:
            return
        
        if lvl == len(self.result):
            self.result.append(root.val)
        else:
            self.result[lvl] = root.val
                
        self.dfs(root.left, lvl + 1) #---------------Root,left,right so we need else condition
        self.dfs(root.right, lvl + 1)
    
    # def dfs(self, root:Optional[TreeNode], lvl: int) -> None:
    #     if root is None:
    #         return
        
    #     if lvl == len(self.result):
    #         self.result.append(root.val)

                
    #     self.dfs(root.right, lvl + 1) #---------------Root,right,left so we DO NOT need else condition
    #     self.dfs(root.left, lvl + 1)


#----------------------------BFS Time = O(n), Space = O(n/2) = O(n)---------------------------------------------------------------

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        q = Queue()
        q.put(root)

        while not q.empty():
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                if i == size - 1:
                    result.append(curr.val)
                if curr.left != None:
                    q.put(curr.left)
                if curr.right != None:
                    q.put(curr.right)
        return result

