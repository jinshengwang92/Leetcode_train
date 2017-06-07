#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
Given a binary tree, find its max depth.
The maximum depth is the number of nodes along the longest path from the root
node down to the nearest leaf node.
解题思路：分几种情况考虑：1，树为空，则为0。 2，根节点如果只存在左子树或者只存在右子树，
则返回值应为左子树或者右子树的（最da深度+1）。 3，如果根节点的左子树和右子树都存在，
则返回值为（左右子树的最da深度的较小值+1）。
'''

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return self.maxDepth( root.right ) + 1
        if root.left != None and root.right == None:
            return self.maxDepth( root.left ) + 1
        return max( self.maxDepth( root.left ), self.maxDepth( root.right ) ) + 1


solution = Solution()
test_String = '1234698432198'
ans = solution.singleNumber(test_String)
print(test_String)
print(ans)
