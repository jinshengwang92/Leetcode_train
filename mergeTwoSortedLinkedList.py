#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
题意：Merge two sorted linked lists and return it as a new list. The new list
should be made by splicing together the nodes of the first two lists.

解题思路：合并两个已经排好序的链表。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy = ListNode(0)
        tmp = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next
            else:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next
        if l2 == None:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next


class Solution2:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        result = ListNode(0)
        cur = result
        while l1 or l2:
            tmp = ListNode(0)
            if l1 and not l2:
                tmp = l1
                l1 = l1.next
            elif l2 and not l1:
                tmp = l2
                l2 = l2.next
            else:
                if l1.val < l2.val:
                    tmp = l1
                    l1 = l1.next
                else:
                    tmp = l2
                    l2 = l2.next
            cur.next, cur = tmp, tmp
        return(result.next)


solution = Solution()
test_String = '1234698432198'
ans = solution.singleNumber(test_String)
print(test_String)
print(ans)
