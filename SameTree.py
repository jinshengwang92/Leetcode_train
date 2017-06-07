#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这个题的意思非常简单，给定两颗二叉树，判断这两颗二叉树是否相同。树相同包括两点：一是结构相同，
而是值相同。因此我们只需要对两棵树同时遍历)(简单的递归)一遍，遇到不同（结构不同或者值不同）
时则返回False；若遍历一遍之后没有发现不同则说明这两棵树相同
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
         self.right = None
# end class

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return(True)
        elif p == None or q == None:
            return(False)
        else:
            if p.val != q.val:
                return(False)
            else:
                if self.isSameTree(p.left, q.left):
                    return(self.isSameTree(p.right, q.right))
                else:
                    return(False)

class Solution2:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False



solution = Solution()
test_String = '1234698432198'
ans = solution.singleNumber(test_String)
print(test_String)
print(ans)
