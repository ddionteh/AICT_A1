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

traffic_light_info = read_csv(
    './data/traffic_light.csv'
)

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

kb = And()
def inconsistent_data(x, y):
    return x['Vehicle_ID'] == y['Vehicle_ID'] and x['Timestamp'] == y['Timestamp'] and x['Location'] != y['Location']

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


# Add inconsistency rules
for i in range(len(traffic_info)):
    for j in range(i + 1, len(traffic_info)):
        if inconsistent_data(traffic_info[i], traffic_info[j]):
            inconsistency_rule(traffic_info[i], traffic_info[j])



# Check for inconsistent data
inconsistent = Symbol('Inconsistent_Data')
if model_check(kb, inconsistent):
    print("Inconsistent data found!")
else:
    print("No inconsistent data found.")