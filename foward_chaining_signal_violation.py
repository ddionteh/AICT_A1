# uses forward chaining to detect traffic violations
# The algorithm iterates through the dataset, applies rules to individual rows, and updates the KB to draw conclusions.
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