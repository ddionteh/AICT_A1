from logic import *

# Define facts
facts = [
    Symbol("Speed_V001_70"),  # Speed(V001) = 70
    Symbol("Location_V001_Bishan_Seletar"),  # Location(V001) = Bishan-Seletar
    Symbol("Speed_Limit_Bishan_Seletar_60"),  # Speed_Limit(Bishan-Seletar) = 60
    Symbol("Signal_Status_Bishan_Seletar_Red"),  # Signal_Status(Bishan-Seletar) = Red
    Symbol("At_Intersection_V001_TRUE")  # At_Intersection(V001) = TRUE
]

# Define rules
rules = [
    # Speeding rule: If Speed(V001) > Speed_Limit(Bishan-Seletar), then Speeding(V001)
    Implication(
        And(
            Symbol("Speed_V001_70"),
            Symbol("Speed_Limit_Bishan_Seletar_60")
        ),
        Symbol("Speeding_V001")
    ),
    # Red light violation rule: If At_Intersection(V001) = TRUE, Signal_Status(Bishan-Seletar) = Red, and Speed(V001) != 0, then Red_Light_Violation(V001)
    Implication(
        And(
            Symbol("At_Intersection_V001_TRUE"),
            Symbol("Signal_Status_Bishan_Seletar_Red"),
            Symbol("Speed_V001_70")  # Speed(V001) = 70 (which is != 0)
        ),
        Symbol("Red_Light_Violation_V001")
    )
]

kb = And(*facts, *rules)
print(kb.formula())

# Query for speeding violations
speeding_query = Symbol("Speeding_V001")
if model_check(kb, speeding_query):
    print("Vehicle V001 is speeding!")
else:
    print("Vehicle V001 is not speeding.")

# Query for red light violations
red_light_query = Symbol("Red_Light_Violation_V001")
if model_check(kb, red_light_query):
    print("Vehicle V001 has a red light violation!")
else:
    print("Vehicle V001 has no red light violation.")

''' 
This is inference by resolution for 1 set of data only. 

The speeding rule implication checks whether Symbol("Speed_V001_70"), and Symbol("Speed_Limit_Bishan_Seletar_60")
are in facts (which is what ) and if so, it implies Symbol("Speeding_V001"); adding it to the knowledge base. 
- A shortcoming is that if the speed is not equal to 70 but is still greater than 60, the rule will not be triggered.
(Speed_V001_70) ∧ (Speed_Limit_Bishan_Seletar_60)) => (Speeding_V001)

The red light violation rule implication checks whether Symbol("At_Intersection_V001_TRUE"), Symbol("Signal_Status_Bishan_Seletar_Red"), and Symbol("Speed_V001_70") are in facts 
and if so, it implies Symbol("Red_Light_Violation_V001"); adding it to the knowledge base.
(At_Intersection_V001_TRUE) ∧ (Signal_Status_Bishan_Seletar_Red) ∧ (Speed_V001_70)) => (Red_Light_Violation_V001)

The knowledge base is then checked for speeding and red light violations.
'''