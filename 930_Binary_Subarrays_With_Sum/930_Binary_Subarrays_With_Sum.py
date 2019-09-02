class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
	# prefix sfirst calculate all array sum, then use hashmap
        if not A:
            return 0
        n = len(A)
        sum= [0] 
        temp = 0
        for idx, num in enumerate(A):
            temp += num
            sum.append(temp)
        counter = 0
        index = {}  # sum : num of combination of sum
        for s in sum:
            if s in index:  # only when we see s+S before
                counter += index[s]
            if s+S in index:
                index[s+S] += 1
            else:
                index[s+S] = 1
        return counter

        
