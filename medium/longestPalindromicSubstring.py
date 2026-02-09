def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    start = 0
    maxVal = 1

    def expand(left, right) :
        while left >= 0 and right < len(s) and s[left] == s[right] :
            left -= 1
            right += 1
        return right - left - 1

    for x in range(len(s)) :
        len1 = expand(x, x)
        len2 = expand(x, x + 1)
        current = max(len1, len2)

        if current > maxVal :
            maxVal = current
            start = x - (current - 1) // 2

    return s[start:start + maxVal]