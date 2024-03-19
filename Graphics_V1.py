import pulp
import numpy as np
import matplotlib.pyplot as plt

# Define the LP variables and problem as you did before
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)
problem = pulp.LpProblem("Un semplice problema di max", pulp.LpMaximize)

# Add objective function and constraints
problem += 20 * x + 12.5 * y, "The objective function"
problem += 0.72 * x + 0.23 * y <= 13, "1st constraint"
problem += 2 * x + 0.2 * y <= 31, "2nd constraint"
problem += 12 * x + 3 * y <= 230, "3rd constraint"
problem += 0.33 * x + 0.28 * y <= 10, "4th constraint"

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
y_values_1 = (13 - 0.72 * x_values) / 0.23
y_values_2 = (31 - 2 * x_values) / 0.2
y_values_3 = (230 - 12 * x_values) / 3
y_values_4 = (10 - 0.33 * x_values) / 0.28

plt.plot(x_values, y_values_1, label="0.72x + 0.23y <= 13")
plt.plot(x_values, y_values_2, label="2x + 0.2y <= 31")
plt.plot(x_values, y_values_3, label="12x + 3y <= 230")
plt.plot(x_values, y_values_4, label="0.33x + 0.28y <= 10")

# Highlight the feasible region
plt.fill_between(x_values, np.minimum.reduce([y_values_1, y_values_2, y_values_3, y_values_4]), color='gray', alpha=0.5, label='Feasible Region')

# Highlight the optimal solution
plt.scatter([pulp.value(x)], [pulp.value(y)], color='red', label='Optimal Solution')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Feasible Region and Optimal Solution")
plt.legend()
plt.grid(True)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()
