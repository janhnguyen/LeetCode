def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) < 2 :
        return len(s)

    maxVal = 0
    chars = set()
    x = 0

    for y in range(len(s)) :

        while s[y] in chars :
            chars.remove(s[x])
            x += 1

        chars.add(s[y])
        maxVal = max(maxVal, len(chars))

    return maxVal

print(lengthOfLongestSubstring("abcdefgh"))