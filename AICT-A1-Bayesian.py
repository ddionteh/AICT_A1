from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import random
import math

# ------------------------- Define Bayesian Network Structure -------------------------
model = BayesianNetwork([
    ('W', 'C'),  # Weather → Congestion
    ('W', 'A'),  # Weather → Accidents
    ('T', 'C'),  # Time of Day → Congestion
    ('R', 'S'),  # Road Type → Speed Limit
    ('R', 'A'),  # Road Type → Accidents
    ('C', 'TT'), # Congestion → Travel Time
    ('A', 'TT'), # Accidents → Travel Time
    ('S', 'TT'), # Speed Limit → Travel Time
    ('H', 'C'),  # Historical Congestion → Current Congestion
    ('H', 'A'),  # Historical Congestion → Accidents
])

# CPD for Weather (W)
cpd_W = TabularCPD(variable='W', variable_card=4,
                   values=[[0.5], [0.3], [0.15], [0.05]],  # Sunny, Rainy, Foggy, Stormy
                   state_names={'W': ['Sunny', 'Rainy', 'Foggy', 'Stormy']})

# CPD for Time of Day (T)
cpd_T = TabularCPD(variable='T', variable_card=3,
                   values=[[0.3], [0.4], [0.3]],  # Morning, Afternoon, Evening
                   state_names={'T': ['Morning', 'Afternoon', 'Evening']})

# CPD for Road Type (R)
cpd_R = TabularCPD(variable='R', variable_card=3,
                   values=[[0.4], [0.4], [0.2]],  # Highway, Main Road, Residential
                   state_names={'R': ['Highway', 'Main Road', 'Residential']})

# CPD for Speed Limit (S | R)
cpd_S = TabularCPD(variable='S', variable_card=4,
                   values=[[0.8, 0.4, 0.1],  # 80 km/h for Highway, etc.
                           [0.2, 0.4, 0.3],  # 70 km/h
                           [0.0, 0.2, 0.4],  # 60 km/h
                           [0.0, 0.0, 0.2]],  # 50 km/h
                   evidence=['R'], evidence_card=[3],
                   state_names={'S': ['80 km/h', '70 km/h', '60 km/h', '50 km/h'],
                                'R': ['Highway', 'Main Road', 'Residential']})

# CPD for Historical Congestion (H)
cpd_H = TabularCPD(variable='H', variable_card=3,
                   values=[[0.5], [0.3], [0.2]],  # Low, Medium, High
                   state_names={'H': ['Low', 'Medium', 'High']})

# CPD for Congestion (C | W, T, H)
cpd_C = TabularCPD(variable='C', variable_card=3,
                   values=[[0.5] * 36, [0.3] * 36, [0.2] * 36],
                   evidence=['W', 'T', 'H'], evidence_card=[4, 3, 3],
                   state_names={'C': ['Low', 'Medium', 'High'],
                                'W': ['Sunny', 'Rainy', 'Foggy', 'Stormy'],
                                'T': ['Morning', 'Afternoon', 'Evening'],
                                'H': ['Low', 'Medium', 'High']})

# CPD for Accidents (A | W, R, H)
cpd_A = TabularCPD(variable='A', variable_card=3,
                   values=[[0.7] * 36, [0.2] * 36, [0.1] * 36],
                   evidence=['W', 'R', 'H'], evidence_card=[4, 3, 3],
                   state_names={'A': ['No Accident', 'Minor Accident', 'Major Accident'],
                                'W': ['Sunny', 'Rainy', 'Foggy', 'Stormy'],
                                'R': ['Highway', 'Main Road', 'Residential'],
                                'H': ['Low', 'Medium', 'High']})

# CPD for Travel Time (TT | C, A, S)
cpd_TT = TabularCPD(variable='TT', variable_card=3,
                    values=[[0.5] * 36, [0.3] * 36, [0.2] * 36],
                    evidence=['C', 'A', 'S'], evidence_card=[3, 3, 4],
                    state_names={'TT': ['Short', 'Medium', 'Long'],
                                 'C': ['Low', 'Medium', 'High'],
                                 'A': ['No Accident', 'Minor Accident', 'Major Accident'],
                                 'S': ['80 km/h', '70 km/h', '60 km/h', '50 km/h']})

# Add CPDs to the model
model.add_cpds(cpd_W, cpd_T, cpd_R, cpd_S, cpd_H, cpd_C, cpd_A, cpd_TT)

# Verify model validity
assert model.check_model()

print("Bayesian Network successfully built! No errors.")

# ------------------------- Bayesian Inference Functions -------------------------
inference = VariableElimination(model)

def predict_traffic(weather, time_of_day, history):
    """
    Predict congestion level based on real-time inputs.
    """
    query_result = inference.query(variables=['C'], evidence={'W': weather, 'T': time_of_day, 'H': history})
    
    congestion_levels = {'Low': 1.0, 'Medium': 1.5, 'High': 2.0}
    predicted_c = query_result.values
    expected_congestion = sum(predicted_c[i] * congestion_levels[state] for i, state in enumerate(['Low', 'Medium', 'High']))
    
    print(f"Predicted Congestion Factor: {expected_congestion:.2f}")
    return expected_congestion  # 1.0 = Normal, >1.0 = Delays

# ------------------------- Traffic Flow Optimization -------------------------
fleet = [('A', 'E'), ('B', 'D'), ('C', 'F')]

def total_travel_time(assignments, weather, time_of_day, history):
    total_time = 0
    congestion_factor = predict_traffic(weather, time_of_day, history)
    
    for i, (start, end) in enumerate(fleet):
        base_time = random.uniform(10, 30)  # Simulated base travel time
        adjusted_time = base_time * congestion_factor
        total_time += adjusted_time
    
    return total_time

def simulated_annealing(initial_solution, weather, time_of_day, history, temp=10000, cooling_rate=0.995):
    current_solution = initial_solution
    best_solution = current_solution
    best_cost = total_travel_time(current_solution, weather, time_of_day, history)

    while temp > 1:
        new_solution = list(current_solution)
        i = random.randint(0, len(fleet) - 1)
        new_solution[i] = (random.choice(['A', 'B', 'C', 'D', 'E', 'F']), random.choice(['A', 'B', 'C', 'D', 'E', 'F']))

        new_cost = total_travel_time(new_solution, weather, time_of_day, history)

        if new_cost < best_cost or math.exp((best_cost - new_cost) / temp) > random.random():
            best_solution, best_cost = new_solution, new_cost

        temp *= cooling_rate

    return best_solution, best_cost

# Run Optimization
optimized_routes, optimized_time = simulated_annealing(fleet, 'Rainy', 'Morning', 'High')

print(f"Optimized Fleet Routes: {optimized_routes} with total travel time {optimized_time:.2f} mins")
