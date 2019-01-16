class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # use Recursive methond
        if num <= 0:
            return ""
        if num >= 1000:
            m = num // 1000
            return m * "M" + self.intToRoman(num - m * 1000)
        elif num >= 900:
            return "CM" + self.intToRoman(num - 900)
        elif num >= 500:
            return "D" + self.intToRoman(num - 500)
        elif num >= 400:
            return "CD" + self.intToRoman(num - 400)
        elif num >= 100:
            c = num // 100
            return c * "C" + self.intToRoman(num - c * 100)
        elif num >= 90:
            return "XC" + self.intToRoman(num - 90)
        elif num >= 50:
            return "L" + self.intToRoman(num - 50)
        elif num >= 40:
            return "XL" + self.intToRoman(num - 40)
        elif num >= 10:
            x = num // 10
            return x * "X" + self.intToRoman(num - x * 10)
        elif num >= 9:
            return "IX" + self.intToRoman(num - 9)
        elif num >= 5:
            return "V" + self.intToRoman(num - 5)
        elif num >= 4:
            return "IV" + self.intToRoman(num - 4)
        else:  # >= 1
            i = num
            return i * "I" + self.intToRoman(num - i * 1)
