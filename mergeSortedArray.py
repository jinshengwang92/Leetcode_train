#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这个题目的意思是把两个排好序的序列合并为一个排好序的序列，本来我最开始想的是直接把两个序列拼接
在一起，然后用python列表里面自带的sort函数排个序就Ok了，但是这样做的复杂度至少
是O((m+n)log(m+n))的，另外一种O(m+n)做法是从后面往前面排，比如合并后的最后一个
数A[m+n-1]就应该等于A[m-1]和B[n-1]中较大的一个以此类推，这样可以避免从前往后需要移动的操作，
需要注意的特列就是A和B中某一个为空
'''

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        # first 判断A、B是否为空
        if m == 0:
            return B
        if n == 0:
            return A
        result = [None]*(m+n)
        for i in list(range(0,m+n))[::-1]:
            #print(i)
            if B[n-1] >= A[m-1] and n>=1:
                result[i] = B[n-1]
                n -= 1
            elif m>=1:
                result[i] = A[m-1]
                m -= 1
        return(result)

solution = Solution()
A = [1,4,5,7,8,11,25,30]
#A = []
B = [1,3,5,6,9,12]
#B = []
ans = solution.merge(A,len(A),B,len(B))
#print(test_String)
print(ans)
