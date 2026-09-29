class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            start = 0
            end = len(matrix)-1
            while (start<=end):
                midpoint = (start+end) // 2
                if matrix[midpoint][0] < target and matrix[midpoint][-1] < target:
                    start = midpoint+1
                elif matrix[midpoint][0] > target:
                    end = midpoint-1
                else:
                    start = 0
                    end = len(matrix[midpoint])-1
                    while (start<=end):
                        midpoint_2 = (start+end) // 2
                        if matrix[midpoint][midpoint_2] < target:
                            start = midpoint_2+1
                        elif matrix[midpoint][midpoint_2] > target:
                            end = midpoint_2-1
                        else:
                            return True
                    break
            return False
        
        
        