class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_tallest_height = [0] * len(height)
        suffix_tallest_heigh = [0] * len(height)
        sum = 0
        max_height_left = 0
        max_height_right = 0
        for i in range(len(height)):
            prefix_tallest_height[i] = max_height_left
            if height[i] > max_height_left:
                max_height_left = height[i]

            j = len(height) - 1 - i
            suffix_tallest_heigh[j] = max_height_right
            if max_height_right < height[j]:
                max_height_right = height[j]

        for i in range(len(height)):
            sum += max(
                (min(prefix_tallest_height[i], suffix_tallest_heigh[i]) - height[i]), 0
            )

        return sum
