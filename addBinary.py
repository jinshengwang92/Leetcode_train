#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
这个题目非常简单，就是二进制的加法。对于我们这种python的初学者来说难点是字符串与列表的转化，
题目本身需要注意的一个地方就是，最后可能由于进位需要补一位，我们可以先把字符串先倒一转再加，
这样就可以在末尾补位。代码如下
'''
class Solution1:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        return bin(int(a,2) + int(b,2))[2:]

class Solution2:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a = a[::-1] # 字符串倒序
        b = b[::-1] # 字符串倒序
        i = j = 0
        c = []
        add = 0 # 表示进位
        while i < len(a) or j < len(b):
            if i < len(a) and j < len(b):
                tmp = (int(a[i]) + int(b[j]) + add) % 2
                c.append(str(tmp))
                if (int(a[i]) + int(b[j]) + add) >= 2:
                    add = 1
                else:
                    add = 0
                i += 1
                j += 1
            if i < len(a) and j>= len(b):
                tmp = (int(a[i]) + add)%2
                c.append(str(tmp))
                if (int(a[i]) + add) >= 2:
                    add = 1
                else:
                    add = 0
                i += 1
            if i >= len(a) and j < len(b):
                tmp = (int(b[j]) + add)%2
                c.append(str(tmp))
                if (int(b[j]) + add) >= 2:
                    add = 1
                else:
                    add = 0
                j += 1
        if add:
            c.append('1')
        c = c[::-1]
        result = "".join(c)
        return(result)

class Solution3:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        length_a = len(a)
        length_b = len(b)
        length = max(length_a,length_b)
        if length_a > length_b:
            b = '0' * (length_a - length_b) + b
        else:
            a = '0' * (length_b - length_a) + a
        a = a[::-1]
        b = b[::-1]
        Sum = ''
        carry = 0
        for i in range(length):
            tmp_sum = int(a[i])+int(b[i]) + carry
            this_val = int(tmp_sum%2)
            Sum = Sum + (str(this_val))
            carry = (tmp_sum-this_val )/2
        if carry == 1:
            Sum = Sum + '1'
        return Sum[::-1]

solution = Solution1()
a = "1101"
b = "1110"
ans = solution.addBinary(a,b)
print(ans)


solution2 = Solution2()
a = "1101"
b = "1110"
ans = solution2.addBinary(a,b)
print(ans)

solution3 = Solution3()
a = "1101"
b = "1110"
ans = solution3.addBinary(a,b)
print(ans)
