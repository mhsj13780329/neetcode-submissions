class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_tallest_height = [0] * len(height)
        suffix_tallest_heigh = [0] * len(height)
        sum = 0
        max_height = 0
        for i in range(len(height)):
            prefix_tallest_height[i] = max_height
            if height[i] > max_height:
                max_height = height[i]

        max_height = 0
        for i in range(len(height) - 1, -1, -1):
            suffix_tallest_heigh[i] = max_height
            if height[i] > max_height:
                max_height = height[i]

        for i in range(len(height)):
            sum += max(
                (min(prefix_tallest_height[i], suffix_tallest_heigh[i]) - height[i]), 0
            )

        return sum
