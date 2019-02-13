class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        # one/two    x/x       one two/one two
        # 0   0      1/0           10 / 00      first time
        # 0   1      1/0           00 / 01      third time
        # 1   0      1/0           01 / 10      second time
        one, two = 0, 0
        for i in nums:
            one = (i ^ one) & ~two
            print(one)
            two = (i ^ two) & ~one
            print(two)
        return one
