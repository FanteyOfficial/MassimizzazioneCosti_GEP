import pulp
#from pulp import *
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)
problem = pulp.LpProblem("Un semplice problema di max", pulp.LpMaximize)

problem += 20*x + 12.5*y, "The objective function"
problem += 0.72*x + 0.23*y <= 13, "1st constraint"
problem += 2*x + 0.2*y <= 31, "2nd constraint"
problem += 12*x + 3*y <= 230, "3rd constraint"
problem += 0.33*x + 0.28*y <= 10, "4th constraint"
problem.solve()

print("Risultati della ottimizzazione:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Massimo profitto netto totale:")
print(pulp.value(problem.objective))