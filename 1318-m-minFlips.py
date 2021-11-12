class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        """
        XOR same = 0  different = 1
        """
        """

        bin((a | b)^c).count('1') :wrong position
         or    real   destination
        0   0   0       1   change onece
        0   1   1       0   change onece
        1   0   1       0   change onece
        1   1   1       0   change twice
        change onece has been counted in bin((a | b)^c).count('1')
        only consider 1 or 1 change to 0
        when a&b == 1(a == 1,b == 1) and c == 0:
            count++
        in code:
            bin(a&b&(b^c)).count('1') or bin(a&b&(a^c)).count('1')
            eg bin(a&b&(1^c)).count('1') is wrong
        """
        return bin((a|b)^c).count('1')+bin(a&b&(c^a)).count('1')