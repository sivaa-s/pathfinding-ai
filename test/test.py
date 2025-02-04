import unittest
from utils_pathfinding import load_maze_from_file, save_maze_to_file, save_path_to_json, load_path_from_json
import os

class TestPathfindingUtils(unittest.TestCase):
    
    def setUp(self):
        """Setup test files before running tests."""
        self.sample_maze = [
            ['S', '.', '.', '#', 'G'],
            ['#', '#', '.', '#', '.'],
            ['.', '.', '.', '.', '.']
        ]
        self.maze_filename = "test_maze.txt"
        self.path_filename = "test_path.json"
        self.sample_path = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (0, 4)]
    
    def test_save_and_load_maze(self):
        """Test saving and loading a maze from a file."""
        save_maze_to_file(self.sample_maze, self.maze_filename)
        loaded_maze = load_maze_from_file(self.maze_filename)
        self.assertEqual(self.sample_maze, loaded_maze)
    
    def test_save_and_load_path(self):
        """Test saving and loading a path from a JSON file."""
        save_path_to_json(self.sample_path, self.path_filename)
        loaded_path = load_path_from_json(self.path_filename)
        self.assertEqual(self.sample_path, loaded_path)
    
    def tearDown(self):
        """Cleanup test files after tests run."""
        if os.path.exists(self.maze_filename):
            os.remove(self.maze_filename)
        if os.path.exists(self.path_filename):
            os.remove(self.path_filename)

if __name__ == "__main__":
    unittest.main()
