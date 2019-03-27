class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ## use DP-like method to achieve 3-size heap
        ## also can use heap
        t2, t3, t5 = 0, 0, 0  # pointers for *2, *3, *5
        q = [1] * n
        for i in range(1, n):
            q[i] = (min(q[t2]*2, q[t3]*3, q[t5]*5))
            # remove duplicates; compare 2*a, 3*a, 5*a for each a
            if q[i] == q[t2]*2:
                t2 += 1
            if q[i] == q[t3]*3:
                t3 += 1
            if q[i] == q[t5]*5:
                t5 += 1
        return q[-1]
