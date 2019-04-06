class NumArray:
    ## use segmentation tree, do update and query in O(logn); use array to simulate segmentation tree
    def __init__(self, nums: List[int]):
        n = len(nums)
        if n == 0:
            return
        self.n = n
        self.tree = [0] * (2*n)
        for i in range(n, 2*n):
            self.tree[i] = nums[i-n]
        for i in range(n-1, -1, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
        
    def update(self, i: int, val: int) -> None:  # O(logn)
        i += self.n
        self.tree[i] = val
        while i > 0:
            if i % 2 == 0:  # left child
                self.tree[i//2] = self.tree[i] + self.tree[i+1]
            else:  # right child
                self.tree[i//2] = self.tree[i] + self.tree[i-1]
            i //= 2

    def sumRange(self, i: int, j: int) -> int:  # O(logn)
        # sum up num[i:j+1]
        i += self.n
        j += self.n
        res = 0
        while i <= j:  # until boundary meet; [i, L] + [R, j]
            if i % 2 == 1:  # if right child of left boundary, no need parent
                res += self.tree[i]
                i += 1
            if j % 2 == 0:  # if left child of right boundary, no need parent
                res += self.tree[j]
                j -= 1
            i //= 2  # get corresponding parent
            j //= 2
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
