class Solution:
    '''
    思路：摩尔投票升级版，超过n/3的数最多只能有两个；
    先选出两个候选人A,B,遍历数组，如果投A（等于A），则A的票数++;如果投B，B的票数++；
    如果A,B都不投（即与A，B都不相等）,那么检查此时是否AB中候选人的票数是否为0，如果为0,则成为新的候选人；
    如果A,B两个人的票数都不为0，那么A,B两个候选人的票数均--；
    遍历结束后选出两个候选人，但是这两个候选人是否满足>n/3，还需要再遍历一遍数组，找出两个候选人的具体票数
    '''
    def majorityElement(self, nums: List[int]) -> List[int]:
        ## Boyer-Moore Voting Algorithm, neutralize prefix votes; O(n) time, O(1) space
        # at most two majority number; actually do Boyer-Moore Voting twice at the same time, so need check if great than n//3
        res = []
        if not nums:
            return res
        a, b = nums[0], nums[0]  # top 2 candidates
        countA, countB = 0, 0  # counter for a and b
        for e in nums:
            if e == a:
                countA += 1
                continue
            if e == b:
                countB += 1
                continue
            if countA == 0:
                a = e
                countA += 1
                continue
            if countB == 0:
                b = e
                countB += 1
                continue
            countA -= 1
            countB -= 1
        countA, countB = 0, 0
        for e in nums:
            if e == a:
                countA += 1
                continue
            if e == b:
                countB += 1
                continue
        if countA > len(nums)//3:
            res.append(a)
        if countB > len(nums)//3:
            res.append(b)
        return res
