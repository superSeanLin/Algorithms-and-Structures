class Solution:
    def fractionToDecimal(self, numerator: 'int', denominator: 'int') -> 'str':
        ## simulating long devison
        # acceleration
        if denominator == 1:
            return str(numerator)
        res = []
        if numerator * denominator < 0:
            res.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)
        book = {}  # remainder : index
        n, remainder = divmod(numerator, denominator)  # divmod(a,b) -> a//b, a%b
        res.append(str(n))
        if remainder == 0:  # no fraction
            return ''.join(res)
        res.append('.')
        while not remainder in book:
            book[remainder] = len(res)
            n, remainder = divmod(remainder*10, denominator)
            res.append(str(n))
            if remainder == 0:
                return ''.join(res)
        res.insert(book[remainder], '(')
        res += ')'
        return ''.join(res)
