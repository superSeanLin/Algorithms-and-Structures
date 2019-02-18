class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        i, j = 0, 0
        m, n = len(v1), len(v2)
        if m < n:
            count = 0
            while count < n-m:
                v1.append('0')
                count += 1
        elif n < m:
            count = 0
            while count < m-n:
                v2.append('0')
                count += 1
        length = max(m, n)
        while i < length:
            num1 = int(v1[i])
            num2 = int(v2[i])
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            i += 1
        return 0    
