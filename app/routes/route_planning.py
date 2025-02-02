# from flask import Blueprint, jsonify

# route_planning = Blueprint('route_planning', __name__, url_prefix="/api/route")

# import heapq
# from collections import deque

# class Graph:
#     def __init__(self, graph):
#         self.graph = graph
    
#     def bfs(self, start, goal):
#         queue = deque([(start, [start])])
#         visited = set()
#         while queue:
#             node, path = queue.popleft()
#             if node == goal:
#                 return path
#             if node not in visited:
#                 visited.add(node)
#                 for neighbor in self.graph[node]:
#                     queue.append((neighbor, path + [neighbor]))
#         return None
    
#     def dfs(self, start, goal, path=None, visited=None):
#         if visited is None:
#             visited = set()
#         if path is None:
#             path = []
#         path.append(start)
#         visited.add(start)
#         if start == goal:
#             return path
#         for neighbor in self.graph[start]:
#             if neighbor not in visited:
#                 result = self.dfs(neighbor, goal, path.copy(), visited.copy())
#                 if result:
#                     return result
#         return None
    
#     def greedy_best_first_search(self, start, goal, heuristic):
#         priority_queue = [(heuristic[start], start, [start])]
#         visited = set()
#         while priority_queue:
#             _, node, path = heapq.heappop(priority_queue)
#             if node == goal:
#                 return path
#             if node not in visited:
#                 visited.add(node)
#                 for neighbor in self.graph[node]:
#                     heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))
#         return None
    
#     def a_star(self, start, goal, heuristic, weights):
#         priority_queue = [(0, start, [start])]
#         g_scores = {node: float('inf') for node in self.graph}
#         g_scores[start] = 0
#         while priority_queue:
#             current_g, node, path = heapq.heappop(priority_queue)
#             if node == goal:
#                 return path
#             for neighbor in self.graph[node]:
#                 tentative_g = current_g + weights[node][neighbor]
#                 if tentative_g < g_scores[neighbor]:
#                     g_scores[neighbor] = tentative_g
#                     f_score = tentative_g + heuristic[neighbor]
#                     heapq.heappush(priority_queue, (f_score, neighbor, path + [neighbor]))
#         return None

# # Edge weights (road length, speed limit, traffic congestion factors)
# graph_data = {
#     "Bishan": {"Seletar": {"length": 4.1, "speed": 60, "traffic": {"8 AM-12 PM": 1.75}}, 
#                "Ang Mo Kio": {"length": 2.2, "speed": 50, "traffic": {"8 AM-12 PM": 1.60}},
#                "Potong Pasir": {"length": 4.3, "speed": 60, "traffic": {"8 AM-12 PM": 1.75}}},
#     "Seletar": {"Punggol": {"length": 2.2, "speed": 70, "traffic": {"8 AM-12 PM": 1.40}}, 
#                 "Ang Mo Kio": {"length": 2.9, "speed": 55, "traffic": {"8 AM-12 PM": 1.70}}},
#     # Add other nodes here...
# }

# # graph_data= {
# #     "Bishan": ["Seletar", "Ang Mo Kio", "Potong Pasir"],
# #     "Seletar": ["Punggol", "Ang Mo Kio"], 
# #     "Ang Mo Kio": ["Serangoon"],
# #     "Potong Pasir": ["Serangoon", "MacPherson"],
# #     "Punggol": ["Pasir Ris", "Sengkang"],
# #     "Sengkang": ["Serangoon", "Hougang"],
# #     "Serangoon": ["Hougang"],
# #     "Hougang": ["Paya Lebar"],
# #     "Pasir Ris": ["Paya Lebar", "Tampines"],
# #     "Paya Lebar": ["Tampines", "MacPherson"],
# #     "MacPherson": ["Bedok"],
# #     "Bedok": ["Tampines"]
# # }

# # Example Manhattan Distance as Heuristic
# example_heuristic = {
#     "Bishan": 8,
#     "Seletar": 6,
#     "Punggol": 5,
#     "Pasir Ris": 3,
#     "Ang Mo Kio": 7,
#     "Sengkang": 4,
#     "Serangoon": 4,
#     "Hougang": 3,
#     "Paya Lebar": 2,
#     "MacPherson": 1,
#     "Tampines": 0,
#     "Bedok": 0
# }

# # Example Euclidean Distance as Heuristic
# example_weights = {
#     "Bishan": {"Seletar": 2, "Ang Mo Kio": 3, "Potong Pasir": 4},
#     "Seletar": {"Punggol": 2, "Ang Mo Kio": 1},
#     "Ang Mo Kio": {"Serangoon": 1},
#     "Potong Pasir": {"Serangoon": 2, "MacPherson": 3},
#     "Punggol": {"Pasir Ris": 3, "Sengkang": 2},
#     "Sengkang": {"Serangoon": 2, "Hougang": 1},
#     "Serangoon": {"Hougang": 1},
#     "Hougang": {"Paya Lebar": 2},
#     "Pasir Ris": {"Paya Lebar": 2, "Tampines": 1},
#     "Paya Lebar": {"Tampines": 1, "MacPherson": 1},
#     "MacPherson": {"Bedok": 2},
#     "Bedok": {"Tampines": 1}
# }
    

# # Create Graph Object
# graph = Graph(graph_data)

# # Example Usage
# bfs_path = graph.bfs("Bishan", "Tampines")
# dfs_path = graph.dfs("Bishan", "Tampines")
# gbfs_path = graph.greedy_best_first_search("Bishan", "Tampines", example_heuristic)
# a_star_path = graph.a_star("Bishan", "Tampines", example_heuristic, example_weights)

# print("BFS Path:", bfs_path)
# print("DFS Path:", dfs_path)
# print("GBFS Path:", gbfs_path)
# print("A* Path:", a_star_path)

# @route_planning.route('/test', methods=['GET'])
# def test():
#     return jsonify({"message": "Route Planning API is working!"})

