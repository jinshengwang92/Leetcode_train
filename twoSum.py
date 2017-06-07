#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
需找出一个列表中是否有两个数的和为一个给定的数，并返回这两个数的下标。需要用到python里面的字典（相当于hash表），判断第i个数前面是否有一个数的值为target - num[i]。代码如下：
'''
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        tmp = {}
        for i in range(len(num)):
            if target - num[i] in tmp:
                return(tmp[target - num[i]] +1, i + 1)
            else:
                tmp[num[i]] = i;
#end class


solution = Solution()
test_num = [1,2,5,6,7,10,90]
test_target = 100
ans = solution.twoSum(test_num,test_target)
print(ans)
