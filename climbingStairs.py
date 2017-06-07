#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这其实是一道组合数学的题目，总共有n步台阶，每次只能走一步或者两步，总共有多少种走法。
这个问题可以这样思考：假设已知有n步台阶共有f(n)种走法，对于n+1步台阶由两部分组成：一个是
前面n步台阶的f(n)种走法后直接一步到达n+1；另一种是前面n-1步台阶的f(n-1)种走法后走两步到
达n+1。因此可以得到递推关系是：f(n+1) = f(n) + f(n-1)。代码如下：
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        f = [1, 2]
        for i in range(2,n):
            f.append(f[i-2] + f[i-1])
        return f

solution = Solution()
test_String = '1234698432198'
ans = solution.climbStairs(20)
print(test_String)
print(ans)
