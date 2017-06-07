#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]
解题思路：这题需要将根到叶子的路径和为sum的路径都枚举出来。一样是使用递归。
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# this is path sum 2 to determine if certain path exist and output that
class Solution1:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        def dfs(root, currsum, valuelist):
            if root.left==None and root.right==None and currsum==sum:
                res.append(valuelist)
            if root.left:
                #dfs stands for depth first search
                dfs(root.left, currsum+root.left.val, valuelist+[root.left.val])
            if root.right:
                dfs(root.right, currsum+root.right.val, valuelist+[root.right.val])

        if root == None:
            return []
        res=[]
        dfs(root, root.val, [root.val])
        return res

'''
These below two solutions only for path sum type 1, which does not require the
output of the exact path
'''
class Solution2:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        result = False
        if root == None:
            return result
        else:
            sum -= root.val
            if sum == 0 and root.left == None and root.right == None:
                result = True
                return result
            else:
                if root.left:
                    result = result or self.hasPathSum(root.left, sum) # 只要存在一条就返回True
                if root.right:
                    result = result or self.hasPathSum(root.right, sum)
                return(result)


class Solution3:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    '''
    # I see this as the shortest and easiest code so far
    '''
    def hasPathSum(self, root, sum):
        if root==None:
            return False
        if root.val==sum and root.left==None and root.right==None:
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)

solution = Solution()
test_String = '1234698432198'
ans = solution.singleNumber(test_String)
print(test_String)
print(ans)
