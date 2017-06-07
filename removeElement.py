#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这个题目的意思是去掉序列中规定的元素之后求剩下的序列的长度，非常简单，代码如下
'''
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        while elem in A:
            A = A.replace(elem,'')
        return(A,len(A))

solution = Solution()
test_A = '123445632'
test_elem = '2'
ans = solution.removeElement(test_A,test_elem)
print(test_A)
print(ans)
