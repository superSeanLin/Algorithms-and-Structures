# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Recursive method, slower than tracking through the whole linked list with carriers
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.List2Num(l1)
        num2 = self.List2Num(l2)
        print(num1, num2, num1+num2)
        l3 = self.Num2List(num1+num2)
        return l3
    
    def List2Num(self, l):
        if not l.next:
            return l.val
        res = l.val + self.List2Num(l.next) * 10
        return res
    
    def Num2List(self, num):
        num_curr = num % 10
        num_next = num // 10 # num / 10 will introduce computational error
        if num_next <= 0:
            return ListNode(num_curr)
        res = ListNode(num_curr)
        res.next = self.Num2List(num_next)
        return res
        
