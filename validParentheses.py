#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这道题是判断括号是否匹配，就是利用栈来进行解决，遇到正括号加入栈(初始化的栈为none以防最后一个
是右括号但是pop不出来东西比较)，遇到反括号弹出栈看是否匹配，
只不过刚开始时可以直接排除一些结果：1）如果字符串的长度为奇数，必然False（这个要求有点勉强，
可以有其他字符使得总长为基数）；2）如果最后一个字
符是‘（’‘[’‘{’，必然false；3）第一个字符为‘）’‘]’‘}’必然False等
'''
class Solution:
    # @return a boolean
    def isValid(self, s):
        if s[-1] == '(' or s[-1] =='[' or s[-1] =='{' \
            or s[0] == ')' or s[0] == ']' or s[0]=='}':
            return False
        pa_stack = [None]
        for i in range(len(s)):
            if s[i] =='(' or s[i] =='[' or s[i] =='{':
                pa_stack.append(s[i])
            else:
                #if len(pa_stack) == 0:
                #    return False
                if s[i] == ')' and pa_stack.pop() != '(':
                    return False
                if s[i] == ']' and pa_stack.pop() != '[':
                    return False
                if s[i] == '}' and pa_stack.pop() != '{':
                    return False
        return True
#end class

solution = Solution()
test_String = 'aa{{{[]}}}ccc343432[]}'
ans = solution.isValid(test_String)
print(test_String)
print(ans)
