from logic import *
import csv
from z3 import Bool, Optimize, Not, sat

def read_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Read and standardize the data
traffic_info = read_csv('./data/traffic_information.csv')
traffic_light_info = read_csv('./data/traffic_light.csv')
speed_limit_info = read_csv('./data/speed_limit.csv')

# Combine traffic light information with traffic info with speed limit info
for row in traffic_info:
    location = row['Location']
    timestamp = row['Timestamp']
    speed_limit = next((sl['Speed_Limit'] for sl in speed_limit_info if sl['Location'] == location), None)
    row['Speed_Limit'] = speed_limit
    traffic_light = next((tl['Signal_Status'] for tl in traffic_light_info if tl['Location'] == location and tl['Timestamp'] == timestamp), None)
    row['Signal_Status'] = traffic_light

# check for inconsistency first
# Define predicates
def Vehicle_ID(x):
    return Symbol(f"Vehicle_ID_{x['Vehicle_ID']}")

def Location(x):
    return Symbol(f"Location_{x['Location']}")

def Speed(x):
    return Symbol(f"Speed_{x['Speed']}")

def Timestamp(x):
    return Symbol(f"Timestamp_{x['Timestamp']}")

def At_Intersection(x):
    return Symbol(f"At_Intersection_{x['At_Intersection']}")

def row_to_symbolic(x):
    return And(Vehicle_ID(x),Location(x), Timestamp(x))

kb = And()
def inconsistent_data(x, y):
    return x['Vehicle_ID'] == y['Vehicle_ID'] and x['Timestamp'] == y['Timestamp'] and x['Location'] != y['Location']

# If the vehicle is in 2 locations at the same timestamp, then there are inconsistencies in the data.
def inconsistency_rule(x, y):
    kb.add(
        And( 
        Implication(
            And(Vehicle_ID(x), Vehicle_ID(y), Timestamp(x), Timestamp(y), Location(x), Location(y)),
            Symbol('Inconsistent_Data')
        ),
        Vehicle_ID(x), Vehicle_ID(y), Timestamp(x), Timestamp(y), Location(x), Location(y)
        )
    )

keep_first_of_inconsistent = []
make_consistent = []
# Add inconsistency rules
for i in range(len(traffic_info)):
    if i != 0 and model_check(kb, row_to_symbolic(traffic_info[i])): # if the row is already inconsistent, skip
        continue
    for j in range(i + 1, len(traffic_info)):
        if inconsistent_data(traffic_info[i], traffic_info[j]):
            inconsistency_rule(traffic_info[i], traffic_info[j])
            keep_first_of_inconsistent.append(traffic_info[j]) #keeps the first of the inconsistent data
    


# Check for inconsistent data
inconsistent = Symbol('Inconsistent_Data')
if model_check(kb, inconsistent):
    print("Inconsistent data found!")
else:
    print("No inconsistent data found.")

print("Removing inconsistent data...")
for row in traffic_info:
    if not model_check(kb, row_to_symbolic(row)) or row not in keep_first_of_inconsistent:
        make_consistent.append(row)

def export_to_csv(data, file_name):
    keys = data[0].keys()
    with open(file_name, 'w',newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

export_to_csv(make_consistent, './data/consistent_traffic_info.csv')

###############################################################################

consistent_traffic_info = read_csv("./data/consistent_traffic_info.csv")
kb = And()
# implication rule that checks whether a vehicle has committed any traffic violations
def traffic_violation(x):
    violation = Symbol(f"Traffic_Violation_{x['Vehicle_ID']}")
    s = Symbol(f"Speeding_{x['Vehicle_ID']}")
    r = Symbol(f"Ran_Red_Light_{x['Vehicle_ID']}")
    i = Symbol(f"Made_Illegal_Turn_{x['Vehicle_ID']}")
    kb.add(
        And(
            Implication(Not(violation), Not(Or(s, r, i))), # if there are no violations, vehicle is not speeding. If vehicle is not not speeding, then it is a violation. 
            is_speeding(x),
            ran_red_light(x),
            made_illegal_turn(x),
            )
    )

# implication rule that checks whether a vehicle is speeding
def is_speeding(x):
    speed_check = int(x['Speed']) > int(x['Speed_Limit'])
    speeding = Symbol(f"Speeding_{x['Vehicle_ID']}")
    if speed_check:
        return speeding
    else:
        return Not(speeding)
    
# implication rule that checks whether a vehicle ran a red light
def ran_red_light(x):
    ran_red = x['Signal_Status'] == 'Red'
    At_Intersection = x['At_Intersection'] == 'TRUE'
    ran_red_light = Symbol(f"Ran_Red_Light_{x['Vehicle_ID']}")
    if ran_red and At_Intersection:
        return ran_red_light
    else:
        return Not(ran_red_light)
    
# implication rule that checks whether a vehicle made an illegal turn
def made_illegal_turn(x):
    illegal_turn = x['Direction']
    legal_turn = x['Allowed_Turns']
    At_Intersection = x['At_Intersection'] == 'TRUE'
    made_illegal_turn = Symbol(f"Made_Illegal_Turn_{x['Vehicle_ID']}")
    if illegal_turn not in legal_turn and At_Intersection:
        return made_illegal_turn
    else:
        return Not(made_illegal_turn)

# Check for traffic violations
traffic_violations = []
print("Checking for traffic violations...")
for row in consistent_traffic_info:
    kb = And() #Must keep re-initialising the knowledge base otherwise the rules will keep stacking and become computationally expensive
    traffic_violation(row)
    print(f"Checking for traffic violations for Vehicle {row['Vehicle_ID']}...")
    query = Symbol(f"Traffic_Violation_{row['Vehicle_ID']}")
    result = model_check(kb, query)
    if result:
        traffic_violations.append(row['Vehicle_ID'])

print("Traffic violations:", traffic_violations) #Traffic violations: ['V002', 'V004', 'V006', 'V008', 'V011', 'V016', 'V018', 'V019', 'V004', 'V005', 'V006', 'V009']