# import heapq
# from collections import deque
# import math
# import time  # Import time module to track runtime
# from flask import Flask, jsonify, Blueprint, request, send_file
# import networkx as nx
# import matplotlib.pyplot as plt
# import io
# from io import BytesIO
# import matplotlib.animation as animation
# from matplotlib.animation import FuncAnimation, FFMpegWriter

# # Define the Writer for FFMpeg
# writer = FFMpegWriter(fps=1)

# # Ensure we use a non-GUI backend for matplotlib (helps avoid issues with Flask's threaded environment)
# import matplotlib
# matplotlib.use('Agg')  # Use 'Agg' backend to avoid GUI-related issues

# from matplotlib import rc
# rc('animation', html='html5')  # Set the animation output to HTML5 for better compatibility


# # Graph Data with traffic congestion for different times of the day
# graph_data = {
#     "Bishan": {
#         "Seletar": {"length": 4.1, "speed": 60, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.20, "8 AM-12 PM": 1.75, "12-4 PM": 1.40, 
#             "4-8 PM": 1.85, "8 PM-12 AM": 1.15
#         }},
#         "Ang Mo Kio": {"length": 2.2, "speed": 50, "traffic": {
#             "12-4 AM": 1.02, "4-8 AM": 1.15, "8 AM-12 PM": 1.60, "12-4 PM": 1.30, 
#             "4-8 PM": 1.75, "8 PM-12 AM": 1.10
#         }},
#         "Potong Pasir": {"length": 4.3, "speed": 60, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.25, "8 AM-12 PM": 1.80, "12-4 PM": 1.50, 
#             "4-8 PM": 1.90, "8 PM-12 AM": 1.20
#         }},
#     },
#     "Seletar": {
#         "Punggol": {"length": 2.2, "speed": 70, "traffic": {
#             "12-4 AM": 1.02, "4-8 AM": 1.10, "8 AM-12 PM": 1.40, "12-4 PM": 1.25, 
#             "4-8 PM": 1.50, "8 PM-12 AM": 1.10
#         }},
#         "Ang Mo Kio": {"length": 2.9, "speed": 55, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.20, "8 AM-12 PM": 1.70, "12-4 PM": 1.40, 
#             "4-8 PM": 1.85, "8 PM-12 AM": 1.15
#         }},
#     },
#     "Ang Mo Kio": {
#         "Serangoon": {"length": 3.2, "speed": 50, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.20, "8 AM-12 PM": 1.65, "12-4 PM": 1.40, 
#             "4-8 PM": 1.80, "8 PM-12 AM": 1.10
#         }},
#     },
#     "Potong Pasir": {
#         "Serangoon": {"length": 2.0, "speed": 60, "traffic": {
#             "12-4 AM": 1.02, "4-8 AM": 1.10, "8 AM-12 PM": 1.50, "12-4 PM": 1.30, 
#             "4-8 PM": 1.60, "8 PM-12 AM": 1.10
#         }},
#         "MacPherson": {"length": 2.4, "speed": 50, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.25, "8 AM-12 PM": 1.60, "12-4 PM": 1.40, 
#             "4-8 PM": 1.70, "8 PM-12 AM": 1.20
#         }},
#     },
#     "Punggol": {
#         "Pasir Ris": {"length": 2.5, "speed": 70, "traffic": {
#             "12-4 AM": 1.02, "4-8 AM": 1.10, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
#             "4-8 PM": 1.50, "8 PM-12 AM": 1.10
#         }},
#         "Sengkang": {"length": 1.3, "speed": 70, "traffic": {
#             "12-4 AM": 1.01, "4-8 AM": 1.05, "8 AM-12 PM": 1.15, "12-4 PM": 1.20, 
#             "4-8 PM": 1.30, "8 PM-12 AM": 1.05
#         }},
#     },
#     "Sengkang": {
#         "Serangoon": {"length": 2.8, "speed": 60, "traffic": {
#             "12-4 AM": 1.02, "4-8 AM": 1.10, "8 AM-12 PM": 1.50, "12-4 PM": 1.30, 
#             "4-8 PM": 1.60, "8 PM-12 AM": 1.10
#         }},
#         "Hougang": {"length": 1.3, "speed": 60, "traffic": {
#             "12-4 AM": 1.02, "4-8 AM": 1.15, "8 AM-12 PM": 1.40, "12-4 PM": 1.30, 
#             "4-8 PM": 1.50, "8 PM-12 AM": 1.10
#         }},
#     },
#     "Serangoon": {
#         "Hougang": {"length": 4.1, "speed": 55, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.20, "8 AM-12 PM": 1.60, "12-4 PM": 1.40, 
#             "4-8 PM": 1.70, "8 PM-12 AM": 1.10
#         }},
#     },
#     "Hougang": {
#         "Paya Lebar": {"length": 1.4, "speed": 50, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.50, "12-4 PM": 1.30, 
#             "4-8 PM": 1.60, "8 PM-12 AM": 1.10
#         }},
#     },
#     "Pasir Ris": {
#         "Paya Lebar": {"length": 1.5, "speed": 50, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.10, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
#             "4-8 PM": 1.50, "8 PM-12 AM": 1.10
#         }},
#         "Tampines": {"length": 2.7, "speed": 50, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
#             "4-8 PM": 1.50, "8 PM-12 AM": 1.10
#         }},
#     },
#     "Paya Lebar": {
#         "Tampines": {"length": 1.7, "speed": 55, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
#             "4-8 PM": 1.50, "8 PM-12 AM": 1.10
#         }},
#         "MacPherson": {"length": 3.8, "speed": 60, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
#             "4-8 PM": 1.50, "8 PM-12 AM": 1.10
#         }},
#     },
#     "MacPherson": {
#         "Bedok": {"length": 1.9, "speed": 55, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
#             "4-8 PM": 1.50, "8 PM-12 AM": 1.10
#         }},
#     },
#     "Bedok": {
#         "Tampines": {"length": 4.1, "speed": 50, "traffic": {
#             "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
#             "4-8 PM": 1.50, "8 PM-12 AM": 1.10
            
#         }},
#     },
#     "Tampines": {}  # Added missing node
# }

