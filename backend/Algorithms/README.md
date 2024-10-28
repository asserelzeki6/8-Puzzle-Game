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

# BFS (Breadth-First Search) Algorithm Documentation

This module implements the **Breadth-First Search (BFS)** algorithm for solving the 8-puzzle problem. The algorithm explores states level by level, starting from the initial state and exploring all possible moves at each level before proceeding to the next. BFS is guaranteed to find the shortest path to the goal, but it may be inefficient in terms of memory usage for larger problems.

---

## Class: `BFS`

### Parameters:

- `start_state` (str): The starting state of the 8-puzzle, represented as a string (e.g., `'123456780'`, where `'0'` is the blank space).
- `goal_state` (str): The target goal state to reach (default is `'012345678'`).
- `heuristic` (str): Not used in BFS, but included for compatibility with other algorithms.

### Attributes:

- `explored_nodes` (int): Tracks the number of nodes (states) explored during the search.
- `search_depth` (int): The maximum depth reached during the search.
- `total_time` (float): Total time taken by the algorithm in seconds.

### Methods:

### `run() -> tuple`

Executes the BFS search algorithm and returns the path to the goal and the total cost.

- **Returns**:
    - A tuple containing:
        - `path` (list): The sequence of states leading to the goal (or `None` if no path is found).
        - `cost` (float): BFS always returns the cost of 0 since it focuses on finding the shortest path without a heuristic cost.

### `get_neighbors(state: str) -> list`

Generates the neighboring states by moving the blank space ('0') up, down, left, or right.

- **Returns**:
    - A list of neighboring states for the current state of the puzzle.

### `swap(state: str, i: int, j: int) -> str`

Swaps two characters in the puzzle state to simulate tile movement.

- **Returns**:
    - A new string with the characters at indices `i` and `j` swapped.

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

This is an example demonstrating how to use the BFS algorithm. The puzzle starts with a state `'123456780'` and aims to reach the goal state `'012345678'`.

```python
# Initialize the BFS algorithm with start and goal states
bfs = BFS('123456780', '012345678', 'Euclidean')  # Note: The heuristic parameter is ignored in BFS.

# Run the algorithm
path = bfs.run()

# Print the resulting path and cost
print(path)  # Expected output: ['123456708', '123456078', ..., '012345678']
print(bfs.get_info())  # Expected output: {'explored_nodes': 17588, 'total_time': 0.07373905181884766, 'search_depth': 25673}

```

### Output:

```python
['123456708', '123456078', '123450678', '123405678', '123045678', '023145678', '203145678', '230145678', '231045678', '031245678', '301245678', '310245678', '312045678', '012345678']
{'explored_nodes': 17588, 'total_time': 0.07373905181884766, 'search_depth': 25673}
```

---

# DFS Search Algorithm Documentation

### Class: `DFS`

#### Parameters:

- **`start_state`** (`str`): The initial state of the 8-puzzle, represented as a string (e.g., `'123456780'` where `'0'` is the blank space).
- **`goal_state`** (`str`): The goal state of the puzzle (default is `'012345678'`).
- **`heuristic`** (`str`): Not used in DFS but included for consistency with other algorithms.

#### Attributes:

- **`explored_nodes`** (`int`): Tracks the number of explored nodes.
- **`search_depth`** (`int`): Tracks the maximum depth reached during the search.
- **`total_time`** (`float`): Total time taken for the search in seconds.

#### Methods:

1. **`run()`**:
   Executes the DFS algorithm and returns the path to the goal if found, or `None` if there is no solution.

2. **`get_neighbors(state: str)`**:
   Generates neighboring states by moving the blank tile up, down, left, or right.

3. **`swap(state: str, i: int, j: int)`**:
   Swaps two characters in the puzzle state to simulate tile movement.

4. **`get_path(came_from: dict, current: str)`**:
   Reconstructs the path from the start state to the goal state using a dictionary of predecessors.

5. **`get_info()`**:
   Returns a dictionary with statistics about the search, including the number of explored nodes, total execution time, and the maximum search depth.

---

### Example Usage

```python
# Initialize the DFS algorithm with start and goal states
dfs = DFS('041586732', '012345678')

# Run the algorithm
path = dfs.run()

# Print the resulting path and search statistics
print(path)  # Example output: ['123456780', ..., '012345678']
print(dfs.get_info())  # Example output: {'explored_nodes': X, 'total_time': Y, 'search_depth': Z}
```

### Expected Output

```python
{'explored nodes': 107390, 'total time': 0.248, 'max search depth': 70180}
```

---

# Iterative DFS Search Algorithm Documentation

### Class: `IT_DFS`

#### Parameters:

- **`start_state`** (`str`): The initial state of the 8-puzzle, represented as a string (e.g., `'123456780'` where `'0'` is the blank space).
- **`goal_state`** (`str`): The goal state of the puzzle (default is `'012345678'`).
- **`heuristic`** (`str`): Not used in IDDFS but included for consistency with other algorithms.

#### Attributes:

- **`explored_nodes`** (`int`): Tracks the number of explored nodes.
- **`search_depth`** (`int`): Tracks the maximum depth reached during the search.
- **`total_time`** (`float`): Total time taken for the search in seconds.

#### Methods:

1. **`run()`**:
   Executes the IDDFS algorithm and returns the path to the goal if found, or `None` if there is no solution.

2. **`get_neighbors(state: str)`**:
   Generates neighboring states by moving the blank tile up, down, left, or right.

3. **`swap(state: str, i: int, j: int)`**:
   Swaps two characters in the puzzle state to simulate tile movement.

4. **`get_path(came_from: dict, current: str)`**:
   Reconstructs the path from the start state to the goal state using a dictionary of predecessors.

5. **`get_info()`**:
   Returns a dictionary with statistics about the search, including the number of explored nodes, total execution time, and the maximum search depth.

---

### Example Usage

```python
# Initialize the IDDFS algorithm with start and goal states
it_dfs = IT_DFS('041586732', '012345678')

# Run the algorithm
path = it_dfs.run()

# Print the resulting path and search statistics
print(path)  # Example output: ['123456780', ..., '012345678']
print(it_dfs.get_info())  # Example output: {'explored_nodes': X, 'total_time': Y, 'search_depth': Z}
```

### Expected Output

```python
['541086732', '541786032', '541786302', '541786320', '541780326', '541708326', '541728306', '541728360', '541720368', '541702368', '541762308', '541762038', '541062738', '541602738', '541632708', '541632078', '541032678', '541302678', '501342678', '051342678', '351042678', '351402678', '301452678', '310452678', '312450678', '312405678', '312045678', '012345678']
{'explored nodes': 167450, 'total time': 0.168, 'max search depth': 28}
```

---