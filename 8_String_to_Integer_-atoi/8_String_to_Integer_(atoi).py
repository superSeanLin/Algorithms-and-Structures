class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        length = len(str)
        negative = 1
        while i < length and str[i] == ' ':  # until not whilespace
            i += 1
        if i >= length:
            return 0
        if str[i] == '-':
            negative = -1
            i += 1
        elif str[i] == '+':
            negative = 1
            i += 1
        elif str[i] < '0' or str[i] > '9':
            return 0
        j = i
        while j < length and ('0' <= str[j] <= '9'):
            j += 1
        if i == j:
            return 0
        else:
            res = int(str[i:j]) * negative
            if res > (2**31 - 1):
                return 2**31 - 1
            elif res < -2**31:
                return -2**31
            else:
                return res
