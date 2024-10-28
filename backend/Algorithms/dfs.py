import queue
import time

class DFS:
    def __init__(self, start_state, goal_state='012345678', heuristic='Manhattan'):
        """
        Initializes the DFS search algorithm.

        Args:
            start_state (str): The initial state of the puzzle.
            goal_state (str): The goal state of the puzzle (default is '012345678').
            heuristic (str): The heuristic function to use (not used in DFS, included for consistency).
        """
        self.start_state = start_state
        self.goal_state = goal_state
        self.heuristic = heuristic
        self.explored_nodes = 0  # Tracks how many nodes have been explored
        self.search_depth = 0  # Maximum depth reached during the search
        self.total_time = 0  # Total time taken to complete the search

    def run(self):
        """
        Executes the DFS algorithm.

        Returns:
            A list representing the path to the goal state, or None if no path is found.
        """
        start_time = time.time()  # Start timing the search
        frontier = []  # Stack for DFS exploration
        frontier.append(self.start_state)  # Add the initial state to the stack
        came_from = {}  # Maps each state to its predecessor to reconstruct the path
        visited = {self.start_state: 0}  # Tracks visited states

        while frontier:  # Continue while there are states in the stack
            current = frontier.pop()  # Pop the last state added (LIFO)
            self.explored_nodes += 1  # Increment the count of explored nodes

            if current == self.goal_state:  # Check if the goal state is reached
                self.total_time = time.time() - start_time  # Calculate total search time
                return self.get_path(came_from, current)  # Return the path to the goal

            # Explore neighbors of the current state
            for next_state in self.get_neighbors(current):
                if next_state not in visited:  # Only add unvisited states to the stack
                    visited[next_state] = 0  # Mark as visited
                    frontier.append(next_state)  # Add to the stack
                    came_from[next_state] = current  # Track predecessor for path reconstruction
                    self.search_depth = max(self.search_depth, len(came_from))  # Update search depth

        self.total_time = time.time() - start_time  # Calculate total time if no solution is found
        return None  # Return None if no solution exists

    def get_neighbors(self, state):
        """
        Generates valid neighboring states by moving the blank tile (0).

        Args:
            state (str): The current puzzle state.

        Returns:
            A list of neighboring states resulting from valid moves.
        """
        i = state.index('0')  # Find the blank tile's index
        neighbors = []

        # Move the blank tile up if within bounds
        if i - 3 >= 0:
            neighbors.append(self.swap(state, i, i - 3))

        # Move the blank tile right if within bounds
        if i % 3 < 2:  # Right movement within the same row
            neighbors.append(self.swap(state, i, i + 1))

        # Move the blank tile left if within bounds
        if i % 3 > 0:  # Left movement within the same row
            neighbors.append(self.swap(state, i, i - 1))

        # Move the blank tile down if within bounds
        if i + 3 < 9:
            neighbors.append(self.swap(state, i, i + 3))

        return neighbors

    def swap(self, state, i, j):
        """
        Swaps two characters in the puzzle state string.

        Args:
            state (str): The current state of the puzzle.
            i (int): Index of the first character.
            j (int): Index of the second character.

        Returns:
            str: A new state with the characters at indices i and j swapped.
        """
        state = list(state)  # Convert to list for mutability
        state[i], state[j] = state[j], state[i]  # Swap tiles
        return ''.join(state)  # Return as a string

    def get_path(self, came_from, current):
        """
        Reconstructs the path from the start state to the goal state.

        Args:
            came_from (dict): Maps each state to its predecessor.
            current (str): The current state (goal state).

        Returns:
            list: The path from the start to the goal state.
        """
        path = []
        while current in came_from:  # Trace from goal to start
            path.append(current)  # Add each state to the path
            current = came_from[current]  # Move to predecessor
        path.reverse()  # Reverse to get path from start to goal
        return path

    def get_info(self):
        """
        Retrieves search statistics.

        Returns:
            dict: Contains the number of explored nodes, total time, and maximum search depth.
        """
        return {
            'explored_nodes': self.explored_nodes,  # Total nodes explored
            'total_time': self.total_time,  # Search duration
            'search_depth': self.search_depth  # Max depth reached
        }
