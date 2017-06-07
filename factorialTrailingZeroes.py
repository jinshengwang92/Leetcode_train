#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions

class Solution1:
    # @return an integer
    def trailingZeroes(self, n):
        tmp = 5
        result = 0
        while n >= tmp:
            print(n//tmp)
            result += n//tmp
            tmp *= 5
            #print(tmp)
        return(result)

class Solution2:
    # @return an integer
    def trailingZeroes(self, n):
        res = 0
        x = 5
        while( n >= x):
            res += n/x
            x *= 5
        return res


solution = Solution1()
test_String = 100
ans = solution.trailingZeroes(test_String)
print(test_String)
print(ans)
