class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2 :
            if height[0] < height[1] :
                return height[0]
            return height[1]

        left = 0
        right = len(height) - 1
        max = -1
        
        while not left == right :
            
            current = 0
            diff = right - left

            if height[left] < height[right] :
                current = height[left] * diff
            else :
                current = height[right] * diff
            
            if current > max :
                max = current

            if height[left] < height[right] :
                left += 1
            else :
                right -= 1

        return max
