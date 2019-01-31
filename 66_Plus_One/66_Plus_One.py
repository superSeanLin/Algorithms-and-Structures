class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [0] + digits  # for edge case
        carry = 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            if carry and digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
                break
        if digits[0] == 0:
            return digits[1:]
        else:
            return digits
