from flask import Flask, jsonify, request
from flask_cors import CORS
from Algorithms.Astar import AStar
from Algorithms.bfs import BFS
from Algorithms.dfs import DFS
from Algorithms.it_dfs import IT_DFS

 
app = Flask(__name__)
CORS(app)

@app.route('/start', methods=['POST'])  # New endpoint for starting the algorithm
def start_algorithm():
    info = [
    ]
    path = [
        '125670834',  # Initial State
        '125607834',  # Step 1
        '125683074',  # Step 2
        '120683754',  # Step 3
        '123456780'   # Final State
    ]
    data = request.json  # Get JSON data from the request
    initial_input = data.get('inputString')
    goal = data.get('goalString')
    algorithm_name = data.get('algorithmName')

    if algorithm_name == "bfs":
        solver = BFS(initial_input, goal)
        path = solver.run()
    elif algorithm_name == "a-starm":
        solver = AStar(initial_input, goal, heuristic='Manhattan')
        path = solver.run()[0]
    elif algorithm_name == "a-stare":
        solver = AStar(initial_input, goal, heuristic='euclidean')
        path = solver.run()[0]
    elif algorithm_name == "dfs":
        solver = DFS(initial_input, goal)
        path = solver.run()
    elif algorithm_name == "it-dfs":
        solver = IT_DFS(initial_input, goal)
        path = solver.run()

    if path is None:
        print("no solution found")
        return jsonify({
            'message': f'No solution found with input {initial_input} using {algorithm_name}',
            'status': 'failed'
        })
    
    analysis = solver.get_info()

    # Append analysis information to info
    for key, value in analysis.items():
        info.append({"title": key, "value": value})

    print(info)
    print(path)
    return jsonify({
        'message': f'Started solving with input {initial_input} using {algorithm_name}',
        'status': 'success',
        'path': path,
        'info': info
    })


if __name__ == '__main__':
    print("Server is running...")
    app.run(debug=True)
