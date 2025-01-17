#!/usr/bin/env python3
import sys
import heapq
from collections import deque

# Define directions with corresponding row and column changes
DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}

# Helper function to print the board
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()  # Print a newline for better readability

# Helper function to print the solution path
def print_solution(path):
    print("Moves:")
    for move in path:
        print(move)
    print(f"Total Moves: {len(path)}")

# Function to read the puzzle from input
def read_puzzle():
    size = int(input().strip())  # Read puzzle size
    board = []
    for _ in range(size):
        board.append(list(map(int, input().strip().split())))
    return size, board

# Function to find the blank tile (0) in the board
def find_blank(board):
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == 0:
                return i, j
    return -1, -1

# Utility to generate the next board state after moving the blank tile
def get_next_board(board, blank_pos, direction):
    size = len(board)
    blank_row, blank_col = blank_pos
    delta_row, delta_col = DIRECTIONS[direction]
    new_row, new_col = blank_row + delta_row, blank_col + delta_col
    
    if 0 <= new_row < size and 0 <= new_col < size:
        # Create a copy of the board to avoid mutating the original
        new_board = [row[:] for row in board]
        # Swap the blank with the target tile
        new_board[blank_row][blank_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_row][blank_col]
        return new_board, (new_row, new_col)
    
    return None, None

# Check if the current board is the goal state
def is_goal(board):
    size = len(board)
    goal = [[(i * size + j) % (size * size) for j in range(size)] for i in range(size)]
    return board == goal

# BFS Algorithm for solving the puzzle
def bfs(initial_board):
    print("Initial Board:")
    print_board(initial_board)  # Display the initial board
    
    initial_blank = find_blank(initial_board)
    
    frontier = deque([(initial_board, initial_blank, [])])  # (board, blank_pos, path)
    visited = set()
    visited.add(tuple(map(tuple, initial_board)))  # Store as tuple to be hashable
    
    while frontier:
        board, blank_pos, path = frontier.popleft()
        
        if is_goal(board):
            print_solution(path)
            print("Final Board:")
            print_board(board)
            return path
        
        for direction in DIRECTIONS:
            next_board, next_blank = get_next_board(board, blank_pos, direction)
            if next_board and tuple(map(tuple, next_board)) not in visited:
                visited.add(tuple(map(tuple, next_board)))
                frontier.append((next_board, next_blank, path + [direction]))

# Heuristic function for A* (Manhattan Distance)
def manhattan_heuristic(board):
    size = len(board)
    distance = 0
    
    for i in range(size):
        for j in range(size):
            tile = board[i][j]
            if tile != 0:
                target_row, target_col = (tile // size), (tile % size)
                distance += abs(i - target_row) + abs(j - target_col)
    
    return distance

# A* Search Algorithm for solving the puzzle
def astar(initial_board):
    print("Initial Board:")
    print_board(initial_board)  # Display the initial board
    
    size = len(initial_board)
    initial_blank = find_blank(initial_board)
    
    frontier = []
    initial_heuristic = manhattan_heuristic(initial_board)
    heapq.heappush(frontier, (initial_heuristic, 0, initial_board, initial_blank, []))  # (priority, steps, board, blank_pos, path)
    
    visited = set()
    visited.add(tuple(map(tuple, initial_board)))  # Store as tuple to be hashable
    
    while frontier:
        _, steps, board, blank_pos, path = heapq.heappop(frontier)
        
        if is_goal(board):
            print_solution(path)
            print("Final Board:")
            print_board(board)
            return path
        
        for direction in DIRECTIONS:
            next_board, next_blank = get_next_board(board, blank_pos, direction)
            if next_board and tuple(map(tuple, next_board)) not in visited:
                visited.add(tuple(map(tuple, next_board)))
                new_steps = steps + 1
                new_heuristic = new_steps + manhattan_heuristic(next_board)
                heapq.heappush(frontier, (new_heuristic, new_steps, next_board, next_blank, path + [direction]))

# Main entry point for the program
def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("--bfs", "--astar"):
        print("Usage: ./puzzle --bfs|--astar", file=sys.stderr)
        return

    size, initial_board = read_puzzle()

    if sys.argv[1] == "--bfs":
        bfs(initial_board)
    elif sys.argv[1] == "--astar":
        astar(initial_board)

if __name__ == "__main__":
    main()
