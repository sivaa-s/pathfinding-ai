# Pathfinding AI 🚀

An AI-powered pathfinding algorithm to navigate 2D mazes efficiently.

## Features
- Uses AI to find the shortest path in a 2D maze.
- Implements algorithms such as A* and Dijkstra.
- Visualizes the pathfinding process.

## Installation
```bash
# Clone the repository
git clone https://github.com/sivaa-s/pathfinding-ai.git
cd pathfinding-ai

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
python main.py --maze example_maze.txt
```

## Project Structure
```
pathfinding-ai/
│── src/               # Source code
│   ├── pathfinder.py  # Pathfinding logic
│   ├── visualize.py   # Visualization utilities
│   ├── utils.py       # Helper functions
│── tests/             # Unit tests
│── example_maze.txt   # Sample maze file
│── README.md          # Project documentation
│── requirements.txt   # Python dependencies
```

## Example Maze
```
S . . . #
# # . # .
. . . . G
```
Where:
- `S` is the start point
- `G` is the goal
- `#` represents walls
- `.` represents open paths

## Contributing
Feel free to fork and contribute! Pull requests are welcome.
