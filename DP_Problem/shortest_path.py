'''
 the key to solve the dp problem is to transform the cyclic graph into an acyclic graph so that we can use bottom up 
 memoize solution 
'''

'''
Description:
Given a grid, each cell is either 0 or 1 meaning walkable or blocked respectively. Find the number of paths that goes from 
top left cell to down right cell([0,0] to [N, N])
'''

def find_all_paths(grid):
    row = len(grid)-1
    col = len(grid[0])-1
    if row < 3 or col < 3:
        return None

    memoized_map = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    # memoized_map = 
    memoized_map[row][col] = 1
    
    # boundary1: last row's value
    for c in range(col-1,-1,-1):
        if grid[row][c] == 1:
            memoized_map[row][c]=0
        else:
            memoized_map[row][c]=memoized_map[row][c+1]
    # boundary2: last col's value
    for r in range(row-1, -1, -1):
        if grid[r][col] == 1:
            memoized_map[r][col]=0
        else:
            memoized_map[r][col]=memoized_map[r+1][col]
    
    row = row-1
    col = col-1
    while row>=0:
        while col>=0:
            if grid[row][col] == 1:
                memoized_map[row][col]=0
            else:
                memoized_map[row][col]=memoized_map[row+1][col]+memoized_map[row][col+1]
            col -= 1
        row-=1
        col=len(grid[0])-2
    for i in memoized_map:
        print(i)
    return memoized_map[0][0]

if __name__=='__main__':
    test_case = [
        [0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0],
        [0,0,0,0,1,0,0,0],
        [1,0,1,0,0,1,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,0,1,1,0,1,0],
        [0,1,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0]]

    print(find_all_paths(test_case))