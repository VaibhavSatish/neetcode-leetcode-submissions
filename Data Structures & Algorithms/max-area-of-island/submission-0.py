class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_count = 0
        if not grid:
            return []
        size = len(grid)
        col_size = len(grid[0])
        for row in range(size):
            count = 0
            for col in range(col_size):
                if grid[row][col] == 1:
                    count = self.IslandsHelper(row, col, size, col_size, grid)
                    print(count)
                if count > max_count:
                    max_count = count
        return max_count
        

    def IslandsHelper(self, row, col, size, col_size, grid) -> int:
        if row<0 or row >= size or col < 0 or col >= col_size:
            return 0
        if grid[row][col] == 0:
            return 0
        grid[row][col] = 0
        return (1+self.IslandsHelper(row+1, col, size, col_size, grid)+
        self.IslandsHelper(row-1,col, size, col_size, grid)+
        self.IslandsHelper(row,col+1, size, col_size, grid)+
        self.IslandsHelper(row,col-1, size, col_size, grid))
        
        