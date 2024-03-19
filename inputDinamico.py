import pulp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define the LP variables and problem as you did before
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)
problem = pulp.LpProblem("Un semplice problema di max", pulp.LpMaximize)

excel_file_path = 'model.xlsx'

df = pd.read_excel(excel_file_path)

obj_func = df.columns.tolist()
obj_func.pop()

constraints = df.values.tolist()

problem += obj_func[0] * x + obj_func[1] * y, "The objective function"

for j in range(len(constraints)):
    constraint_name = f"Constraint_{j+1}"
    problem += constraints[j][0] * x + constraints[j][1] * y <= constraints[j][2], constraint_name

# Solve the problem
problem.solve()

# Print the results
print("Optimal values:")
for variable in problem.variables():
    print(f"{variable.name} = {variable.varValue}")
print("Maximum net profit:")
print(pulp.value(problem.objective))

# Plot the feasible region
x_values = np.linspace(0, 100, 100)
y_values = [(j[2] - j[0] * x_values) / j[1] for j in constraints]

for j in y_values:
    plt.plot(x_values, j, label=f"n")

# Highlight the feasible region
plt.fill_between(x_values, np.minimum.reduce([x for x in y_values]),
                 color='gray', alpha=0.5, label='Feasible Region')

# Highlight the optimal solution
plt.scatter([pulp.value(x)], [pulp.value(y)], color='red',
            label='Optimal Solution')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Feasible Region and Optimal Solution")
plt.legend()
plt.grid(True)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()