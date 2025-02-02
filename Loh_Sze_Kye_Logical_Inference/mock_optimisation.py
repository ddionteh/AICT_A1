# Define weights for different rules
weights = {
    'ran_red_light': 10,
    'made_illegal_turn': 5
}

# Define cost function
def cost_function(violations):
    return sum(weights[violation] for violation in violations)

# Example traffic data
traffic_data = [
    {'Vehicle_ID': 1, 'Ran_Red_Light': True, 'Direction': 'left', 'Allowed_Turns': ['right'], 'At_Intersection': 'TRUE'},
    {'Vehicle_ID': 2, 'Ran_Red_Light': False, 'Direction': 'right', 'Allowed_Turns': ['right'], 'At_Intersection': 'TRUE'},
    {'Vehicle_ID': 3, 'Ran_Red_Light': True, 'Direction': 'straight', 'Allowed_Turns': ['left'], 'At_Intersection': 'TRUE'}
]

# Check for traffic violations and calculate cost
traffic_violations = []
for row in traffic_data:
    violations = []
    
    # Check red light violation
    if row.get('Ran_Red_Light', False):
        violations.append('ran_red_light')
    
    # Check illegal turn violation
    allowed_turns = row.get('Allowed_Turns', [])
    direction = row.get('Direction', '')
    at_intersection = row.get('At_Intersection', 'FALSE') == 'TRUE'
    
    if direction not in allowed_turns and at_intersection:
        violations.append('made_illegal_turn')
    
    if violations:
        traffic_violations.append({
            'Vehicle_ID': row['Vehicle_ID'],
            'Violations': violations,
            'Cost': cost_function(violations)
        })

# Optimization: Sort violations by descending cost
traffic_violations.sort(key=lambda x: x['Cost'], reverse=True)

print("Optimized Traffic Violations (Prioritized by Severity):")
for v in traffic_violations:
    print(f"Vehicle {v['Vehicle_ID']} -> Violations: {v['Violations']}, Cost: {v['Cost']}")