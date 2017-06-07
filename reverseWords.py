#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这个题的意思是，给定一个字符串，字符串是以单词的形式拼接起来的，需要做的就是把字符串里面的
单词逆序输出，但是单词内的顺序是不变的，相信看它的例子大家都能明白。这个题目用python里面的
列表的话就非常简单，首先将字符串按“ ”分割，然后去掉分割出来的列表中空格（因为两个单词间可能
有多个空格，这是这个题目的陷阱），最后列表倒序再以空格拼接成字符串输出即可
'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        tmp = s.split(' ') # 将字符串分割为列表
        while '' in tmp:   # 清除空元素
            tmp.remove('')
        tmp.reverse()      # 列表倒序
        tmp = ' '.join(tmp) #列表转化为字符串，并以空格连接
        return(tmp)

# end class

solution = Solution()
test_String = 'abs 990 999   543'
ans = solution.reverseWords(test_String)
print(test_String)
print(ans)
