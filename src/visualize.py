import matplotlib.pyplot as plt
import numpy as np

def visualize_maze(maze, path):
    """Visualize the maze and the computed path using matplotlib."""
    rows, cols = len(maze), len(maze[0])
    maze_array = np.zeros((rows, cols))
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == '#':
                maze_array[i][j] = 1  # Walls marked as 1
            elif maze[i][j] == 'S':
                start_pos = (i, j)
            elif maze[i][j] == 'G':
                goal_pos = (i, j)
    
    fig, ax = plt.subplots()
    ax.imshow(maze_array, cmap='Greys', origin='upper')
    
    # Mark start and goal positions
    ax.scatter(start_pos[1], start_pos[0], c='blue', s=100, label='Start')
    ax.scatter(goal_pos[1], goal_pos[0], c='green', s=100, label='Goal')
    
    # Mark the path
    for (x, y) in path:
        ax.scatter(y, x, c='red', s=50)
    
    ax.legend()
    plt.show()

if __name__ == "__main__":
    sample_maze = [
        ['S', '.', '.', '#', 'G'],
        ['#', '#', '.', '#', '.'],
        ['.', '.', '.', '.', '.']
    ]
    
    from pathfinder import Pathfinder
    
    pf = Pathfinder(sample_maze)
    path = pf.astar()
    print("Path:", path)
    
    visualize_maze(sample_maze, path)
