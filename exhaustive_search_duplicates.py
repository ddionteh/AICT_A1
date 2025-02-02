# an exhaustive search algorithm to find duplicates in the data.
#does not actually use any inference rules to resolve the inconsistencies.
from logic import * 
import csv

# read the data from traffic_information.csv
def read_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))
    return data

# create a list of dictionaries from the data
# example: {'Vehicle_ID': 'V001', 'Location': 'Bishan - Seletar', 'Speed': '50', 'Timestamp': '2025-01-26 08:00:00', 'At_Intersection': 'FALSE'}
def create_dict(data):
    keys = data[0]
    data_dict = []
    for i in range(1, len(data)):
        data_dict.append(dict(zip(keys, data[i])))
    return data_dict

traffic_info = read_data('./data/traffic_information.csv')
traffic_info_dict = create_dict(traffic_info)

# define the predicates
def Vehicle_ID(x):
    return Symbol(f"{x['Vehicle_ID']}")

def Location(x):
    return Symbol(f"{x['Location']}")

def Speed(x):
    return Symbol(f"{x['Speed']}")

def Timestamp(x):
    return Symbol(f"{x['Timestamp']}")

def At_Intersection(x):
    return Symbol(f"{x['At_Intersection']}")

def repeat_check_symbolic(row):
    return And(
        Vehicle_ID(row),
        Location(row),
        Timestamp(row),
    )

# define the rules

# Rule: If the vehicle is in 2 locations at the same timestamp, then there are inconsistencies in the data.
def find_repeated_rows(data_dict):
    n = len(data_dict)
    
    for i in range(n):
        sentry = False
        for j in range(i + 1, n):
            # Convert rows to symbolic representations
            row_i_symbolic = repeat_check_symbolic(data_dict[i])
            row_j_symbolic = repeat_check_symbolic(data_dict[j])
            # Check if the symbolic representations are equivalent
            if row_i_symbolic == row_j_symbolic:
                # Store the indices and values of the duplicate rows
                duplicates.append(((i+1, j+2), (data_dict[i], data_dict[j])))
                sentry = True
        if not sentry:
            consistent.append(data_dict[i])

duplicates = []
consistent = []
find_repeated_rows(traffic_info_dict)

if duplicates:
    print("Repeated rows found:", len(duplicates))
    for indices, values in duplicates:
        print(f"Rows {indices[0]} and {indices[1]} are duplicates:")
        print(f"Row {indices[0]}: {values[0]}")
        print(f"Row {indices[1]}: {values[1]}")
else:
    print("No repeated rows found.")

# export the consistent data to a new csv file
def export_to_csv(data, file_name):
    keys = data[0].keys()
    with open(file_name, 'w',newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    
export_to_csv(consistent, './data/consistent_traffic_info.csv')


# Might work if data is smaller and there is only 1 inconsistency
# def rule3(x, y):  
#     inconsistent = Symbol('inconsistent')
#     return Implication (Not(inconsistent), 
#         Not(
#             And(
#                 And(Location(x), Location(y)), 
#                 And(Timestamp(x) , Timestamp(y)), 
#                 And(Vehicle_ID(x), Vehicle_ID(y))
#             )
#         )
#         )
    

# n = len(traffic_info_dict)
# duplicates = []
# for i in range(n):
#     for j in range(i + 1, n):
#         test = rule3(traffic_info_dict[i], traffic_info_dict[j])
#         print(test)

# inconsistent = Symbol('inconsistent')
# print(model_check(kb, inconsistent))

# Another similar attempt to the one above
# # Function to convert a row into a symbolic representation
# def unique_row(x, y):
#     return Not(And(
#         And(Location(x) , Location(y)),
#         And(Timestamp(x) , Timestamp(y)),
#         And(Vehicle_ID(x) , Vehicle_ID(y))
#     ))

# #
# # Add constraints to the KB to ensure no two rows are identical
# for i in range(len(traffic_info_dict)):
#     for j in range(i + 1, len(traffic_info_dict)):
#         kb.add(unique_row(traffic_info_dict[i], traffic_info_dict[j]))

# # Query the KB to check for duplicates
# duplicates = []
# for i in range(len(traffic_info_dict)):
#     for j in range(i + 1, len(traffic_info_dict)):
#         if not model_check(kb, unique_row(traffic_info_dict[i], traffic_info_dict[j])):
#             duplicates.append(((i, j), (traffic_info_dict[i], traffic_info_dict[j])))