# # Coordinates for each node in the graph
# coordinates = {
#     "Bishan": (0, 0),
#     "Seletar": (2.5, 3.1),
#     "Punggol": (3.6, 3.0),
#     "Potong Pasir": (2.8, -2.0),
#     "Ang Mo Kio": (1.2, 1.3),
#     "Sengkang": (3.4, 2.0),
#     "Serangoon": (3.0, -0.3),
#     "Hougang": (4.1, 1.2),
#     "Paya Lebar": (5.1, 1.5),
#     "Pasir Ris": (5.6, 2.4),
#     "MacPherson": (4.8, -1.8),
#     "Tampines": (6.5, 0.2),
#     "Bedok": (5.8, -0.4)
# }

# # Manhattan Distance as Heuristic
# def calculate_manhattan_distance(node1, node2, coordinates):
#     x1, y1 = coordinates[node1]
#     x2, y2 = coordinates[node2]
#     return abs(x2 - x1) + abs(y2 - y1)

# # Euclidean Distance as Heuristic
# def calculate_euclidean_distance(node1, node2, coordinates):
#     x1, y1 = coordinates[node1]
#     x2, y2 = coordinates[node2]
#     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# # Graph class that contains algorithms for shortest path calculations
# class Graph:
#     def __init__(self, graph, coordinates):
#         self.graph = graph
#         self.coordinates = coordinates
#         self.fig, self.ax = plt.subplots(figsize=(12, 8))  # Create a figure and axis for visualization
#         self.G = nx.Graph()  # NetworkX graph object
#         self.pos = coordinates  # Node positions for drawing
#         self.visited_order = []  # List to store nodes visited during algorithm execution
#         self.current_path = []  # List to store the current path from start to goal nodes
        
#    # Tracked BFS algorithm (video)
#     def _tracked_bfs(self, start, goal):
#         visited = set()
#         queue = deque([(start, [start])])
#         while queue:
#             node, path = queue.popleft()
#             self.visited_order.append(node)  # Track visited node
#             if node == goal:
#                 return path
#             if node not in visited:
#                 visited.add(node)
#                 for neighbor in self.graph[node]:
#                     if neighbor not in visited:
#                         queue.append((neighbor, path + [neighbor]))
#         return None

#     # Tracked DFS algorithm (video)
#     def _tracked_dfs(self, start, goal):
#         visited = set()
#         stack = [(start, [start])]
#         while stack:
#             node, path = stack.pop()
#             self.visited_order.append(node)  # Track visited node
#             if node == goal:
#                 return path
#             if node not in visited:
#                 visited.add(node)
#                 for neighbor in self.graph[node]:
#                     if neighbor not in visited:
#                         stack.append((neighbor, path + [neighbor]))
#         return None

#     # Tracked Greedy Best-First Search (GBFS) algorithm (video)
#     def _tracked_gbfs(self, start, goal, heuristic_func):
#         visited = set()
#         queue = [(heuristic_func(start, goal, self.coordinates), start, [start])]
#         while queue:
#             _, node, path = heapq.heappop(queue)
#             self.visited_order.append(node)  # Track visited node
#             if node == goal:
#                 return path
#             if node not in visited:
#                 visited.add(node)
#                 for neighbor in self.graph[node]:
#                     if neighbor not in visited:
#                         heapq.heappush(queue, (heuristic_func(neighbor, goal, self.coordinates), neighbor, path + [neighbor]))
#         return None

#     # Tracked A* algorithm (video)
#     def _tracked_astar(self, start, goal, heuristic_func, start_time):
#         heuristic = {node: heuristic_func(node, goal, self.coordinates) for node in self.graph}
#         open_list = [(0, start, [start], start_time)]
#         g_scores = {node: float('inf') for node in self.graph}
#         g_scores[start] = 0
#         while open_list:
#             current_f, node, path, current_time = heapq.heappop(open_list)
#             self.visited_order.append(node)  # Track visited node
#             if node == goal:
#                 return path
#             for neighbor, edge_data in self.graph[node].items():
#                 travel_time = self.calculate_travel_time(node, neighbor, edge_data, current_time)
#                 new_time = self.update_time(current_time, travel_time)
#                 congestion_factor = self.get_congestion_factor(new_time, edge_data)
#                 time_cost = (edge_data["length"] / edge_data["speed"]) * congestion_factor
#                 tentative_g = g_scores[node] + time_cost
#                 if tentative_g < g_scores.get(neighbor, float('inf')):
#                     g_scores[neighbor] = tentative_g
#                     f_score = tentative_g + heuristic.get(neighbor, 0)
#                     heapq.heappush(open_list, (f_score, neighbor, path + [neighbor], new_time))
#         return None
  
#    # Algorithm wrappers (bfs, dfs, gbfs, astar)
#     def bfs(self, start, goal):
#         return self._tracked_bfs(start, goal)

#     def dfs(self, start, goal):
#         return self._tracked_dfs(start, goal)

#     def greedy_best_first_search(self, start, goal, heuristic_func):
#         return self._tracked_gbfs(start, goal, heuristic_func)

#     def a_star(self, start, goal, heuristic_func, start_time="8:00 AM"):
#         return self._tracked_astar(start, goal, heuristic_func, start_time)
    
#     # Visualization functions
#     def visualize_traversal(self, algorithm_name, start, goal, path=None):
#         """ Visualize traversal steps, highlight visited nodes in different colors """
#         self.ax.clear()
#         visited_nodes = self.visited_order if path is None else path
#         # Draw nodes
#         for node in self.graph:
#             color = 'red' if node in visited_nodes else 'blue'
#             self.ax.scatter(self.coordinates[node][0], self.coordinates[node][1], color=color)
#             self.ax.text(self.coordinates[node][0] + 0.1, self.coordinates[node][1] + 0.1, node, fontsize=12)

#         # Draw edges
#         for node in self.graph:
#             for neighbor in self.graph[node]:
#                 self.ax.plot(
#                     [self.coordinates[node][0], self.coordinates[neighbor][0]],
#                     [self.coordinates[node][1], self.coordinates[neighbor][1]],
#                     color='gray', linestyle='--'
#                 )
#         plt.title(f"{algorithm_name} from {start} to {goal}")
#         plt.pause(0.1)

