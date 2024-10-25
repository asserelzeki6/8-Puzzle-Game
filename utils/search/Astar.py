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
        self.explored_nodes = 0
        self.search_depth = 0
        self.total_time = 0

    def run(self):
        """
        Runs the A* search algorithm.

        Returns:
            A tuple containing the path to the goal state and the total cost.
        """
        start_time = time.time()
        frontier = []
        heapq.heappush(frontier, (0, self.start_state))
        came_from = {}
        cost_so_far = {self.start_state: 0}

        while frontier:
            _, current = heapq.heappop(frontier)
            self.explored_nodes += 1

            if current == self.goal_state:
                self.total_time = time.time() - start_time
                return self.get_path(came_from, current), cost_so_far[current]

            for next_state, cost in self.get_neighbors(current):
                new_cost = cost_so_far[current] + cost
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost
                    # priority = new_cost + self.heuristic(next_state, self.goal_state)
                    heapq.heappush(frontier, (new_cost, next_state))
                    came_from[next_state] = current
                    self.search_depth = max(self.search_depth, len(came_from))

        self.total_time = time.time() - start_time
        return None, float('inf')

    def get_neighbors(self, state):
        i = state.index('0')
        neighbors = []
        if i - 3 >= 0:
            up = self.swap(state, i, i - 3)
            neighbors.append((up, self.get_cost(up)))
        if i - 1 >= 2:
            right = self.swap(state, i, i - 1)
            neighbors.append((right, self.get_cost(right)))
        if i + 1 < 9:
            left = self.swap(state, i, i + 1)
            neighbors.append((left, self.get_cost(left)))
        if i + 3 < 9:
            down = self.swap(state, i, i + 3)
            neighbors.append((down, self.get_cost(down)))
        return neighbors
    
    def swap(self, state, i, j):
        state = list(state)
        state[i], state[j] = state[j], state[i]
        return ''.join(state)
    
    def get_cost(self, state):
        if state == self.goal_state:
            return 0
       
        if self.heuristic == 'Manhattan':
            return self.manhattan_distance(state)
        
        return self.euclidean_distance(state)
    
    def manhattan_distance(self, state):
        distance = 0
        for i in range(9):
            if state[i] != '0':  # Skip the blank space (represented by '0')
                x, y = divmod(i, 3)  # Get the current position (i)
                x_goal, y_goal = divmod(int(state[i]), 3)  # Get the goal position based on the value in state[i]
                distance += abs(x - x_goal) + abs(y - y_goal)  # Calculate Manhattan distance
        return distance
    
    def euclidean_distance(self, state):
        distance = 0
        for i in range(9):
            if state[i] != '0':  # Skip the blank space (represented by '0')
                x, y = divmod(i, 3)  # Get the current position (i)
                x_goal, y_goal = divmod(int(state[i]), 3)  # Get the goal position based on the value in state[i]
                distance += ((x - x_goal)**2 + (y - y_goal)**2)**0.5  # Calculate Euclidean distance
        return distance


    def get_path(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

    def get_info(self):
        return {
            'explored_nodes': self.explored_nodes,
            'total_time': self.total_time,
            'search_depth': self.search_depth
        }