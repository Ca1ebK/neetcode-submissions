from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        '''
        Time: O(n*m)
        Space: O(n*m)?
        '''

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # 1. SETUP SCAN
        # TODO: Loop through grid. Add '2's to queue, count '1's.

        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # 2. THE BFS RIPPLE
        while queue and fresh_count > 0:
            
            # This loop processes exactly ONE minute of rot
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # The 4 directions: Up, Down, Left, Right
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    # 3. SPREAD THE ROT
                    # TODO: If row/col is in bounds AND grid[row][col] == 1:
                    #   - Change to 2
                    #   - Decrease fresh_count
                    #   - Append (row, col) to queue
                    if row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh_count -= 1
                        queue.append((row, col))
            # Minute is over!
            minutes += 1
            
        # 4. FINAL CHECK
        return minutes if fresh_count == 0 else -1