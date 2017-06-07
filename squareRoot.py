#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
Calculate the root of a value without using sqrt or other mudules functions.
'''

class Solution1:
    # @ x the original value
    # @ eta the acceptable error
    def squareRoot(self,x,eta):
        ans = 1.0
        while abs(ans-sqrt(x*1.0))>=eta:
            ans = (ans+x/ans)/2.0
        return ans
from math import sqrt
solution = Solution1()
test_String = 12
test_eta = 0.2
ans = solution.squareRoot(test_String,test_eta)
print(test_String)
print(ans)
