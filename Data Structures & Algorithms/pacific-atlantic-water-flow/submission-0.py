class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # find all cells where water can flow from the cell we're at to both the pacific and alantic oceans 
        # return the cells we have found as. a 2D list where each element is a list [r,c] representing the coordinates 
        # constraints: the water can flow in four directions (up,down,left or right) into a neighboring cell WITH height equal or lower so “next height <= current height of the cells 
# pacific = top row, left column :::: Alantic == bottom row, right column
        ROWS, COLS = len(heights),len(heights[0])
        pac, atl = set(), set()
        def dfs(r,c,visited, prev_height): 
                    # 1. stop conditions
            if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]):
                return
            if (r, c) in visited:
                return
            if heights[r][c] < prev_height:
                return

            # 2. mark this cell
            visited.add((r, c))

            # 3. explore the four neighbors
            dfs(r + 1, c, visited,heights[r][c])
            dfs(r - 1, c, visited,heights[r][c])
            dfs(r, c + 1, visited,heights[r][c])
            dfs(r, c - 1, visited,heights[r][c]) 
        for c in range(COLS): 
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS - 1, c,atl,heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl: 
                    res.append([r,c])
        return res
    
    
