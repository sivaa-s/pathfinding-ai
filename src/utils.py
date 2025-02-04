import json

def load_maze_from_file(filename):
    """Load a maze from a text file."""
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    return maze

def save_maze_to_file(maze, filename):
    """Save a maze to a text file."""
    with open(filename, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

def save_path_to_json(path, filename):
    """Save the computed path to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(path, file, indent=4)

def load_path_from_json(filename):
    """Load a path from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    sample_maze = [
        ['S', '.', '.', '#', 'G'],
        ['#', '#', '.', '#', '.'],
        ['.', '.', '.', '.', '.']
    ]
    
    save_maze_to_file(sample_maze, "maze.txt")
    loaded_maze = load_maze_from_file("maze.txt")
    print("Loaded Maze:")
    for row in loaded_maze:
        print(' '.join(row))
    
    sample_path = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (0, 4)]
    save_path_to_json(sample_path, "path.json")
    loaded_path = load_path_from_json("path.json")
    print("Loaded Path:", loaded_path)
