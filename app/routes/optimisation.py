# from flask import Blueprint, jsonify

# optimisation = Blueprint('optimisation', __name__, url_prefix="/api/optimisation")

# @optimisation.route('/test', methods=['GET'])
# def test():
#     return jsonify({"message": "Optimisation API is working!"})

#Optimisation (Advanced)

# from flask import Flask, Blueprint, jsonify, request
# import random
# import math
# import matplotlib.pyplot as plt

# # Ensure we use a non-GUI backend for matplotlib (helps avoid issues with Flask's threaded environment)
# import matplotlib
# matplotlib.use('Agg')  # Use 'Agg' backend to avoid GUI-related issues

# from matplotlib.animation import FuncAnimation, FFMpegWriter
# from matplotlib import rc

# # Set the animation output to HTML5 for better compatibility
# rc('animation', html='html5')

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


# # Optimisation class handling all the algorithms
# class Optimisation:
#     def __init__(self, graph_data, coordinates):
#         self.graph_data = graph_data
#         self.coordinates = coordinates

#     def calculate_total_time(self, route):
#         """
#         Calculate the total time taken by a route.
#         Each segment of the route's travel time is calculated based on
#         the length of the road, speed limit, and current traffic.
#         """
#         total_time = 0
#         for i in range(len(route) - 1):
#             total_time += self.calculate_travel_time(route[i], route[i + 1])
#         return total_time

#     def calculate_travel_time(self, start, end):
#         """
#         Calculate travel time between two locations based on road length, speed limit, and traffic congestion.
#         """
#         edge_data = self.graph_data[start][end]
#         traffic_factor = self.get_traffic_factor(start, end)
#         travel_time = (edge_data["length"] / edge_data["speed"]) * traffic_factor
#         return travel_time

#     def get_traffic_factor(self, start, end):
#         """
#         Returns a traffic congestion factor based on time of day.
#         For simplicity, returning 1.0 for no congestion.
#         """
#         return 1.0  # Placeholder for actual traffic congestion adjustment

#     def simulated_annealing(self, initial_route, initial_temp=100, cooling_rate=0.95, stopping_temp=0.01, max_iterations=1000):
#         """
#         Simulated Annealing algorithm to optimize the route by gradually lowering the temperature and accepting 
#         worse solutions with a certain probability to escape local optima.
#         """
#         current_route = initial_route
#         current_temp = initial_temp
#         best_route = current_route
#         best_cost = self.calculate_total_time(current_route)

#         for iteration in range(max_iterations):
#             new_route = self.swap_cities(current_route)
#             current_cost = self.calculate_total_time(current_route)
#             new_cost = self.calculate_total_time(new_route)

#             # Accept new route based on temperature
#             if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / current_temp):
#                 current_route = new_route
#                 current_cost = new_cost

#             # Update best route
#             if current_cost < best_cost:
#                 best_route = current_route
#                 best_cost = current_cost

#             # Cool down temperature
#             current_temp *= cooling_rate
#             if current_temp < stopping_temp:
#                 break

#         return best_route, best_cost

#     def hill_climbing(self, initial_route, max_iterations=100):
#         """
#         Hill Climbing algorithm to optimize the route by iteratively improving it by moving to the neighboring route
#         that has the lowest cost.
#         """
#         current_route = initial_route
#         current_cost = self.calculate_total_time(current_route)

#         best_route = current_route
#         best_cost = current_cost

#         for _ in range(max_iterations):
#             new_route = self.swap_cities(current_route)
#             new_cost = self.calculate_total_time(new_route)

#             if new_cost < current_cost:
#                 current_route = new_route
#                 current_cost = new_cost

#             if current_cost < best_cost:
#                 best_route = current_route
#                 best_cost = current_cost

#         return best_route, best_cost

#     def local_search(self, initial_route, max_iterations=100):
#         """
#         Local Search algorithm that iteratively improves the current route by checking neighbors.
#         """
#         current_route = initial_route
#         current_cost = self.calculate_total_time(current_route)

#         best_route = current_route
#         best_cost = current_cost

#         for _ in range(max_iterations):
#             new_route = self.swap_cities(current_route)
#             new_cost = self.calculate_total_time(new_route)

#             if new_cost < current_cost:
#                 current_route = new_route
#                 current_cost = new_cost

#             if current_cost < best_cost:
#                 best_route = current_route
#                 best_cost = current_cost

#         return best_route, best_cost

#     def csp(self, routes, max_iterations=100):
#         """
#         Constraint Satisfaction Problem (CSP) approach, potentially using backtracking or forward checking to ensure
#         constraints like road capacity and delivery time windows are satisfied.
#         """
#         best_route = routes
#         best_cost = sum(self.calculate_total_time(route) for route in routes)

#         # Placeholder for CSP logic
#         # Implement constraint satisfaction (e.g., backtracking, forward checking) here
#         return best_route, best_cost

#     def swap_cities(self, route):
#         """
#         Swap two cities in a route (excluding start and end cities).
#         """
#         new_route = route[:]
#         i, j = random.sample(range(1, len(route) - 1), 2)  # Avoid swapping start/end
#         new_route[i], new_route[j] = new_route[j], new_route[i]
#         return new_route

# # Flask Setup
# optimisation = Blueprint('optimisation', __name__, url_prefix="/api/optimisation")

# @optimisation.route('/optimize_route', methods=['POST'])
# def optimize_route():
#     """
#     Route to trigger optimization algorithm.
#     The client provides the initial route in the body of the request.
#     """
#     data = request.get_json()
#     initial_route = data.get('route', ["Bishan", "Seletar", "Punggol", "Ang Mo Kio", "Potong Pasir", "Serangoon"])
    
