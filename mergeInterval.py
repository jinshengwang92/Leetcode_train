#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
A list consists of sub lists representing the start and end point of line segments
calculte the total length covered by all the line segments
'''
class solution2:
    # @ lists, the intervals of small xianduan
    # return the total length covered on the axis
    def totalLength(self,lists):
        if lists == []:
            return 0
        sorted_lists = sorted(lists,key=lambda x:x[0])
        final_stack = [sorted_lists[0]]
        for ele in sorted_lists[1:]:
            last_ele = final_stack[-1]
            if last_ele[1] < ele[0]:
                final_stack.append(ele)
            else:
                final_stack[-1]=[last_ele[0],max(last_ele[1],ele[1])]
        return sum([x[1]-x[0] for x in final_stack])

def main():
    # general test
    intervals1 = [[-4,5],[0,1],[2.5,60],[2,3]]
    test = solution2()
    ans1 = test.totalLength(intervals1)
    print(ans1)
    # test a vacant list
    interval2 = []
    ans2 = test.totalLength(interval2)
    print(ans2)

if __name__ =="__main__":
    main()
