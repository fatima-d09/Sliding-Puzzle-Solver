# Sliding-Puzzle-Solver
The program provides two algorithms to solve puzzles

Breadth-First Search (BFS): A brute-force search that guarantees the shortest path by exploring all nodes level by level.
*A Search (A*)**: An optimized search algorithm that uses a heuristic to prioritize nodes closer to the goal.

The program reads the puzzle input from a text file, processes the board state, and prints the moves required to solve the puzzle 
along with the final board configuration and the total number of moves.


Usage:
To run the program, use one of the following commands:

# To use BFS:
./puzzle --bfs < input_file.txt
./puzzle --bfs  < /Users/fatoumatadembele/Desktop/cs242/hw2/test_in.txt

# To use A*:
./puzzle --astar < input_file.txt
./puzzle --astar  < /Users/fatoumatadembele/Desktop/cs242/hw2/test_in.txt

Where input_file.txt contains the size of the board followed by the board's initial configuration. 
For example, a 3x3 puzzle would look like this:

3
1 2 5
3 4 8
6 7 0

# Usage:

<strong>Heuristic for A*:</strong>
The heuristic used for the A* algorithm is the Manhattan Distance. This is a common heuristic for sliding puzzles because it accurately represents how far each tile is from its goal position. It is computed as the sum of the horizontal and vertical distances of each tile from its target position.

<strong>Manhattan Distance Formula:</strong>
For each tile t (i,j), its Manhattan Distance from its goal position (goal_i, goal_j) is:
    distance(t) = |i - goal_i|+ |j - goal_j|

The total Manhattan Distance for the board is the sum of these distances for all tiles.

Why Manhattan Distance?
- Optimality: It is admissible (never overestimates the cost to reach the goal) and consistent, which ensures that A* will find 
              the optimal solution.
- Efficiency: It provides a good balance between accuracy and computational cost, making it suitable for the n-puzzle problem.
              Performance Comparison

Breadth-First Search (BFS):
- Exploration: BFS explores all possible configurations level by level, ensuring that it finds the shortest path in terms of moves.
               Memory and Time Complexity: BFS is memory-intensive, as it must store all nodes at each depth level. Its time complexity 
               is O(b^d), where b is the branching factor (average number of children per node) and d is the depth of the solution.
- Performance: BFS can be slow and memory-heavy for larger boards (e.g., 5x5, 6x6) due to the sheer number of states it explores.

A* Search:
- Exploration: A* uses the Manhattan Distance heuristic to guide the search, exploring paths that are likely to lead to the goal faster.
               This means fewer nodes are expanded compared to BFS.
- Memory and Time Complexity: A* has a time complexity of O(b^d) in the worst case, similar to BFS, but the heuristic helps reduce 
                              the number of nodes expanded. The space complexity is also high because A* stores all generated nodes in 
                              memory, but it is typically more efficient than BFS.
- Performance: A* is significantly faster and more efficient for larger boards because the heuristic reduces the number of 
               unnecessary node expansions.

Node Expansion:
A good way to measure the performance of both BFS and A* is to count the number of expanded nodes during the search process. 
This gives an indication of how many states were explored before the goal was reached.

BFS: Will tend to expand more nodes, especially in larger puzzles, because it explores all possibilities evenly.

A*: Typically expands fewer nodes because the heuristic directs the search toward promising paths, reducing unnecessary exploration.

When to Use BFS vs. A*:
- BFS: Use when the puzzle size is small (e.g., 3x3 or 4x4) and finding the absolute shortest path is critical. BFS is guaranteed 
       to find the shortest solution, but it is not efficient for larger puzzles.
- A*: Use when the puzzle size increases (e.g., 5x5, 6x6, or higher). A* is more efficient because it uses the heuristic to 
      minimize the number of nodes expanded, leading to faster solutions with less memory usage.

# Measuring Performance

To measure the performance of each algorithm in terms of node expansions, you can modify the code to track the number of nodes 
that were expanded during the search. This can be done by incrementing a counter each time a node is dequeued from the frontier 
(for BFS) or popped from the priority queue (for A*). Here is how you can modify the code:
    1. Initialize a counter at the beginning of the search.
    2. Increment the counter each time a node is dequeued (BFS) or popped from the priority queue (A*).
    3. Print the counter at the end of the search to see how many nodes were expanded.
    4. This will allow you to compare the number of nodes expanded by BFS and A*, giving a clearer picture of their 
    relative performance.
