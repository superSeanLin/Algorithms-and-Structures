class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## build graph and find entrance of the cycle
        # we consider nums list as [index node: next node], if there is duplicates, then must two different index nodes -> same nodes; we use fast and slow pointer to detect the cycle
        slow = nums[0]  # skip 0 since range (1, n)
        fast = nums[0]
        while True:  # unitil meet
            slow = nums[slow]
            fast = nums[nums[fast]]  # fast is twice quicker than slow
            if slow == fast:
                break
        # reset fast to start
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast
