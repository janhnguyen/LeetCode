class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        revX = 0
        isNeg = -1 if x < 0 else 1
        x = abs(x)

        while not x == 0 :
            revX = (x % 10) + (revX * 10)
            x = x // 10

        if revX > 2**31-1 or x < -2**31 :
            return 0

        return revX * isNeg