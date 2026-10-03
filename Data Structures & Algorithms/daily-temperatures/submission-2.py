class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        final = [0] * size
        stack = []
        for i, current_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current_temp:
                prev_index = stack.pop()
                final[prev_index] = i - prev_index
            stack.append(i)
        
        return final
            
                


        


        