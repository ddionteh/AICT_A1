from logic import *
#  Define symbols
L = Symbol("LegallyParked")
I = Symbol("InDesignatedParking")
P = Symbol("PaidFee")

# Create biconditional: L ⇔ (I ∧ P)
biconditional = Biconditional(L, And(I, P))

# Build knowledge base
knowledge = And(biconditional)
knowledge.add(I)
knowledge.add(P)

# Query: "Is the vehicle legally parked?"
query = L

# Check if the knowledge entails the query
result = model_check(knowledge, query)
print(result)  # Output: False (depends on model constraints)