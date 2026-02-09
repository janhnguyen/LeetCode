class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 :
            return s

        row = 0
        goingDown = False

        rows = ['' for _ in range(numRows)]

        for char in s :

            rows[row] += char

            if row == numRows - 1 or row == 0 :
                goingDown = not goingDown

            if goingDown :
                row += 1
            else :
                row -= 1

        return ''.join(rows)