#     # Animation function to animate the algorithm progress
#     def animate_algorithm(self, algorithm_name, start, goal, path=None):
#     # Create an animation of the algorithm's progress
#        def update_plot(frame):
#         self.visualize_traversal(algorithm_name, start, goal, path[:frame])

#        # Animate algorithm steps
#        ani = FuncAnimation(self.fig, update_plot, frames=len(self.visited_order) + 1, repeat=False)
#        buf = io.BytesIO()
#        ani.save(buf, writer=writer)  # Correctly save the animation using the writer
#        buf.seek(0)
#       # Return the animation as a response (sending the video file)
#        return send_file(buf, mimetype='video/mp4')


#     # # A* Algorithm
#     # def a_star(self, start, goal, heuristic_func, start_time="8:00 AM"):
#     #     heuristic = {node: heuristic_func(node, goal, self.coordinates) for node in self.graph}
#     #     open_list = [(0, start, [start], start_time)]
#     #     g_scores = {node: float('inf') for node in self.graph}
#     #     g_scores[start] = 0
#     #     while open_list:
#     #         current_f, node, path, current_time = heapq.heappop(open_list)
#     #         if node == goal:
#     #             return path
#     #         if node not in self.graph:
#     #             continue  # Skip nodes with no outgoing edges
#     #         for neighbor, edge_data in self.graph[node].items():
#     #             travel_time = self.calculate_travel_time(node, neighbor, edge_data, current_time)
#     #             new_time = self.update_time(current_time, travel_time)
#     #             congestion_factor = self.get_congestion_factor(new_time, edge_data)
#     #             time_cost = (edge_data["length"] / edge_data["speed"]) * congestion_factor
#     #             tentative_g = g_scores[node] + time_cost
#     #             if tentative_g < g_scores.get(neighbor, float('inf')):
#     #                 g_scores[neighbor] = tentative_g
#     #                 f_score = tentative_g + heuristic.get(neighbor, 0)
#     #                 heapq.heappush(open_list, (f_score, neighbor, path + [neighbor], new_time))
#     #     return None
    
#     # def greedy_best_first_search(self, start, goal, heuristic_func):
#     #     heuristic = {node: heuristic_func(node, goal, self.coordinates) for node in self.graph}
#     #     heap = [(heuristic[start], start, [start])]
#     #     visited = set()
#     #     while heap:
#     #         _, node, path = heapq.heappop(heap)
#     #         if node == goal:
#     #             return path
#     #         if node in visited or node not in self.graph:
#     #             continue
#     #         visited.add(node)
#     #         for neighbor in self.graph[node]:
#     #             if neighbor not in visited:
#     #                 heapq.heappush(heap, (heuristic[neighbor], neighbor, path + [neighbor]))
#     #     return None
    
#     # def bfs(self, start, goal):
#     #     queue = deque([(start, [start])])
#     #     visited = set()
#     #     while queue:
#     #         node, path = queue.popleft()
#     #         if node == goal:
#     #             return path
#     #         if node not in visited:
#     #             visited.add(node)
#     #             for neighbor in self.graph[node]:
#     #                 queue.append((neighbor, path + [neighbor]))
#     #     return None

#     # def dfs(self, start, goal, path=None, visited=None):
#     #     if visited is None:
#     #         visited = set()
#     #     if path is None:
#     #         path = []
#     #     path.append(start)
#     #     visited.add(start)
#     #     if start == goal:
#     #         return path
#     #     for neighbor in self.graph[start]:
#     #         if neighbor not in visited:
#     #             result = self.dfs(neighbor, goal, path.copy(), visited.copy())
#     #             if result:
#     #                 return result
#     #     return None

#     def calculate_travel_time(self, node, neighbor, edge_data, current_time):
#         road_length = edge_data["length"]
#         speed_limit = edge_data["speed"]
#         congestion_factor = self.get_congestion_factor(current_time, edge_data)
#         time_hours = (road_length / speed_limit) * congestion_factor
#         travel_time_minutes = round(time_hours * 60)  # Round to nearest integer
#         return travel_time_minutes

#     def get_congestion_factor(self, current_time, edge_data):
#         current_minutes = self.time_to_minutes(current_time)
#         for time_range, congestion_factor in edge_data["traffic"].items():
#             parts = time_range.split("-")
#             if len(parts) != 2:
#                 continue
#             start_part, end_part = parts[0].strip(), parts[1].strip()
#             start_minutes = self.parse_time_part(start_part, end_part)
#             end_minutes = self.parse_time_part(end_part)
#             if start_minutes <= current_minutes < end_minutes:
#                 return congestion_factor
#         return 1.0

#     def time_in_range(self, current_time, start_range, end_range):
#         # Parse current_time (e.g., "8:00 AM")
#         current_time_clean = current_time.split()[0]  # Remove AM/PM for parsing
#         current_hour, current_minute = map(int, current_time_clean.split(":"))
#         start_hour, start_minute = map(int, start_range.strip().split(":"))
#         end_hour, end_minute = map(int, end_range.strip().split(":"))

#         # Convert to minutes since midnight
#         current_total = current_hour * 60 + current_minute
#         start_total = start_hour * 60 + start_minute
#         end_total = end_hour * 60 + end_minute

#         return start_total <= current_total < end_total
    
#     def time_to_minutes(self, time_str):
#         parts = time_str.split()
#         time_part = parts[0]
#         period = parts[1].upper() if len(parts) > 1 else "AM"
#         if ':' in time_part:
#             hours, minutes = map(int, time_part.split(':'))
#         else:
#             hours = int(time_part)
#             minutes = 0
#         if period == "PM" and hours != 12:
#             hours += 12
#         elif period == "AM" and hours == 12:
#             hours = 0
#         return hours * 60 + minutes

