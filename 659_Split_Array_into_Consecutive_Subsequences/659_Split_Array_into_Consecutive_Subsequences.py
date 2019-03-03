class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        ## recursive too slow but should work; hard to do math...
        ## greedy idea from Discussion
        freq = {}  # number : count; number left to be placed
        straight = {}  # ending number : count; straight ending at number
        for e in nums:
            if not e in freq:
                freq[e] = 1
            else:
                freq[e] += 1
        for e in nums:
            if freq[e] > 0:  # not all placed
                freq[e] -= 1
                if e-1 in straight and straight[e-1] > 0:
                    straight[e-1] -= 1
                    if e in straight:
                        straight[e] += 1
                    else:
                        straight[e] = 1
                elif e+1 in freq and e+2 in freq and freq[e+1] > 0 and freq[e+2] > 0:
                    freq[e+1] -= 1
                    freq[e+2] -= 1
                    if e+2 in straight:
                        straight[e+2] += 1
                    else:
                        straight[e+2] = 1
                else:
                    return False
        return True
