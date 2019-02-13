# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        ## similar to copy the graph
        ## faster: create linked list first and then connect random
        if not head:
            return head
        res = self.dfs(head, {})
        return res
    
    def dfs(self, head, booker):
        if not head in booker:
            node = RandomListNode(head.label)
            booker[head] = node
        else:
            node = booker[head]
        node.next, node.random = None, None
        if head.next:
            if head.next in booker:
                node.next = booker[head.next]
            else:
                node.next = self.dfs(head.next, booker)
        if head.random:
            if head.random in booker:
                node.random = booker[head.random]
            else:
                node.random = self.dfs(head.random, booker)
        return node
