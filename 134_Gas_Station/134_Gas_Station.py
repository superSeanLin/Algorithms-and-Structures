class Solution:
    def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> 'int':
        ## O(n) idea from Discussion:
        # 1. If car starts at A and can not reach B. Any station between A and B can not reach B
        # 2. If the total number of gas is not smaller than the total number of cost. There must be a solution.
        gasSum = sum(gas)
        costSum = sum(cost)
        if gasSum < costSum:
            return -1
        n = len(gas)
        tank = 0
        start = 0
        for i in range(n):
            tank = tank + gas[i] - cost[i]
            if tank < 0:  # can not reach
                tank = 0
                start = i+1
        return start