#     def parse_time_part(self, time_part, end_part=None):
#         time_components = time_part.split()
#         if len(time_components) == 2:
#             hour_str, period = time_components
#             period = period.upper()
#         else:
#             hour_str = time_components[0]
#             if end_part:
#                 end_components = end_part.split()
#                 if len(end_components) == 2:
#                     period = end_components[1].upper()
#                 else:
#                     period = "AM"
#             else:
#                 period = "AM"
#         if ':' in hour_str:
#             hours, minutes = map(int, hour_str.split(':'))
#         else:
#             hours = int(hour_str)
#             minutes = 0
#         if period == "PM" and hours != 12:
#             hours += 12
#         elif period == "AM" and hours == 12:
#             hours = 0
#         return hours * 60 + minutes

#     def update_time(self, current_time, travel_time):
#         # Parse current_time (e.g., "8:00 AM")
#         time_parts = current_time.split()
#         time_str, period = time_parts[0], time_parts[1] if len(time_parts) > 1 else "AM"
#         current_hour, current_minute = map(int, time_str.split(":"))

#         # Convert to 24-hour format
#         if period == "PM" and current_hour != 12:
#             current_hour += 12
#         elif period == "AM" and current_hour == 12:
#             current_hour = 0

#         total_minutes = current_hour * 60 + current_minute + travel_time
#         new_hour = (total_minutes // 60) % 24
#         new_minute = total_minutes % 60

#         # Convert back to 12-hour format
#         period = "AM" if new_hour < 12 else "PM"
#         display_hour = new_hour if new_hour <= 12 else new_hour - 12
#         if display_hour == 0:
#             display_hour = 12

#         return f"{int(display_hour)}:{new_minute:02} {period}"  # Cast to integer
    
   


# # Flask Setup
# route_planning = Blueprint('route_planning', __name__, url_prefix="/api/route")
# # Add endpoints
# @route_planning.route('/animate_algorithm', methods=['GET'])
# def animate_algorithm():
#     algorithm = request.args.get('algorithm', 'bfs')
#     start = request.args.get('start', 'Bishan')
#     goal = request.args.get('goal', 'Tampines')

#     graph = Graph(graph_data, coordinates)
    
#     if algorithm == 'bfs':
#         path = graph.bfs(start, goal)
#     elif algorithm == 'dfs':
#         path = graph.dfs(start, goal)
#     elif algorithm == 'gbfs':
#         path = graph.greedy_best_first_search(start, goal, calculate_manhattan_distance)
#     elif algorithm == 'astar':
#         path = graph.a_star(start, goal, calculate_manhattan_distance)

#     video = graph.animate_algorithm(algorithm, start, goal, path)
#     return send_file(video, mimetype='video/mp4')



# @route_planning.route('/shortest-path', methods=['GET'])
# def get_shortest_path():
#     start = request.args.get("start")
#     end = request.args.get("end")
#     algo = request.args.get("algo", "bfs").lower()
#     heuristic_type = request.args.get("heuristic", "manhattan").lower()

#     if not start or not end:
#         return jsonify({"error": "Missing start or end"}), 400

#     if start not in graph_data or end not in graph_data:
#         return jsonify({"error": "Invalid locations"}), 400

#     graph = Graph(graph_data, coordinates)
#     heuristic_func = calculate_manhattan_distance if heuristic_type == "manhattan" else calculate_euclidean_distance

#     if algo == "bfs":
#         path = graph.bfs(start, end)
#     elif algo == "dfs":
#         path = graph.dfs(start, end)
#     elif algo == "gbfs":
#         path = graph.greedy_best_first_search(start, end, heuristic_func)
#     elif algo == "astar":
#         start_time = request.args.get("start_time", "8:00 AM")
#         path = graph.a_star(start, end, heuristic_func, start_time)
#     else:
#         return jsonify({"error": "Invalid algorithm"}), 400

#     return jsonify({"path": path if path else "No path found"})

# app = Flask(__name__)
# app.register_blueprint(route_planning)

# if __name__ == "__main__":
#     app.run(debug=True)
    
import time
import heapq
from collections import deque
import math
from flask import Flask, jsonify, Blueprint, request, send_file
import networkx as nx
import matplotlib.pyplot as plt
import io
from io import BytesIO
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Define the Writer for FFMpeg
writer = FFMpegWriter(fps=1)

# Ensure we use a non-GUI backend for matplotlib (helps avoid issues with Flask's threaded environment)
import matplotlib
matplotlib.use('Agg')  # Use 'Agg' backend to avoid GUI-related issues

from matplotlib import rc
rc('animation', html='html5')  # Set the animation output to HTML5 for better compatibility

