class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        
        def dfs(i, j):
            if i == len(triangle):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                memo[(i, j)] = triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
                return memo[(i, j)]
            
        return triangle[0][0] + min(dfs(1,0), dfs(1,1))
    
        # sums = 0
        # for i in range(len(triangle)):
        #     sums += min(triangle[i])
        # return sums