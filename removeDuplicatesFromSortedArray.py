#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
Given a sorted array, remove the duplicates in place such that each element
appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place
with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

解题思路：使用一个指针j，当i向后遍历数组时，如果遇到与A[j]不同的，将A[i]和A[j+1]交换，
同时j=j+1，即j向后移动一个位置，然后i继续向后遍历。
'''
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                A[i], A[j+1] = A[j+1], A[i]
                j = j + 1
        return j+1

class Solution2:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A == []:
            return(0)
        count = 1
        for i in range(1,len(A)):
            if A[i] != A[i-1]:
                A[count] = A[i]
                count += 1
        return(count)

solution = Solution()
test_String = [1,2,3,3,3,3,4,4,5,7,7,8,8,9]
ans = solution.removeDuplicates(test_String)
print(ans)

solution = Solution2()
test_String = [1,2,3,3,3,3,4,4,5,7,7,8]
ans = solution.removeDuplicates(test_String)
print(ans)
