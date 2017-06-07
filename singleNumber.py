#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这个题和下一个题都很有技巧，这个题的意思是给定一个序列，这个序列中的数除了有一个数只出现过
一次外，其他的数都出现两次，请找出这个只出现一次的数。最直观的想法就是遍历一遍把每个数出现
的次数都存起来，然后再看谁的次数为1。但是网上有一种更加简洁而巧妙地方法，用异或来解决这个
问题，他的思想是两个相同的数异或为0,0和任何数异或为任何数，这样只需要把整个序列全都异或一遍，
最后得到的数就是想要的答案了
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
        # 相同元素异或为0,0与任何数异或等于任何数，有a^b^a = b 交换元素位置
        # 此外，异或还可以用于两个元素交换a=a^b^(b=a)
            result = result^int(i)
            print(result)
        return(result)
# end class

solution = Solution()
test_String = '1234698432198'
ans = solution.singleNumber(test_String)
print(test_String)
print(ans)
