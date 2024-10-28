import time

class IT_DFS:
    def __init__(self, start_state, goal_state='012345678',max_depth=500):
        """
        Initializes the IDDFS search algorithm.

        Args:
            start_state (str): The initial state of the puzzle.
            goal_state (str): The goal state of the puzzle (default is '012345678').
            heuristic (str): The heuristic function to use (not used in IDDFS but included for consistency).
        """
        self.start_state = start_state
        self.goal_state = goal_state
        self.max_depth = max_depth  # Maximum depth to explore
        self.explored_nodes = 0  # Tracks the number of explored nodes
        self.search_depth = 0  # Maximum depth reached during the search
        self.total_time = 0  # Total time taken to complete the search

    def run(self):
        """
        Executes the IDDFS algorithm.

        Returns:
            A list representing the path to the goal state, or None if no path is found.
        """
        start_time = time.time()  # Start timing the search
        limit = 0  # Initial depth limit
        self.max_depth = 500  # Maximum depth to explore

        while limit < self.max_depth:  # Iteratively deepen until max_depth is reached
            frontier = [(self.start_state, 0)]  # Stack with initial state and depth 0
            came_from = {}  # Maps each state to its predecessor for path reconstruction
            visited = {self.start_state: 0}  # Tracks visited states

            while frontier:  # Continue while there are states in the stack
                current, depth = frontier.pop()  # Pop the last state added (LIFO)
                self.explored_nodes += 1  # Increment the count of explored nodes
                # self.search_depth = max(self.search_depth, len(self.get_path(came_from,current)))  # Update the maximum search depth

                if current == self.goal_state:  # Check if the goal state is reached
                    self.total_time = time.time() - start_time  # Calculate total search time
                    self.search_depth=depth
                    return self.get_path(came_from, current)  # Return the path to the goal

                if depth < limit and (current not in visited or depth < visited[current]):
                    visited[current] = depth  # Mark as visited with current depth

                    # Explore neighbors of the current state
                    for next_state in self.get_neighbors(current):
                        if next_state not in visited or depth + 1 < visited.get(next_state, float('inf')):
                            frontier.append((next_state, depth + 1))  # Add to the stack with incremented depth
                            came_from[next_state] = current  # Track predecessor for path reconstruction

            limit += 1  # Increase depth limit for the next iteration

        self.total_time = time.time() - start_time  # Calculate total time if no solution is found
        return None  # Return None if no solution exists

    def get_neighbors(self, state):
        """
        Finds the neighboring states by moving the blank tile ('0') up, down, left, or right.

        Args:
            state (str): The current state of the puzzle.

        Returns:
            A list of tuples where each tuple contains the neighbor state and the associated move cost.
        """
        i = state.index('0')  # Find the index of the blank space (0)
        y, x = divmod(i, 3)
        # print(i,x,y)
        neighbors = []

        # Move the blank tile up (if possible)
        if y > 0:
            # print("up")
            up = self.swap(state, i, i - 3)  # Swap the blank tile with the tile above
            neighbors.append(up)

        # Move the blank tile right (if possible)
        if x < 2:  
            # print("right")
            right = self.swap(state, i, i + 1)  # Swap the blank tile with the tile on the right
            neighbors.append(right)

        # Move the blank tile left (if possible)
        if x > 0:
            # print("left")
            left = self.swap(state, i, i - 1)  # Swap the blank tile with the tile on the left
            neighbors.append(left)

        # Move the blank tile down (if possible)
        if y < 2:
            # print("down")
            down = self.swap(state, i, i + 3)  # Swap the blank tile with the tile below
            neighbors.append(down)

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
        Returns information about the search process.

        Returns:
            A dictionary containing the number of explored nodes, total execution time, and search depth.
        """

        return {
            'explored nodes': self.explored_nodes,  # Number of nodes explored
            'total time': round(self.total_time,3),  # Total time taken for the search
            'max search depth': self.search_depth,  # Maximum search depth reached
        }
