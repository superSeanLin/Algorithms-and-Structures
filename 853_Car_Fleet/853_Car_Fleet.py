class Car:
    def __init__(self, position, speed):
        self.pos = position
        self.sp = speed
        self.prev = None
        self.next = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = None
        self.next = None
        del self
        
class Solution:
    def __init__(self):
        self.head = Car(0, 0)
        self.tail = Car(0, 0)

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## Note time is continuous, thus cannot simplify to list
        ## naive solution, use double linked list to simulate
        # first need to sort the lists
        count = 0
        if not position or not speed:  # empty
            return count
        if len(position) == 1 or len(speed) == 1:  # single car
            return 1
        self.head.pos = target
        helper = sorted(zip(position, speed), key=lambda pair:pair[0])
        position = [x[0] for x in helper][::-1]
        speed = [x[1] for x in helper][::-1]
        road = self.constructList(position, speed)
        while self.head.next != self.tail:  # until empty -> all car arrive
            p = self.head.next  # pointer
            last_arrive = None
            newFleet = 0
            while p != self.tail:  # traversal
                p.pos = p.pos + p.sp
                local = p.pos
                temp = p.next
                print(local, last_arrive)
                if p.pos >= p.prev.pos:  # if pass the prev car
                    p.remove()
                if local >= target and temp.prev.pos >= target:  # prev car reach the end
                    if last_arrive == None:
                        last_arrive = local
                        newFleet += 1
                    elif local < last_arrive:
                        newFleet += 1
                        last_arrive = min(local, last_arrive)  # prev car ending pos
                p = temp
            count += newFleet
        return count
    
    def constructList(self, position, speed):
        temp = self.head
        for i in range(len(position)):
            node = Car(position[i], speed[i])
            node.prev = temp
            temp.next = node
            node.next = self.tail
            self.tail.prev = node
            temp = node
