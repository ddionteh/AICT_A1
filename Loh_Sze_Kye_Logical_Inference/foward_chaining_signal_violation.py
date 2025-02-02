# uses forward chaining to detect traffic violations
# The algorithm iterates through the dataset, applies rules to individual rows, and updates the KB to draw conclusions.
import csv
from logic import *
from datetime import datetime

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

# Read and standardize the data
traffic_info = read_csv(
    './data/traffic_information.csv',
)

traffic_light_info = read_csv(
    './data/traffic_light.csv',
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

def Signal_Status(x):
    return Symbol(f"Signal_Status_{x['Signal_Status']}")

def row_to_symbolic(x):
    return And(Location(x), Timestamp(x))

# insert rules into knowledge base for red light violations
kb = And()
for row in traffic_light_info:
    if row['Signal_Status'] == 'Red':
        kb.add(row_to_symbolic(row))

# if location and timestamp are the same, and the signal status is red, and the vehicle is at the intersection, then the vehicle is running the red light
for row in traffic_info:
    if row['At_Intersection'] == "TRUE":
        if model_check(kb, row_to_symbolic(row)):
            print(f"Vehicle {row['Vehicle_ID']} is running the red light.")