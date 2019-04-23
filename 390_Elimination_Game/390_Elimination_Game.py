class Solution:
    # after the first elimination, only even number remain, then devided by 2 will give continuous 1~n//2
    # r_startLeft + r_startRight = n+1; e(n) = 2 * mirror result of e(n//2)
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        return 2 * ( 1+ n//2 - self.lastRemaining(n//2))
