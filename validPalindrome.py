#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

''' this is my test of leetcode solutions
这个题是判断一个字符串是否是回文，回文的意思是
正序和逆序都一样，所以这也成了我们判断的标准，这个题的回文是不区分大小写的，因此首先可以将所有字
母转为小（大）写，需要注意的是它这里只关注字母和数字，因此其他的符号需要去掉，需要用到了python
的正则表达式
'''
import re  #正则表达式包含在re里面
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower() # 首先将字符串转为小写
        s = re.sub('[^A-Za-z0-9]','',s) # 正则表达式去除非字母和数字的符号
        #s = re.sub('[\W]+|_','',s)
        # 如果是回文，即正序和逆序一样
        print(s)
        return s==s[::-1]
# end class

solution = Solution()
test_String = '9908*80**88_099'
ans = solution.isPalindrome(test_String)
print(test_String)
print(ans)
