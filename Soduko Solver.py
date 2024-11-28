def print_grid(grid):
    """Prints the Sudoku grid in a readable format."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_safe(grid, row, col, num):
    """Checks if placing a number in a specific cell is valid."""
    # Check the row
    if num in grid[row]:
        return False
    
    # Check the column
    if num in (grid[i][col] for i in range(9)):
        return False
    
    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

def solve_sudoku(grid):
    """Solves the Sudoku puzzle using backtracking."""
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Numbers 1 to 9
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num  # Tentatively place the number
                        if solve_sudoku(grid):  # Recur to solve the rest
                            return True
                        grid[row][col] = 0  # Undo the move if no solution
                return False  # Trigger backtracking if no number fits
    return True  # Puzzle is solved

# Example unsolved Sudoku puzzle (0 represents empty cells)
unsolved_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku:")
print_grid(unsolved_grid)

if solve_sudoku(unsolved_grid):
    print("\nSolved Sudoku:")
    print_grid(unsolved_grid)
else:
    print("\nNo solution exists!")
