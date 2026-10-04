class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        size = len(grid)
        col_size = len(grid[0])
        if not grid:
            return []
        for row in range(size):
            for col in range(col_size):
                if grid[row][col] == "1":
                    count+=1
                    self.numIslandsHelper(row, col, size, col_size, grid)
        return count
        

    def numIslandsHelper(self, row, col, size, col_size, grid):
        if row<0 or row >= size or col < 0 or col >= col_size:
            return
        if grid[row][col] == "0":
            return
        grid[row][col] = "0"
        self.numIslandsHelper(row+1, col, size, col_size, grid)
        self.numIslandsHelper(row-1,col, size, col_size, grid)
        self.numIslandsHelper(row,col+1, size, col_size, grid)
        self.numIslandsHelper(row,col-1, size, col_size, grid)
                
