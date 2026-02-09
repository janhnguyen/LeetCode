def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxVal = 0
    for x in range(len(s)) :
        for y in range(x + 1, len(s)) :
            if s[x] == s[y] :
                if len(s[x:y]) > maxVal :
                    maxVal = len(s[x:y])
                break
    return maxVal