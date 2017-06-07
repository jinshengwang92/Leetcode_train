#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这个题更加巧妙，题目与上一个题目类似，不过这一次序列中的数字除了某一个数字外都出现3次，
需要找出这个数字，先贴代码再解释
'''


class Solution:
    #这一次序列中的数字除了某一个数字外都出现3次，需要找出这个数字
    # @param A, a list of integer
    # @return an integer
    def singleNumber32(self, A):
        ones, twos = 0, 0
        for ele in A:
            ele = int(ele)
            ones = ones^ele & ~twos
            twos = twos^ele & ~ones
        return(ones)

    # end def

    def singleNumberMN(self,A,m,n):
        # 序列中所有的数字都出现m次，只有一个数字出现n次（m>n），请找出这个只出现n次的数字
        tmp = [0]*(m-1)
        for ele in A:
            ele = int(ele)
            for i in range(m-1):
                tmp[i] = tmp[i]^ele
                for j in range(m-1):
                    if i != j:
                        tmp[i] = tmp[i] & ~tmp[j]
        return(tmp[n-1])
    # end def

# end class



solution = Solution()
test_String = '22233355999'
ans = solution.singleNumberMN(test_String,3,2)
print(test_String)
print(ans)
