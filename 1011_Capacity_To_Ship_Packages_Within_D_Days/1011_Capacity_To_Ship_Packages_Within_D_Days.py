class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
	    # binary search on [1, sum(weights)], do validation for each capacity and find the minimum one
        low, high = 1, sum(weights)
        while low <= high:  # high is the target
            mid = (low + high) // 2
            if self.ifValid(weights, D, mid):  # bigger
                high = mid -1
            else:  # smaller
                low = mid + 1
        return low  # high is max of nonvalid, low is min of valid

    def ifValid(self, weights, D, cap):
        counter = 0
        tempSum = 0
        for w in weights:
            if w > cap:  # already large than cap
                return False
            if tempSum + w > cap:  # need a slicing
                counter += 1
                tempSum = 0
            tempSum += w
        return (counter <= D-1)

