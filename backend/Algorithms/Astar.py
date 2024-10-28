import heapq
import time

class AStar:
    def __init__(self, start_state, goal_state='012345678', heuristic='Manhattan'):
        """
        Initializes the A* search algorithm.

        Args:
            start_state (str): The initial state of the puzzle.
            goal_state (str): The goal state of the puzzle (default is '012345678').
            heuristic (str): The heuristic function to use (default is 'Manhattan').
        """
        self.start_state = start_state
        self.goal_state = goal_state
        self.heuristic = heuristic
        self.explored_nodes = 0  # Track the number of explored nodes
        self.search_depth = 0  # Track the maximum search depth reached
        self.total_time = 0  # Track the total execution time
        self.cost=0 # Computed cost

    def run(self):
        """
        Runs the A* search algorithm.

        Returns:
            A tuple containing the path to the goal state and the total cost.
        """
        start_time = time.time()  # Start timing the algorithm
        frontier = []  # Priority queue for nodes to explore
        heapq.heappush(frontier, (0, self.start_state, 0))  # Push the initial state with a cost of 0
        came_from = {}  # Dictionary to store the path to reach each node
        cost_so_far = {self.start_state: 0}  # Dictionary to store the cost to reach each state

        while frontier:  # Loop while there are nodes in the frontier
            _, current, path_length = heapq.heappop(frontier)  # Get the node with the lowest cost
            self.explored_nodes += 1  # Increment the number of explored nodes
            self.search_depth = max(self.search_depth, path_length)  # Update the maximum search depth

            if current == self.goal_state:  # If the current node is the goal state
                self.total_time = time.time() - start_time  # Calculate total time
                self.cost= cost_so_far[current]
                return self.get_path(came_from, current), cost_so_far[current]  # Return the path and cost

            # Loop through the neighbors of the current state
            for next_state, cost in self.get_neighbors(current):
                new_cost = cost_so_far[current] + cost  # Calculate the new cost to reach the neighbor
                # If the neighbor is unvisited or the new cost is lower than a previous visit
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost  # Update the cost to reach the neighbor
                    heapq.heappush(frontier, (new_cost, next_state, path_length+1))  # Add the neighbor to the frontier
                    came_from[next_state] = current  # Record the current state as the predecessor

        # If no solution is found, return None and infinite cost
        self.total_time = time.time() - start_time  # Calculate total time
        return None, float('inf')

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
            neighbors.append((up, self.get_cost(up)))

        # Move the blank tile right (if possible)
        if x < 2:  
            # print("right")
            right = self.swap(state, i, i + 1)  # Swap the blank tile with the tile on the right
            neighbors.append((right, self.get_cost(right)))

        # Move the blank tile left (if possible)
        if x > 0:
            # print("left")
            left = self.swap(state, i, i - 1)  # Swap the blank tile with the tile on the left
            neighbors.append((left, self.get_cost(left)))

        # Move the blank tile down (if possible)
        if y < 2:
            # print("down")
            down = self.swap(state, i, i + 3)  # Swap the blank tile with the tile below
            neighbors.append((down, self.get_cost(down)))

        return neighbors

    def swap(self, state, i, j):
        """
        Swaps two characters in a string.

        Args:
            state (str): The current state of the puzzle.
            i (int): The index of the first character.
            j (int): The index of the second character.

        Returns:
            A new string with the characters at indices i and j swapped.
        """
        state = list(state)  # Convert the string to a list for mutability
        state[i], state[j] = state[j], state[i]  # Swap the characters
        return ''.join(state)  # Convert the list back to a string

    def get_cost(self, state):
        """
        Calculates the heuristic cost to reach the goal state.

        Args:
            state (str): The current state of the puzzle.

        Returns:
            The heuristic cost based on the chosen heuristic function.
        """
        if state == self.goal_state:  # If the state is the goal, return a cost of 0
            return 0
       
        # Use the Manhattan distance as the heuristic cost
        if self.heuristic == 'Manhattan':
            return self.manhattan_distance(state) 
        
        # Otherwise, use the Euclidean distance as the heuristic cost
        return self.euclidean_distance(state)

    def manhattan_distance(self, state):
        """
        Calculates the Manhattan distance for the current state.

        Args:
            state (str): The current state of the puzzle.

        Returns:
            The Manhattan distance from the current state to the goal state.
        """
        distance = 0
        for i in range(9):
            if state[i] != '0':  # Skip the blank tile
                x, y = divmod(i, 3)  # Get the current position (i)
                x_goal, y_goal = divmod(int(state[i]), 3)  # Get the goal position
                distance += abs(x - x_goal) + abs(y - y_goal)  # Calculate Manhattan distance
        return distance

    def euclidean_distance(self, state):
        """
        Calculates the Euclidean distance for the current state.

        Args:
            state (str): The current state of the puzzle.

        Returns:
            The Euclidean distance from the current state to the goal state.
        """
        distance = 0
        for i in range(9):
            if state[i] != '0':  # Skip the blank tile
                x, y = divmod(i, 3)  # Get the current position (i)
                x_goal, y_goal = divmod(int(state[i]), 3)  # Get the goal position
                distance += ((x - x_goal)**2 + (y - y_goal)**2)**0.5  # Calculate Euclidean distance
        return distance

    def get_path(self, came_from, current):
        """
        Reconstructs the path from the start state to the goal state.

        Args:
            came_from (dict): A dictionary mapping each state to its predecessor.
            current (str): The current state (goal state).

        Returns:
            A list representing the path from the start state to the goal state.
        """
        path = []
        while current in came_from:  # Trace back from the goal state to the start state
            path.append(current)  # Add the current state to the path
            current = came_from[current]  # Move to the predecessor state
        path.reverse()  # Reverse the path to get it from start to goal
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
            'cost':round(self.cost,3)
        }
