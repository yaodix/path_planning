# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):
    # Get dimensions of the grid
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    # Create matrices for the value function (grid*4 possible orientations) and the 3D and 2D policies
    value = [[[999 for col in range(n_cols)] for row in range(n_rows)],
            [[999 for col in range(n_cols)] for row in range(n_rows)],
            [[999 for col in range(n_cols)] for row in range(n_rows)],
            [[999 for col in range(n_cols)] for row in range(n_rows)]]
            
    policy3D = [[[' ' for col in range(n_cols)] for row in range(n_rows)],
                [[' ' for col in range(n_cols)] for row in range(n_rows)],
                [[' ' for col in range(n_cols)] for row in range(n_rows)],
                [[' ' for col in range(n_cols)] for row in range(n_rows)]]
                
    policy2D = [[' ' for col in range(n_cols)] for row in range(n_rows)]
    
    

    # Helper variable
    change = True

    while change:
        change = False

        # Go trough the whole solution space
        for x in range(n_rows):
            for y in range(n_cols):
                for theta in range(4):
                    # If we are in the goal position
                    if goal[0]==x and goal[1]==y:
                        if value[theta][x][y] > 0:
                            value[theta][x][y] = 0
                            policy3D[theta][x][y] = '*'
                            change = True
                    # General case
                    elif grid[x][y] == 0:
                        for a in range(len(action)):
                            theta2 = (theta+action[a]) % 4
                            x2 = x + forward[theta2][0]
                            y2 = y + forward[theta2][1]
    
                            if x2>=0 and x2<n_rows and y2>=0 and y2<n_cols and grid[x2][y2]==0:
                                v2 = value[theta2][x2][y2] + cost[a]
    
                                if v2 < value[theta][x][y]:
                                    change = True
                                    value[theta][x][y] = v2
                                    policy3D[theta][x][y] = action_name[a]

    # Build the 2D policy
    x = init[0]
    y = init[1]
    theta = init[2]
    
    policy2D[x][y] = policy3D[theta][x][y]
    
    while policy3D[theta][x][y] != '*':
        if policy3D[theta][x][y] == '#':
            theta2 = theta
        elif policy3D[theta][x][y] == 'R':
            theta2 = (theta-1) % 4
        elif policy3D[theta][x][y] == 'L':
            theta2 = (theta+1) % 4
        
        x = x + forward[theta2][0]
        y = y + forward[theta2][1]
        theta = theta2
        
        policy2D[x][y] = policy3D[theta][x][y]

    # Print policy map
    for row in policy2D:
        print(row)

    return policy2D

# Call function
optimum_policy2D(grid, init, goal, cost)

