import csv
from logic import *
from datetime import datetime

def read_csv(file_name, timestamp_column=None, input_format=None, output_format=None):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Read and standardize the data
traffic_info = read_csv(
    './data/traffic_information.csv'
)

speed_limit_info = read_csv('./data/speed_limit.csv')

# Combine traffic light information with traffic info
for row in traffic_info:
    location = row['Location']
    timestamp = row['Timestamp']
    speed_limit = next((sl['Speed_Limit'] for sl in speed_limit_info if sl['Location'] == location), None)
    row['Speed_Limit'] = speed_limit

def is_speeding(x):
    speed_check = int(x['Speed']) > int(x['Speed_Limit'])
    speeding = Symbol(f"Speeding")
    if speed_check:
        return speeding
    else:
        return Not(speeding)

def exceed_speed_limit(x):
    excess = int(x['Speed']) - int(x['Speed_Limit'])
    if excess < 20:
        return {'Vehicle_ID': x['Vehicle_ID'], 'Excess_Speed': excess, 'Demerit_Points': 4}
    elif excess < 30:
        return {'Vehicle_ID': x['Vehicle_ID'], 'Excess_Speed': excess, 'Demerit_Points': 6}
    elif excess < 40:
        return {'Vehicle_ID': x['Vehicle_ID'], 'Excess_Speed': excess, 'Demerit_Points': 8}
    elif excess < 50:
        return {'Vehicle_ID': x['Vehicle_ID'], 'Excess_Speed': excess, 'Demerit_Points': 12}
    elif excess < 60:
        return {'Vehicle_ID': x['Vehicle_ID'], 'Excess_Speed': excess, 'Demerit_Points': 18}
    else:
        return {'Vehicle_ID': x['Vehicle_ID'], 'Excess_Speed': excess, 'Demerit_Points': 24}

def speeding_rule(x):
    violation = Symbol(f"Speeding_{x['Vehicle_ID']}")
    s = Symbol(f"Speeding")
    t = Symbol(f"Not_Speeding")
    kb.add(
        And(
            Implication(Not(violation), t), # if there are no violations, vehicle is not speeding. If vehicle is not not speeding, then it is a violation. 
            Or(s, t), #vehicle is either speeding or not speeding
            Not(And(s, t)), #vehicle cannot be both speeding and not speeding
            is_speeding(x)
            )
    )

# Check for speeding violations
speeding_violations = []
for row in traffic_info:
    kb = And()
    speeding_rule(row)
    query = Symbol(f"Speeding_{row['Vehicle_ID']}")
    if model_check(kb, query):
        speeding_violations.append(exceed_speed_limit(row))

print("Speeding violations:", speeding_violations)

# export vehicles with speeding violations to a new csv file
with open('./data/speeding_violations.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=speeding_violations[0].keys())
    writer.writeheader()
    writer.writerows(speeding_violations)



'''Check for speeding violations
this method is too computationally expensive
Why It Gets Stuck
Exponential Complexity:

The model_check function evaluates all possible combinations of truth assignments for the symbols in the knowledge base.

If the knowledge base contains many symbols (e.g., Vehicle_ID, Location, Speed, Timestamp, etc.), the number of combinations grows exponentially, making the function very slow.

Large Knowledge Base:

If the knowledge base (kb) contains many rules (e.g., one for each row in traffic_info), the evaluation process becomes even slower.

Inefficient Queries:

Each call to model_check re-evaluates the entire knowledge base, which is redundant and inefficient.
for row in traffic_info:
    print(row)
    print(query)
    query = Symbol(f"Speeding_{row['Vehicle_ID']}")
    if model_check(kb, query):
        print(model_check(kb, query))
        speeding_violations.append(row['Vehicle_ID'])
    else:
        continue
def speeding_rule(x): # part of the computationally expensive method; coded at 2359 idk what's going on
    return Implication(
        And(Vehicle_ID(x), Location(x), Speed(x), Timestamp(x)),
        Symbol(f"Speeding_{x['Vehicle_ID']}")
    )'''
