class Solution(object):
    
    ## create an negated helper list and use merge technique to find result
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Complexity O(n*log(n)), better than brute force
        # assume nums is sorted and independet
        t = target / 2.0
        nums_copy = nums.copy()  # deep copy
        # made centered by target
        nums_copy = [t - x for x in nums_copy]
        nums_copy.reverse()
        nums = [x - t for x in nums]
        nums_merged = self.merge(nums_copy, nums)
        # check if two consecutive same numbers
        r = None
        for i in range((len(nums_merged)) - 1):
            j = i + 1
            if nums_merged[i] == nums_merged[j]:
                r = nums_merged[i]
                break
        print(nums_merged)
        # bring t back
        if r != None:
            return [nums.index(r), len(nums_copy) - 1 - nums_copy.index(r)]
        else:  # no result
            return None
        
    def merge(self, l1, l2):
        result = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        if i < len(l1):
            result.extend(l1[i:])
        elif j < len(l2):
            result.extend(l2[j:])
        return result
