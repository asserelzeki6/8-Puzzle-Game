from it_dfs import IT_DFS
from Astar import AStar
from bfs import BFS
from dfs import DFS

# IT_DFS
it_dfs = IT_DFS("041586732","012345678")
# it_dfs.run()
print("IT_DFS Path:", it_dfs.run())
print(f"IT_DFS Info: {it_dfs.get_info()}")

# AStar
a_star = AStar("041586732","012345678","Euclidean")
# a_star.run()
print("AStar Euclidean Path:", a_star.run())
print(f"AStar Euclidean Info: {a_star.get_info()}")

# AStar
a_star = AStar("041586732","012345678","Manhattan")
print("AStar Manhattan Path:", a_star.run())
# a_star.run()
print(f"AStar Manhattan Info: {a_star.get_info()}")


# BFS
bfs = BFS("041586732","012345678")
print("BFS Path:", bfs.run())
# bfs.run()
print(f"BFS Info: {bfs.get_info()}")

# DFS
dfs = DFS("041586732","012345678")
print("DFS Path:", dfs.run())
# dfs.run()
print(f"DFS Info: {dfs.get_info()}")
