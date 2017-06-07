#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].

解题思路：一种巧妙的解法。使用两个指针prev和curr，判断A[curr]是否和A[prev]、A[prev-1]相等
，如果相等curr指针继续向后遍历，直到不相等时，将curr指针指向的值赋值给A[prev+1]，这样多余
的数就都被交换到后面去了。最后prev+1值就是数组的长度。
'''

class Solution1:
    # @param A a list of integers
    # @return an integer
    # @it's a good solution!
    def removeDuplicates(self, A):
        if len(A) <= 2: return len(A)
        prev = 1;
        curr = 2
        while curr < len(A):
            if A[curr] == A[prev] and  A[curr] == A[prev - 1]:
                curr += 1
            else:
                prev += 1
                A[prev] = A[curr]
                curr += 1
        return prev + 1

class Solution2:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return(len(A))
        count = 2
        for i in range(2,len(A)):
            if A[i] != A[count-1] or A[i] != A[count-2]:
                A[count] = A[i]
                count += 1
        return count

solution = Solution1()
test_String = [1,2,3,3,3,3,4,4,5,7,7,8,8,9]
ans = solution.removeDuplicates(test_String)
print(ans)

solution2 = Solution2()
test_String = [1,2,3,3,3,3,4,4,5,7,7,8,8,9]
ans = solution2.removeDuplicates(test_String)
print(ans)