#     optimizer = Optimisation(graph_data, coordinates)  # Initialize Optimisation class
#     best_route, best_cost = optimizer.simulated_annealing(initial_route)
#     print(f"Optimizing route: {initial_route}")

    
#     return jsonify({
#         "route": best_route,
#         "cost": best_cost
#     })
    
    

# # Initialize Flask App
# app = Flask(__name__)
# app.register_blueprint(optimisation)

# if __name__ == "__main__":
#     app.run(debug=True)

import heapq
import random
import math
import time
import matplotlib.pyplot as plt
from flask import Flask, Blueprint, jsonify, request

# # Graph Data with traffic congestion for different times of the day
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



# Travel time based on traffic conditions (simplified)
def calculate_travel_time(start, end):
    edge_data = graph_data[start][end]
    traffic_factor = get_traffic_factor(start, end)
    travel_time = (edge_data["length"] / edge_data["speed"]) * traffic_factor
    return travel_time

def get_traffic_factor(start, end):
    # Return traffic factor based on time of day (simplified for now)
    return 1.0  # Placeholder for actual traffic congestion adjustment

# Optimisation class handling all algorithms
class Optimisation:
    def __init__(self, graph_data, coordinates):
        self.graph_data = graph_data
        self.coordinates = coordinates

    def calculate_total_time(self, route):
        """
        Calculate the total time taken by a route.
        Each segment of the route's travel time is calculated based on
        the length of the road, speed limit, and current traffic.
        """
        total_time = 0
        for i in range(len(route) - 1):
            total_time += calculate_travel_time(route[i], route[i + 1])
        return total_time

    def simulated_annealing(self, initial_route, initial_temp=100, cooling_rate=0.95, stopping_temp=0.01, max_iterations=1000):
        """
        Simulated Annealing algorithm to optimize the route by gradually lowering the temperature and accepting 
        worse solutions with a certain probability to escape local optima.
        """
        current_route = initial_route
        current_temp = initial_temp
        best_route = current_route
        best_cost = self.calculate_total_time(current_route)

        for iteration in range(max_iterations):
            new_route = self.swap_cities(current_route)
            current_cost = self.calculate_total_time(current_route)
            new_cost = self.calculate_total_time(new_route)

            # Accept new route based on temperature
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / current_temp):
                current_route = new_route
                current_cost = new_cost

            # Update best route
            if current_cost < best_cost:
                best_route = current_route
                best_cost = current_cost

            # Cool down temperature
            current_temp *= cooling_rate
            if current_temp < stopping_temp:
                break

        return best_route, best_cost

    def hill_climbing(self, initial_route, max_iterations=100):
        """
        Hill Climbing algorithm to optimize the route by iteratively improving it by moving to the neighboring route
        that has the lowest cost.
        """
        current_route = initial_route
        current_cost = self.calculate_total_time(current_route)

        best_route = current_route
        best_cost = current_cost

        for _ in range(max_iterations):
            new_route = self.swap_cities(current_route)
            new_cost = self.calculate_total_time(new_route)

            if new_cost < current_cost:
                current_route = new_route
                current_cost = new_cost

            if current_cost < best_cost:
                best_route = current_route
                best_cost = current_cost

        return best_route, best_cost

    def local_search(self, initial_route, max_iterations=100):
        """
        Local Search algorithm that iteratively improves the current route by checking neighbors.
        """
        current_route = initial_route
        current_cost = self.calculate_total_time(current_route)

        best_route = current_route
        best_cost = current_cost

        for _ in range(max_iterations):
            new_route = self.swap_cities(current_route)
            new_cost = self.calculate_total_time(new_route)

            if new_cost < current_cost:
                current_route = new_route
                current_cost = new_cost

            if current_cost < best_cost:
                best_route = current_route
                best_cost = current_cost

        return best_route, best_cost

    def csp(self, routes, max_iterations=100):
        """
        Constraint Satisfaction Problem (CSP) approach, potentially using backtracking or forward checking to ensure
        constraints like road capacity and delivery time windows are satisfied.
        """
        best_route = routes
        best_cost = sum(self.calculate_total_time(route) for route in routes)

        # Placeholder for CSP logic
        # Implement constraint satisfaction (e.g., backtracking, forward checking) here
        return best_route, best_cost

    def swap_cities(self, route):
        """
        Swap two cities in a route (excluding start and end cities).
        """
        new_route = route[:]
        i, j = random.sample(range(1, len(route) - 1), 2)  # Avoid swapping start/end
        new_route[i], new_route[j] = new_route[j], new_route[i]
        return new_route

# Flask Setup
optimisation = Blueprint('optimisation', __name__, url_prefix="/api/optimisation")

@optimisation.route('/optimize_route', methods=['POST'])
def optimize_route():
    """
    Route to trigger optimization algorithm.
    The client provides the initial route in the body of the request.
    """
    data = request.get_json()
    initial_route = data.get('route', ["Bishan", "Seletar", "Punggol", "Ang Mo Kio", "Potong Pasir", "Serangoon"])

    optimizer = Optimisation(graph_data, coordinates)  # Initialize Optimisation class
    # Run all optimization algorithms and compare results
    simulated_route, simulated_cost = optimizer.simulated_annealing(initial_route)
    hill_climbing_route, hill_climbing_cost = optimizer.hill_climbing(initial_route)
    local_search_route, local_search_cost = optimizer.local_search(initial_route)

    # Return all optimized results for comparison
    return jsonify({
        "simulated_annealing": {"route": simulated_route, "cost": simulated_cost},
        "hill_climbing": {"route": hill_climbing_route, "cost": hill_climbing_cost},
        "local_search": {"route": local_search_route, "cost": local_search_cost}
    })

# Initialize Flask App
app = Flask(__name__)
app.register_blueprint(optimisation)

if __name__ == "__main__":
    app.run(debug=True)
