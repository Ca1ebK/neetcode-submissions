# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # 1. BASE CASES (When do we stop?)
        # If we hit the bottom, or if we find p, or if we find q: return the current node.
        if root == None or root == p or root == q:
            return root

        # 2. THE SEARCH (Press pause, wait for clones)
        left_search = self.lowestCommonAncestor(root.left, p, q)
        right_search = self.lowestCommonAncestor(root.right, p, q)

        # 3. THE RECOMBINATION (Look at what the clones brought back)
        
        # If BOTH clones brought something back, they split at this exact node!
        if left_search != None and right_search != None:
            return root
        
        # If ONLY the left clone brought something back, pass it upwards!
        elif left_search != None:
            return left_search
            
        # If ONLY the right clone brought something back, pass it upwards!
        elif right_search != None:
            return right_search
            
        # If neither found anything (this handles leaves)
        else:
            return None