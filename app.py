from flask import Flask, render_template, request, jsonify
import pulp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve_problem', methods=["POST"])
def solve_problem():
    data = request.json[2::]
    print(data)  # Print the received data for debugging purposes

    # Process the data and perform the algorithm (you need to implement this part)
    def solve(param):
        # Extract data for objective function and constraints
        data1 = [float(i['value']) for i in param[:2]]
        data2 = [list(map(float, [item['value'] for item in param[i:i + 3]])) for i in range(2, len(param), 3)]

        # Combine data for objective function and constraints
        all_data = [data1] + data2

        # Define decision variables and LP problem
        x = pulp.LpVariable("x", lowBound=0)
        y = pulp.LpVariable("y", lowBound=0)
        problem = pulp.LpProblem("A Simple Maximize Problem", pulp.LpMaximize)

        # Set up objective function
        problem += data1[0] * x + data1[1] * y, "The objective function"

        # Add constraints
        for i, constraint_data in enumerate(data2, start=1):
            constraint_name = f"Constraint_{i}"
            problem += constraint_data[0] * x + constraint_data[1] * y <= constraint_data[2], constraint_name

        # Solve the problem
        problem.solve()

        # Print the results
        """print("Optimal values:")
        for variable in problem.variables():
            print(f"{variable.name} = {variable.varValue}")
        print("Maximum net profit:")
        print(pulp.value(problem.objective))"""

        return pulp.value(problem.objective)

    res = solve(data)
    print(res)
    # For now, just returning the received data as a response
    return jsonify({"result": res})

if __name__ == '__main__':
    app.run(debug=True)
