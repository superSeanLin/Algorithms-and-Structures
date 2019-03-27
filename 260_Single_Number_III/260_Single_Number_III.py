class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ## two pass, first pass find XOR result of a and b, the find the set bit, second pass devide list into two group
        ## idea from disscussion and follow-up; https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C%2B%2BJava-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations
        diff = 0
        for e in nums:
            diff ^= e
        diff &= ~(diff - 1)  # ~(diff-1) == -diff
        res = [0, 0]
        for e in nums:
            res[not (e & diff)] ^= e  # e & diff == 0, set bit different; e & diff == 1, set bit same
        return res
        
