class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs(r, c):
            # 1. BASE CASES: 
            # If r is out of bounds, OR c is out of bounds, OR the current cell is '0':
            # return
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or grid[r][c] == '0':
                return
            
            # 2. SINK THE ISLAND:
            # Change grid[r][c] to '0'

            grid[r][c] = '0'
            
            # 3. SEND OUT THE CLONES:
            # Call dfs() for Up, Down, Left, Right

            dfs(r-1, c) # up
            dfs(r+1, c) # down
            dfs(r, c-1) # left
            dfs(r, c+1) # right

        # THE HELICOPTER LOOPS:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c) # Drop the bomb to sink the whole island
                    
        return island_count