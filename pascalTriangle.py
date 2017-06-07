#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution1:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        if numRows > 2:
            list = [[] for i in range(numRows)]
            for i in range(0, numRows):
                list[i] = [1 for j in range(i + 1)]
            for i in range(2, numRows):
                for j in range(1, i):
                    list[i][j] = list[i - 1][j - 1] + list[i - 1][j]
            return list

class Solution2:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 1:
            return([[1]])
        elif numRows == 2:
            return([[1],[1,1]])
        elif numRows == 0:
            return([])
        else:
            result = [[1],[1,1]]
            for i in range(3, numRows+1):
                tmp = [1]*i
                last = result[i-2]
                for j in range(1,(i-1)//2 + 1):
                    tmp[j] = tmp[i-1-j] = last[j-1] +last[j]
                result.append(tmp)
            return(result)

solution = Solution1()
ans = solution.generate(6)
print(ans)