# Graph Data with traffic congestion for different times of the day
graph_data = {
    "Bishan": {
        "Seletar": {"length": 4.1, "speed": 60, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.20, "8 AM-12 PM": 1.75, "12-4 PM": 1.40, 
            "4-8 PM": 1.85, "8 PM-12 AM": 1.15
        }},
        "Ang Mo Kio": {"length": 2.2, "speed": 50, "traffic": {
            "12-4 AM": 1.02, "4-8 AM": 1.15, "8 AM-12 PM": 1.60, "12-4 PM": 1.30, 
            "4-8 PM": 1.75, "8 PM-12 AM": 1.10
        }},
        "Potong Pasir": {"length": 4.3, "speed": 60, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.25, "8 AM-12 PM": 1.80, "12-4 PM": 1.50, 
            "4-8 PM": 1.90, "8 PM-12 AM": 1.20
        }},
    },
    "Seletar": {
        "Punggol": {"length": 2.2, "speed": 70, "traffic": {
            "12-4 AM": 1.02, "4-8 AM": 1.10, "8 AM-12 PM": 1.40, "12-4 PM": 1.25, 
            "4-8 PM": 1.50, "8 PM-12 AM": 1.10
        }},
        "Ang Mo Kio": {"length": 2.9, "speed": 55, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.20, "8 AM-12 PM": 1.70, "12-4 PM": 1.40, 
            "4-8 PM": 1.85, "8 PM-12 AM": 1.15
        }},
    },
    "Ang Mo Kio": {
        "Serangoon": {"length": 3.2, "speed": 50, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.20, "8 AM-12 PM": 1.65, "12-4 PM": 1.40, 
            "4-8 PM": 1.80, "8 PM-12 AM": 1.10
        }},
    },
    "Potong Pasir": {
        "Serangoon": {"length": 2.0, "speed": 60, "traffic": {
            "12-4 AM": 1.02, "4-8 AM": 1.10, "8 AM-12 PM": 1.50, "12-4 PM": 1.30, 
            "4-8 PM": 1.60, "8 PM-12 AM": 1.10
        }},
        "MacPherson": {"length": 2.4, "speed": 50, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.25, "8 AM-12 PM": 1.60, "12-4 PM": 1.40, 
            "4-8 PM": 1.70, "8 PM-12 AM": 1.20
        }},
    },
    "Punggol": {
        "Pasir Ris": {"length": 2.5, "speed": 70, "traffic": {
            "12-4 AM": 1.02, "4-8 AM": 1.10, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
            "4-8 PM": 1.50, "8 PM-12 AM": 1.10
        }},
        "Sengkang": {"length": 1.3, "speed": 70, "traffic": {
            "12-4 AM": 1.01, "4-8 AM": 1.05, "8 AM-12 PM": 1.15, "12-4 PM": 1.20, 
            "4-8 PM": 1.30, "8 PM-12 AM": 1.05
        }},
    },
    "Sengkang": {
        "Serangoon": {"length": 2.8, "speed": 60, "traffic": {
            "12-4 AM": 1.02, "4-8 AM": 1.10, "8 AM-12 PM": 1.50, "12-4 PM": 1.30, 
            "4-8 PM": 1.60, "8 PM-12 AM": 1.10
        }},
        "Hougang": {"length": 1.3, "speed": 60, "traffic": {
            "12-4 AM": 1.02, "4-8 AM": 1.15, "8 AM-12 PM": 1.40, "12-4 PM": 1.30, 
            "4-8 PM": 1.50, "8 PM-12 AM": 1.10
        }},
    },
    "Serangoon": {
        "Hougang": {"length": 4.1, "speed": 55, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.20, "8 AM-12 PM": 1.60, "12-4 PM": 1.40, 
            "4-8 PM": 1.70, "8 PM-12 AM": 1.10
        }},
    },
    "Hougang": {
        "Paya Lebar": {"length": 1.4, "speed": 50, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.50, "12-4 PM": 1.30, 
            "4-8 PM": 1.60, "8 PM-12 AM": 1.10
        }},
    },
    "Pasir Ris": {
        "Paya Lebar": {"length": 1.5, "speed": 50, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.10, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
            "4-8 PM": 1.50, "8 PM-12 AM": 1.10
        }},
        "Tampines": {"length": 2.7, "speed": 50, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
            "4-8 PM": 1.50, "8 PM-12 AM": 1.10
        }},
    },
    "Paya Lebar": {
        "Tampines": {"length": 1.7, "speed": 55, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
            "4-8 PM": 1.50, "8 PM-12 AM": 1.10
        }},
        "MacPherson": {"length": 3.8, "speed": 60, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
            "4-8 PM": 1.50, "8 PM-12 AM": 1.10
        }},
    },
    "MacPherson": {
        "Bedok": {"length": 1.9, "speed": 55, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
            "4-8 PM": 1.50, "8 PM-12 AM": 1.10
        }},
    },
    "Bedok": {
        "Tampines": {"length": 4.1, "speed": 50, "traffic": {
            "12-4 AM": 1.05, "4-8 AM": 1.15, "8 AM-12 PM": 1.30, "12-4 PM": 1.25, 
            "4-8 PM": 1.50, "8 PM-12 AM": 1.10
            
        }},
    },
    "Tampines": {}  # Added missing node
}

# Coordinates for each node in the graph
coordinates = {
    "Bishan": (0, 0),
    "Seletar": (2.5, 3.1),
    "Punggol": (3.6, 3.0),
    "Potong Pasir": (2.8, -2.0),
    "Ang Mo Kio": (1.2, 1.3),
    "Sengkang": (3.4, 2.0),
    "Serangoon": (3.0, -0.3),
    "Hougang": (4.1, 1.2),
    "Paya Lebar": (5.1, 1.5),
    "Pasir Ris": (5.6, 2.4),
    "MacPherson": (4.8, -1.8),
    "Tampines": (6.5, 0.2),
    "Bedok": (5.8, -0.4)
}

# Manhattan Distance as Heuristic
def calculate_manhattan_distance(node1, node2, coordinates):
    x1, y1 = coordinates[node1]
    x2, y2 = coordinates[node2]
    return abs(x2 - x1) + abs(y2 - y1)

