import pulp

data = [
    {'name': 'coefficient', 'value': '20'}, {'name': 'variable', 'value': '12.5'},
    {'name': 'coefficient', 'value': '0.72'}, {'name': 'variable', 'value': '0.23'}, {'name': 'operator', 'value': '13'},
    {'name': 'coefficient', 'value': '2'}, {'name': 'variable', 'value': '0.2'}, {'name': 'operator', 'value': '31'},
    {'name': 'coefficient', 'value': '12'}, {'name': 'variable', 'value': '3'}, {'name': 'operator', 'value': '230'},
    {'name': 'coefficient', 'value': '0.33'}, {'name': 'variable', 'value': '0.28'}, {'name': 'operator', 'value': '10'}
]

# Extract data for objective function and constraints
data1 = [float(i['value']) for i in data[:2]]
data2 = [list(map(float, [item['value'] for item in data[i:i+3]])) for i in range(2, len(data), 3)]

# Combine data for objective function and constraints
all_data = [data1] + data2

# Define decision variables and LP problem
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)
problem = pulp.LpProblem("A Simple Maximize Problem", pulp.LpMaximize)

# Set up objective function
problem += data1[0]*x + data1[1]*y, "The objective function"

# Add constraints
for i, constraint_data in enumerate(data2, start=1):
    constraint_name = f"Constraint_{i}"
    problem += constraint_data[0]*x + constraint_data[1]*y <= constraint_data[2], constraint_name

# Solve the problem
problem.solve()

# Print the results
print("Optimal values:")
for variable in problem.variables():
    print(f"{variable.name} = {variable.varValue}")
print("Maximum net profit:")
print(pulp.value(problem.objective))
