import queue
import time

class BFS:
    def __init__(self, start_state, goal_state='012345678'):
        """
        Initializes the BFS search algorithm.

        Args:
            start_state (str): The initial state of the puzzle.
            goal_state (str): The goal state of the puzzle (default is '012345678').
            heuristic (str): The heuristic function to use (not used in BFS but present for consistency).
        """
        self.start_state = start_state
        self.goal_state = goal_state
        self.explored_nodes = 0  # Count of how many nodes have been explored
        self.search_depth = 0  # Maximum depth reached during the search
        self.total_time = 0  # Time taken to complete the search

    def run(self):
        """
        Executes the BFS algorithm.

        Returns:
            A tuple of the path to the goal state and the total cost (which is not used in BFS).
        """
        start_time = time.time()  # Start timing the execution
        frontier = queue.Queue()  # FIFO queue for nodes to explore
        frontier.put([self.start_state,0])  # Add the start state to the frontier
        came_from = {}  # Tracks the path to each node
        visited = {self.start_state: 0}  # Tracks visited states

        while not frontier.empty():  # Loop while the frontier is not empty
            current,path_length = frontier.get()  # Dequeue the next state to explore
            self.explored_nodes += 1  # Increment the explored node count
            self.search_depth = max(self.search_depth, path_length)  # Update the maximum search depth


            if current == self.goal_state:  # Check if the goal state is reached
                self.total_time = time.time() - start_time  # Calculate total time
                return self.get_path(came_from, current)  # Return the path

            # Explore neighbors of the current state
            for next_state in self.get_neighbors(current):
                if next_state not in visited:  # Process only unvisited states
                    visited[next_state] = 0  # Mark the state as visited
                    frontier.put([next_state,path_length+1])  # Add the neighbor to the frontier
                    came_from[next_state] = current  # Record where we came from

        self.total_time = time.time() - start_time  # If no solution, compute total time
        return None  # Return no solution

    def get_neighbors(self, state):
        """
        Generates neighboring states by moving the blank tile (0).

        Args:
            state (str): The current puzzle state.

        Returns:
            A list of neighboring states resulting from valid moves.
        """
        i = state.index('0')  # Locate the blank tile (0)
        neighbors = []

        # Move the blank tile up if possible
        if i - 3 >= 0:
            neighbors.append(self.swap(state, i, i - 3))

        # Move the blank tile right if possible
        if i % 3 < 2:  # Ensures valid right move
            neighbors.append(self.swap(state, i, i + 1))

        # Move the blank tile left if possible
        if i % 3 > 0:  # Ensures valid left move
            neighbors.append(self.swap(state, i, i - 1))

        # Move the blank tile down if possible
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
            str: A new state with the characters swapped.
        """
        state = list(state)  # Convert the state to a list for mutability
        state[i], state[j] = state[j], state[i]  # Swap the tiles
        return ''.join(state)  # Return the modified state as a string

    def get_path(self, came_from, current):
        """
        Reconstructs the path from the start state to the goal state.

        Args:
            came_from (dict): Tracks the predecessor of each state.
            current (str): The current state (goal state).

        Returns:
            list: The path from the start to the goal state.
        """
        path = []
        while current in came_from:  # Trace back from the goal to the start
            path.append(current)  # Add each state to the path
            current = came_from[current]  # Move to the predecessor state
        path.reverse()  # Reverse the path to start with the initial state
        return path


    def get_info(self):
        """
        Returns information about the search process.

        Returns:
            A dictionary containing the number of explored nodes, total execution time, and search depth.
        """

        return {
            'explored nodes': self.explored_nodes,  # Number of nodes explored
            'total time': round(self.total_time,3),  # Total time taken for the search
            'max search depth': self.search_depth,  # Maximum search depth reached
        }