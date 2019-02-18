class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        low, high = 0, n-1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low+1, high+1]
            elif sum < target:
                low += 1
            else:
                high -= 1
