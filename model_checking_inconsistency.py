import csv
from logic import *
from datetime import datetime

def parse_timestamp(timestamp_str, format):
    """Parse a timestamp string into a datetime object using the specified format."""
    return datetime.strptime(timestamp_str, format)

def standardize_timestamp(timestamp_str, input_format, output_format):
    """Convert a timestamp string from one format to another."""
    dt = parse_timestamp(timestamp_str, input_format)
    return dt.strftime(output_format)

def read_csv(file_name, timestamp_column=None, input_format=None, output_format=None):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if timestamp_column and input_format and output_format:
                # Standardize the timestamp if the column and formats are provided
                row[timestamp_column] = standardize_timestamp(
                    row[timestamp_column], input_format, output_format
                )
            data.append(row)
    return data

# Read traffic information and traffic light data
# Define the timestamp formats
traffic_info_format = "%Y-%m-%d %H:%M:%S"  # Input format for traffic_info
traffic_light_format = "%d/%m/%Y %H:%M"    # Input format for traffic_light_info
output_format = "%Y-%m-%d %H:%M:%S"        # Standardized output format

# Read and standardize the data
traffic_info = read_csv(
    './data/traffic_information.csv',
    timestamp_column='Timestamp',
    input_format=traffic_info_format,
    output_format=output_format
)

traffic_light_info = read_csv(
    './data/traffic_light.csv',
    timestamp_column='Timestamp',
    input_format=traffic_light_format,
    output_format=output_format
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