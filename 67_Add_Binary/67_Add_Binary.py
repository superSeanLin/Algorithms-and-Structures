class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ## use bin(int(a, 2) + int(b, 2))[2:]; bin() converts 10 to 2,str, '0b..'; int(_,2) converts str to 2
        res = ""
        n = len(a)
        m = len(b)
        i, j = n-1, m-1
        carry = 0
        while i >= 0 and j >= 0:
            Sum = int(a[i]) + int(b[j]) + carry
            if Sum > 1:
                Sum -= 2
                carry = 1
            else:
                carry = 0
            res = str(Sum) + res
            i -= 1
            j -= 1
        while i >= 0:
            Sum = int(a[i]) + carry
            if Sum > 1:
                Sum -= 2
                carry = 1
            else:
                carry = 0
            res = str(Sum) + res
            i -= 1
        while j >= 0:
            Sum = int(b[j]) + carry
            if Sum > 1:
                Sum -= 2
                carry = 1
            else:
                carry = 0
            res = str(Sum) + res
            j -= 1
        if carry:
            res = "1" + res
        return res
                