# Euclidean Distance as Heuristic
def calculate_euclidean_distance(node1, node2, coordinates):
    x1, y1 = coordinates[node1]
    x2, y2 = coordinates[node2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Graph class that contains algorithms for shortest path calculations
class Graph:
    def __init__(self, graph, coordinates):
        self.graph = graph
        self.coordinates = coordinates
        self.fig, self.ax = plt.subplots(figsize=(12, 8))  # Create a figure and axis for visualization
        self.G = nx.Graph()  # NetworkX graph object
        self.pos = coordinates  # Node positions for drawing
        self.visited_order = []  # List to store nodes visited during algorithm execution
        self.current_path = []  # List to store the current path from start to goal nodes
        
   # Tracked BFS algorithm (video)
    def _tracked_bfs(self, start, goal):
        visited = set()
        queue = deque([(start, [start])])
        while queue:
            node, path = queue.popleft()
            self.visited_order.append(node)  # Track visited node
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return None

    # Tracked DFS algorithm (video)
    def _tracked_dfs(self, start, goal):
        visited = set()
        stack = [(start, [start])]
        while stack:
            node, path = stack.pop()
            self.visited_order.append(node)  # Track visited node
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
        return None

    # Tracked Greedy Best-First Search (GBFS) algorithm (video)
    def _tracked_gbfs(self, start, goal, heuristic_func):
        visited = set()
        queue = [(heuristic_func(start, goal, self.coordinates), start, [start])]
        while queue:
            _, node, path = heapq.heappop(queue)
            self.visited_order.append(node)  # Track visited node
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(queue, (heuristic_func(neighbor, goal, self.coordinates), neighbor, path + [neighbor]))
        return None

    # Tracked A* algorithm (video)
    def _tracked_astar(self, start, goal, heuristic_func, start_time):
        heuristic = {node: heuristic_func(node, goal, self.coordinates) for node in self.graph}
        open_list = [(0, start, [start], start_time)]
        g_scores = {node: float('inf') for node in self.graph}
        g_scores[start] = 0
        while open_list:
            current_f, node, path, current_time = heapq.heappop(open_list)
            self.visited_order.append(node)  # Track visited node
            if node == goal:
                return path
            for neighbor, edge_data in self.graph[node].items():
                travel_time = self.calculate_travel_time(node, neighbor, edge_data, current_time)
                new_time = self.update_time(current_time, travel_time)
                congestion_factor = self.get_congestion_factor(new_time, edge_data)
                time_cost = (edge_data["length"] / edge_data["speed"]) * congestion_factor
                tentative_g = g_scores[node] + time_cost
                if tentative_g < g_scores.get(neighbor, float('inf')):
                    g_scores[neighbor] = tentative_g
                    f_score = tentative_g + heuristic.get(neighbor, 0)
                    heapq.heappush(open_list, (f_score, neighbor, path + [neighbor], new_time))
        return None
  
   # Algorithm wrappers (bfs, dfs, gbfs, astar)
    def bfs(self, start, goal):
        return self._tracked_bfs(start, goal)

    def dfs(self, start, goal):
        return self._tracked_dfs(start, goal)

    def greedy_best_first_search(self, start, goal, heuristic_func):
        return self._tracked_gbfs(start, goal, heuristic_func)

    def a_star(self, start, goal, heuristic_func, start_time="8:00 AM"):
        return self._tracked_astar(start, goal, heuristic_func, start_time)
    
    # Visualization functions
    def visualize_traversal(self, algorithm_name, start, goal, path=None):
        """ Visualize traversal steps, highlight visited nodes in different colors """
        self.ax.clear()
        visited_nodes = self.visited_order if path is None else path
        # Draw nodes
        for node in self.graph:
            color = 'red' if node in visited_nodes else 'blue'
            self.ax.scatter(self.coordinates[node][0], self.coordinates[node][1], color=color)
            self.ax.text(self.coordinates[node][0] + 0.1, self.coordinates[node][1] + 0.1, node, fontsize=12)

        # Draw edges
        for node in self.graph:
            for neighbor in self.graph[node]:
                self.ax.plot(
                    [self.coordinates[node][0], self.coordinates[neighbor][0]],
                    [self.coordinates[node][1], self.coordinates[neighbor][1]],
                    color='gray', linestyle='--'
                )
        plt.title(f"{algorithm_name} from {start} to {goal}")
        plt.pause(0.1)

    # Animation function to animate the algorithm progress
    def animate_algorithm(self, algorithm_name, start, goal, path=None):
    # Create an animation of the algorithm's progress
       def update_plot(frame):
        self.visualize_traversal(algorithm_name, start, goal, path[:frame])

       # Animate algorithm steps
       ani = FuncAnimation(self.fig, update_plot, frames=len(self.visited_order) + 1, repeat=False)
       buf = io.BytesIO()
       ani.save(buf, writer=writer)  # Correctly save the animation using the writer
       buf.seek(0)
      # Return the animation as a response (sending the video file)
       return send_file(buf, mimetype='video/mp4')


    # # A* Algorithm
    # def a_star(self, start, goal, heuristic_func, start_time="8:00 AM"):
    #     heuristic = {node: heuristic_func(node, goal, self.coordinates) for node in self.graph}
    #     open_list = [(0, start, [start], start_time)]
    #     g_scores = {node: float('inf') for node in self.graph}
    #     g_scores[start] = 0
    #     while open_list:
    #         current_f, node, path, current_time = heapq.heappop(open_list)
    #         if node == goal:
    #             return path
    #         if node not in self.graph:
    #             continue  # Skip nodes with no outgoing edges
    #         for neighbor, edge_data in self.graph[node].items():
    #             travel_time = self.calculate_travel_time(node, neighbor, edge_data, current_time)
    #             new_time = self.update_time(current_time, travel_time)
    #             congestion_factor = self.get_congestion_factor(new_time, edge_data)
    #             time_cost = (edge_data["length"] / edge_data["speed"]) * congestion_factor
    #             tentative_g = g_scores[node] + time_cost
    #             if tentative_g < g_scores.get(neighbor, float('inf')):
    #                 g_scores[neighbor] = tentative_g
    #                 f_score = tentative_g + heuristic.get(neighbor, 0)
    #                 heapq.heappush(open_list, (f_score, neighbor, path + [neighbor], new_time))
    #     return None
    
    # def greedy_best_first_search(self, start, goal, heuristic_func):
    #     heuristic = {node: heuristic_func(node, goal, self.coordinates) for node in self.graph}
    #     heap = [(heuristic[start], start, [start])]
    #     visited = set()
    #     while heap:
    #         _, node, path = heapq.heappop(heap)
    #         if node == goal:
    #             return path
    #         if node in visited or node not in self.graph:
    #             continue
    #         visited.add(node)
    #         for neighbor in self.graph[node]:
    #             if neighbor not in visited:
    #                 heapq.heappush(heap, (heuristic[neighbor], neighbor, path + [neighbor]))
    #     return None
    
    # def bfs(self, start, goal):
    #     queue = deque([(start, [start])])
    #     visited = set()
    #     while queue:
    #         node, path = queue.popleft()
    #         if node == goal:
    #             return path
    #         if node not in visited:
    #             visited.add(node)
    #             for neighbor in self.graph[node]:
    #                 queue.append((neighbor, path + [neighbor]))
    #     return None

    # def dfs(self, start, goal, path=None, visited=None):
    #     if visited is None:
    #         visited = set()
    #     if path is None:
    #         path = []
    #     path.append(start)
    #     visited.add(start)
    #     if start == goal:
    #         return path
    #     for neighbor in self.graph[start]:
    #         if neighbor not in visited:
    #             result = self.dfs(neighbor, goal, path.copy(), visited.copy())
    #             if result:
    #                 return result
    #     return None

    def calculate_travel_time(self, node, neighbor, edge_data, current_time):
        road_length = edge_data["length"]
        speed_limit = edge_data["speed"]
        congestion_factor = self.get_congestion_factor(current_time, edge_data)
        time_hours = (road_length / speed_limit) * congestion_factor
        travel_time_minutes = round(time_hours * 60)  # Round to nearest integer
        return travel_time_minutes

    def get_congestion_factor(self, current_time, edge_data):
        current_minutes = self.time_to_minutes(current_time)
        for time_range, congestion_factor in edge_data["traffic"].items():
            parts = time_range.split("-")
            if len(parts) != 2:
                continue
            start_part, end_part = parts[0].strip(), parts[1].strip()
            start_minutes = self.parse_time_part(start_part, end_part)
            end_minutes = self.parse_time_part(end_part)
            if start_minutes <= current_minutes < end_minutes:
                return congestion_factor
        return 1.0

    def time_in_range(self, current_time, start_range, end_range):
        # Parse current_time (e.g., "8:00 AM")
        current_time_clean = current_time.split()[0]  # Remove AM/PM for parsing
        current_hour, current_minute = map(int, current_time_clean.split(":"))
        start_hour, start_minute = map(int, start_range.strip().split(":"))
        end_hour, end_minute = map(int, end_range.strip().split(":"))

        # Convert to minutes since midnight
        current_total = current_hour * 60 + current_minute
        start_total = start_hour * 60 + start_minute
        end_total = end_hour * 60 + end_minute

        return start_total <= current_total < end_total
    
    def time_to_minutes(self, time_str):
        parts = time_str.split()
        time_part = parts[0]
        period = parts[1].upper() if len(parts) > 1 else "AM"
        if ':' in time_part:
            hours, minutes = map(int, time_part.split(':'))
        else:
            hours = int(time_part)
            minutes = 0
        if period == "PM" and hours != 12:
            hours += 12
        elif period == "AM" and hours == 12:
            hours = 0
        return hours * 60 + minutes

    def parse_time_part(self, time_part, end_part=None):
        time_components = time_part.split()
        if len(time_components) == 2:
            hour_str, period = time_components
            period = period.upper()
        else:
            hour_str = time_components[0]
            if end_part:
                end_components = end_part.split()
                if len(end_components) == 2:
                    period = end_components[1].upper()
                else:
                    period = "AM"
            else:
                period = "AM"
        if ':' in hour_str:
            hours, minutes = map(int, hour_str.split(':'))
        else:
            hours = int(hour_str)
            minutes = 0
        if period == "PM" and hours != 12:
            hours += 12
        elif period == "AM" and hours == 12:
            hours = 0
        return hours * 60 + minutes

    def update_time(self, current_time, travel_time):
        # Parse current_time (e.g., "8:00 AM")
        time_parts = current_time.split()
        time_str, period = time_parts[0], time_parts[1] if len(time_parts) > 1 else "AM"
        current_hour, current_minute = map(int, time_str.split(":"))

        # Convert to 24-hour format
        if period == "PM" and current_hour != 12:
            current_hour += 12
        elif period == "AM" and current_hour == 12:
            current_hour = 0

        total_minutes = current_hour * 60 + current_minute + travel_time
        new_hour = (total_minutes // 60) % 24
        new_minute = total_minutes % 60

        # Convert back to 12-hour format
        period = "AM" if new_hour < 12 else "PM"
        display_hour = new_hour if new_hour <= 12 else new_hour - 12
        if display_hour == 0:
            display_hour = 12

        return f"{int(display_hour)}:{new_minute:02} {period}"  # Cast to integer
    
   


# Flask Setup
route_planning = Blueprint('route_planning', __name__, url_prefix="/api/route")
# Add endpoints
@route_planning.route('/animate_algorithm', methods=['GET'])
def animate_algorithm():
    algorithm = request.args.get('algorithm', 'bfs')
    start = request.args.get('start', 'Bishan')
    goal = request.args.get('goal', 'Tampines')

    graph = Graph(graph_data, coordinates)
    
    if algorithm == 'bfs':
        path = graph.bfs(start, goal)
    elif algorithm == 'dfs':
        path = graph.dfs(start, goal)
    elif algorithm == 'gbfs':
        path = graph.greedy_best_first_search(start, goal, calculate_manhattan_distance)
    elif algorithm == 'astar':
        path = graph.a_star(start, goal, calculate_manhattan_distance)

    video = graph.animate_algorithm(algorithm, start, goal, path)
    return send_file(video, mimetype='video/mp4')

@route_planning.route('/shortest-path', methods=['GET'])
def get_shortest_path():
    start = request.args.get("start")
    end = request.args.get("end")
    algo = request.args.get("algo", "bfs").lower()
    heuristic_type = request.args.get("heuristic", "manhattan").lower()

    if not start or not end:
        return jsonify({"error": "Missing start or end"}), 400

    if start not in graph_data or end not in graph_data:
        return jsonify({"error": "Invalid locations"}), 400

    graph = Graph(graph_data, coordinates)
    heuristic_func = calculate_manhattan_distance if heuristic_type == "manhattan" else calculate_euclidean_distance

    start_time = time.perf_counter()  # Start the timer

    if algo == "bfs":
        path = graph.bfs(start, end)
    elif algo == "dfs":
        path = graph.dfs(start, end)
    elif algo == "gbfs":
        path = graph.greedy_best_first_search(start, end, heuristic_func)
    elif algo == "astar":
        start_time_request = request.args.get("start_time", "8:00 AM")
        path = graph.a_star(start, end, heuristic_func, start_time_request)
    else:
        return jsonify({"error": "Invalid algorithm"}), 400

    end_time = time.perf_counter()  # End the timer
    runtime = end_time - start_time  # Calculate the time taken

    return jsonify({"path": path if path else "No path found", "runtime": runtime})

app = Flask(__name__)
app.register_blueprint(route_planning)

if __name__ == "__main__":
    app.run(debug=True)
    
    