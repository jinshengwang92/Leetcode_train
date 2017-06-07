#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这个题是判断一棵树是不是对称树。我们可以根据上一个题来解决这个问题
有代码可知，我们首先把这个树分成左右两颗子树，然后遍历这两颗子树，
比较时不再是左边和左边的比，因为对称，所以比较左子树的左节点和右子树
的右节点以及左子树的右节点和右子树的左节点是否相等即可。
'''
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return(True)
        else:
            return(self.isSameTree(root.left, root.right))
    def isSameTree(self, p, q):
        if p == None and q == None:
            return(True)
        elif p == None or q == None:
            return(False)
        else:
            if p.val != q.val:
                return(False)
            else:
                if self.isSameTree(p.left, q.right):
                    return(self.isSameTree(p.right, q.left))
                else:
                    return(False)

solution = Solution()
test_String = '1234698432198'
ans = solution.singleNumber(test_String)
print(test_String)
print(ans)
