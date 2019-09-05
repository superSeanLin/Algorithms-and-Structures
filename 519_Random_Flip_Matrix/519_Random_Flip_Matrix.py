import random
class Solution:
    # inspired by @akaenki and Durstenfeld version Fisher–Yates shuffle
    # The baisc idea : flatten matrix to 1-d array; each time we filp a element, swap it with end of current array tail, and decrease the array size by 1; Therefore, we won't touch fliped elements and keep the flip uniformly
    # Note: elements in the valid range of index array are untouched indexes; and each element is not related to indexes of index array
    
    def __init__(self, n_rows: int, n_cols: int):
        self.rows, self.cols = n_rows, n_cols
        self.remain = self.rows*self.cols  # the number of remaining 0
        self.swap = {}  # {original index : new index}
        
    # example: [[0, 0], [0, 0]]
    # step 1: flatten it to 1-d index array [0, 1, 2, 3|]; remain = 4
    # step 2: remain = 3; get a random index, say index = 0; 0 did not swap with other index; update swap[0] = 3 (current tail);
    #         index array [3, 1, 2,| 0] (index before | means untouched, afterwards means flipped); return [0 // 2, 0 % 2]
    #         the original matrix will be [[1, 0], [0, 0]]
    # step 3: remain = 2; get a random index, say index = 0 as before; 0 swapped with 3, thus actual index = 3; update swap[0] = 2 (current tail), which means swap elemnets of index 0 with element of index 2
    #         index array [2, 1,| 3, 0] (index before | means untouched, afterwards means flipped); return [3 // 2, 3 % 2]
    #         the original matrix will be [[1, 0], [0, 1]]
    # step 4: remain = 1; get a random index, say index = 0 as before; 0 swapped with 2, thus actual index = 2; update swap[0] = 1 (current tail), which means swap elemnets of index 0 with element of index 1
    #         index array [1,| 2, 3, 0] (index before | means untouched, afterwards means flipped); return [2 // 2, 2 % 2]
    #         the original matrix will be [[1, 0], [1, 1]]
    # step 5: remain = 0; get a random index, say index = 0 as before; 0 swapped with 1, thus actual index = 1; update swap[0] = 0 (current tail), which means swap elemnets of index 0 with element of index 0
    #         index array [|1, 2, 3, 0] (index before | means untouched, afterwards means flipped); return [1 // 2, 1 % 2]
    #         the original matrix will be [[1, 1], [1, 1]]
            
    def flip(self) -> List[int]:
        self.remain -= 1  # after flipping, there must be a 0 to be changed to 1
        index = random.randint(0, self.remain)  # return a random index from [0, self.remain], valid range
        actualIndex = index  # actual index based on matrix
        if index in self.swap:  # if there is a swap operation happened at this index, find the exact index element on this index now
            actualIndex = self.swap[index]
        tail = self.remain
        if tail in self.swap:  # if there is a swap operation happened at this tail index, find the exact index element on this tail index now
            tail = self.swap[tail]
        self.swap[index] = tail  # swap this index with tail
        return [actualIndex // self.cols, actualIndex % self.cols]
        
    def reset(self) -> None:
        self.swap = {}
        self.remain = self.rows*self.cols


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
