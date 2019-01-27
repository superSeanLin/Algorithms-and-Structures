class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## O(n) time since visit each element once
        n = len(nums)
        visited = set()  # no overlapping circles exisited, since each element leads to a single next index
        maximum = 0
        for i in range(n):
            j = i
            count = 0
            if not nums[i] in visited:
                while j < n:
                    if not nums[j] in visited:
                        visited.add(nums[j])
                        count += 1
                        j = nums[j]
                    else:  # seen before, first
                        break
                if count > maximum:
                    maximum = count
        return maximum
