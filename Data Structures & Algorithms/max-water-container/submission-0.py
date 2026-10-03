class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left_pointer = 0
        right_pointer = len(heights) - 1

        while left_pointer < right_pointer:
            area = (right_pointer - left_pointer) * min(
                heights[left_pointer], heights[right_pointer]
            )
            if area > result:
                result = area
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return result
