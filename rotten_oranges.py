
# Time complexity - O(M*N)
# Space Complexity - O(M)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        time = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        # if no fresh oranges edge case or no oranges
        if not fresh:
            return 0

        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    r,c = i+x, j+y
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r,c))
                        fresh -= 1
            time += 1
        return time - 1 if fresh == 0 else -1
