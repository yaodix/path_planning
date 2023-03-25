# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    expand = None
    
    # List to store our result (cost, x, y)
    path = []
    
    # Get grid dimensions
    n_rows = len(grid[0])
    n_cols = len(grid)
    
    # Create grid saying which cells have been already visited
    visited = [[0 for row in range(n_rows)] for col in range(n_cols)]
    
    # Create expansion grid (initialized with -1) and a expansion counter
    expand = [[-1 for row in range(n_rows)] for col in range(n_cols)]
    n_expansions = 0
    
    # Set initial cell as visited and as 0 expansions in the expansion grid
    visited[init[0]][init[1]] = 1
    expand[init[0]][init[1]] = 0
    
    # Register initial node in the list of cells to expand
    x = init[0]
    y = init[1]
    g = 0 # Current cost
    
    paths_to_expand = [[g, x, y]]
    
    # Flags
    success = False # If the goal is reached
    fail = False # If the goal is unreachable
    
    while success==False and fail==False:
        # If we ran out of cells to expand
        if len(paths_to_expand) == 0:
            fail=True
            path = [-1, -1, -1]
        else:
            # Expand the next cell with the smallest cost
            paths_to_expand.sort() # Sort according 1st element (cost)
            paths_to_expand.reverse() # Reverse to have the smallest cost at the end
            next_cell = paths_to_expand.pop() # Pop last element
            # method 2
            # for n in range(len(paths_to_expand)): 
            #     next_cell = paths_to_expand[n]
            #     if (paths_to_expand[n][1] != goal[0] or paths_to_expand[n][2] != goal[1]):
            #         del paths_to_expand[n]
            #     break
            # Get information about next cell to expand
            g = next_cell[0]
            x = next_cell[1]
            y = next_cell[2]
            
            # BASE CASE. If we are in the goal, save the next cell
            if x==goal[0] and y==goal[1]:
                success = True
                path = next_cell
            else:
                # GENERAL CASE. Expand the cell
                # For each possible movement
                for movement in delta:
                    # Get new cell
                    new_x = x + movement[0]
                    new_y = y + movement[1]
                    
                    # Check if we will be inside the grid
                    if new_x>=0 and new_x<n_cols and new_y>=0 and new_y<n_rows:
                        # Check if the cell is visited and there is no obstacle in the map
                        if visited[new_x][new_y]==0 and grid[new_x][new_y]==0:
                            # Update cost and append to expansion list
                            new_g = g + cost
                            paths_to_expand.append([new_g, new_x, new_y])
                            
                            # Mark cell as visited
                            visited[new_x][new_y] = 1
                            
                            # Update expansion counter and expansion grid
                            n_expansions += 1
                            expand[new_x][new_y] = n_expansions
    
    return expand

path =  search(grid, init, goal, cost)
for n in range(len(path)):
    print(path[n])
