# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    ## Actually pretty trival solution, discard when not uniform
    ## The reason that we cannot multiply rand7() * rand7() is that 1*2 == 2*1 = 2; For example, 13 is not existed when use multiply
    ## Expected value of success when prob = p is 1/p; Can derived from 等比数列
    def rand10(self):
        """
        :rtype: int
        """
        while True:  # avoid 21 in the last stage
            temp = (rand7()-1) * 7 + rand7()
            if temp <= 40:
                return (temp-1) // 4 + 1
            else:  # 41~49
                temp = (temp - 40 - 1) * 7 + rand7()
                if temp <= 60:
                    return (temp-1) // 6 + 1
                else:  # 61~63
                    temp = (temp - 60 - 1) * 7 + rand7()
                    if temp <= 20:
                        return (temp-1) // 2 + 1
        
            
