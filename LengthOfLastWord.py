#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
求一行字符串中最后一个单词的长度，这个题用python做就非常简单了
'''
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWords(self,s):
        if len(s)==0:
            return 0
        split_words = s.split()
        print(split_words)
        if len(split_words[-1]) == 0:
            return 0
        return len(s.split()[-1])

#end class

solution = Solution()
test_String = 'I am a good boy, are you ?'
ans = solution.lengthOfLastWords(test_String)
print(test_String)
print(ans)
