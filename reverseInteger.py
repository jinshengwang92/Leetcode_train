#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这个题是将一个整数逆序输出，当然如果是负数，符号不需要逆序。做法就是将其转化为字符串，
然后逆序即可。需要注意的陷阱就是当你逆序之后，该数可能超出了最大值2^31 - 1，需要做判断。
'''
class Solution:
    # @return an integer
    def reverse(self, x):
        if x >=0:
            x = str(x)  # Convert to string
            if int(x[::-1]) > (2 ** 31-1):
                return 0;
            else:
                return(int(x[::-1])) # reverse
        else:
            x = str(-x)
            if int("-" + x[::-1]) < -2 ** 31:
                return 0
            else:
                return(int("-" + x[::-1]))

solution = Solution()
test_String = -123434+323232
ans = solution.reverse(test_String)
print(ans)
