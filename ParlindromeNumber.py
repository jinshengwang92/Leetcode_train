#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
Determine whether an integer is a palindrome. Do this without extra space.
Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

解题思路：不允许用额外空间，所以不能将数转换成字符串来判断.
'''
class Solution1:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 1
        while x//div >= 10:
            div = div * 10

        while x:
            left = x // div
            right = x % 10

            if left != right:
                return False

            x = ( x % div ) // 10
            div = div / 100
        return True

class Solution2:
    # @return a boolean
    def isPalindrome(self, x):
        mode, result= 1, True
        while x//mode >= 10: ## 相当于算出有多少位
            mode *= 10
        while x:
            if x // mode != x % 10:
                result = False
                return(result)
            x -= mode*(x//mode)
            x //= 10
            mode //= 100
        return(result)

solution = Solution1()
test_String = 92029
ans = solution.isPalindrome(test_String)
print(test_String)
print(ans)
