class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for index, height in enumerate(heights):
            prev_index = index
            while stack and height < stack[-1][0]:
                popped_height, popped_index = stack.pop()
                width = index - popped_index
                area_calc = width * popped_height
                max_area = max(max_area, area_calc)
                prev_index = popped_index
            stack.append((height, prev_index))

        while stack:
                popped_height, popped_index = stack.pop()
                width = len(heights) - popped_index
                area_calc = width * popped_height
                max_area = max(max_area, area_calc)

        
        return max_area

            

                

