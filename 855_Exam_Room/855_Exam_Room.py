## memory allocation
## how to deal with base case???
class ListNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.distance = end - start
        self.next = None

    def allocation(self, mid):
        temp = self.next
        self.next = ListNode(mid, self.end)
        self.next.next = temp
        self.end = mid
        self.distance = self.end - self.start

    def dellocation(self):
        temp = self.next
        if temp:  # avoid last one
            self.end = temp.end
            self.distance = self.end - self.start
            self.next = temp.next
            del temp
            
class ExamRoom:
    def __init__(self, N: int):
        self.initial = 0
        self.counter = 0
        self.capacity = N
        self.head = ListNode(0, self.capacity-1)
        
    def seat(self) -> int:
        self.counter += 1
        if self.counter > self.capacity:
            return 0
        if self.initial < 2:  # initial the linked list
            res = [0, self.capacity-1][self.initial]
            self.initial += 1
            return res
        q, p = self.head, self.head  # q is the Node to be sliced
        dis = 0
        while p:
            if (not dis and p.distance > 1) or p.distance >= 2 + dis:
                dis = p.distance
                q = p
            p = p.next
        mid = (q.start + q.end)//2
        q.allocation(mid)
        return mid

    def leave(self, p: int) -> None:
        self.counter -= 1
        if self.counter == 0:
            self.initial = 0
        q = self.head
        while q:
            if q.end == p:
                q.dellocation()
                return
            q = q.next
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
