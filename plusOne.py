#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
这个题就是实现大数（用数组存储）加1的功能。需要注意的就是满十进一这个规则，
以及类似999+1=1000需要在第一位添一个1这种特例
'''
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] = (digits[i] + 1) % 10 # 加1模10，如果没有进位则跳出循环，否则高一位加1
            print(i,digits[i])
            if digits[i]:
                flag = 0
                break
        if flag: # 如果每一位都进位了，则在数组第一位添加1
            digits.insert(0,1)
        return digits


solution = Solution()
test_String = [9]
ans = solution.plusOne(test_String)
#print(test_String)
print(ans)
