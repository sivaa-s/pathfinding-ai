# Graph-Traversal
Code to traverse a maze in the form of a graph

The program reads its input from a file with the following format. The input begins with
two positive characters on a line indicating the number of rows r and columns c of the maze, re-
spectively. The next r lines contain the color and directional information for each arrow in the
maze. Each line has c values, where each value represents the color of the arrow by the direc-
tion of the arrow (N, E, S, W, NE, SE, SW, or NW). The color codes R and B represent red and
blue, respectively, while the direction codes represent north, east, south, west, northeast, south-
east, southwest, or northwest, respectively. The destination is represented by the letter O.

The output will consist of a path from the top left square to the bottom right square (bulls-eye).
There are multiple mazes to test, along a script that can determine if the
solution is correct. The script to test the solutions is verifyGraph.py.
