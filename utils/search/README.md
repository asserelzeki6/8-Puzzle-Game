# Searching Algoritms
---

# A* Search Algorithm Documentation

This module implements the *A (A-star)** search algorithm for solving the 8-puzzle problem (sliding tile puzzle). The algorithm explores states by minimizing the total cost function \(f(n) = g(n) + h(n)\), where:

- \(g(n)\) is the cost to reach the current state from the start state.
- \(h(n)\) is the heuristic cost (estimated cost) to reach the goal state from the current state.

Currently, this module supports **Manhattan** and **Euclidean** distance heuristics. Additional search algorithms (such as Breadth-First Search, Depth-First Search, and Uniform-Cost Search) will be added soon.

---

## Class: `AStar`

### Parameters:

- `start_state` (str): The starting state of the 8-puzzle, represented as a string (e.g., `'123456780'` where `'0'` is the blank space).
- `goal_state` (str): The target goal state to reach (default is `'012345678'`).
- `heuristic` (str): The heuristic function to use. Options are `'Manhattan'` or `'Euclidean'`. Default is `'Manhattan'`.

### Attributes:

- `explored_nodes` (int): Tracks the number of nodes (states) explored during the search.
- `search_depth` (int): The maximum depth reached during the search.
- `total_time` (float): Total time taken by the algorithm in seconds.

### Methods:

### `run() -> tuple`

Executes the A* search algorithm and returns the path to the goal and the total cost.

- **Returns**:
    - A tuple containing:
        - `path` (list): The sequence of states leading to the goal (or `None` if no path is found).
        - `cost` (float): The total cost to reach the goal (or `float('inf')` if no path is found).

### `get_neighbors(state: str) -> list`

Generates the neighboring states by moving the blank space ('0') up, down, left, or right.

- **Returns**:
    - A list of tuples where each tuple contains:
        - `neighbor_state` (str): A neighboring state of the puzzle.
        - `cost` (int/float): The cost to reach this neighbor.

### `swap(state: str, i: int, j: int) -> str`

Swaps two characters in the puzzle state to simulate tile movement.

- **Returns**:
    - A new string with the characters at indices `i` and `j` swapped.

### `get_cost(state: str) -> float`

Calculates the heuristic cost (Manhattan or Euclidean distance) of a given state.

- **Returns**:
    - The heuristic cost to reach the goal from the given state.

### `manhattan_distance(state: str) -> int`

Calculates the Manhattan distance between the current state and the goal state.

- **Returns**:
    - The Manhattan distance as an integer.

### `euclidean_distance(state: str) -> float`

Calculates the Euclidean distance between the current state and the goal state.

- **Returns**:
    - The Euclidean distance as a floating-point number.

### `get_path(came_from: dict, current: str) -> list`

Reconstructs the path from the start state to the goal state.

- **Returns**:
    - A list of states representing the path to the goal.

### `get_info() -> dict`

Returns statistics about the search process, such as the number of explored nodes, total execution time, and the maximum search depth.

- **Returns**:
    - A dictionary with the following keys:
        - `'explored_nodes'`: Number of nodes explored during the search.
        - `'total_time'`: Total time taken for the search (in seconds).
        - `'search_depth'`: The maximum depth reached during the search.

---

### Example Usage

This is an example that demonstrates how to use the A* search algorithm. The puzzle starts with a state `'123456780'` and aims to reach the goal state `'012345678'` using the **Euclidean distance** heuristic.

```python
# Initialize the A* algorithm with start and goal states, and the Euclidean heuristic
astar = AStar('123456780', '012345678', 'Euclidean')

# Run the algorithm
path, cost = astar.run()

# Print the resulting path and cost
print(path)  # Outputs: ['123456708', '123456078', ..., '012345678']
print(cost)  # Outputs: 66.31809710423605

# Print additional information about the search process
print(astar.get_info())  # Outputs: {'explored_nodes': 414, 'total_time': 0.007120370864868164, 'search_depth': 793}

```

### Output:

```python
['123456708', '123456078', '123450678', '123405678', '123045678', '023145678', '203145678', '230145678', '231045678', '031245678', '301245678', '310245678', '312045678', '012345678']
66.31809710423605
{'explored_nodes': 414, 'total_time': 0.007120370864868164, 'search_depth': 793}

```

---

# DFS Search Algorithm Documentation

---

# BFS Search Algorithm Documentation

---

# Iterative DFS Search Algorithm Documentation

---