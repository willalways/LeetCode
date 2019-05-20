class Solution:
    def intToRoman(self, num: int) -> str:
        i1 = num % 10
        num = num // 10
        i2 = num % 10
        num = num // 10
        i3 = num % 10
        num = num // 10
        i4 = num
        list1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        list2 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        list3 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        return 'M'*i4 + list3[i3] + list2[i2] + list1[i1]
