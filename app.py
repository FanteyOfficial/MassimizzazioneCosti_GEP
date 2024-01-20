from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

"""def index():
    return render_template('index.html', table_data=table_data)
"""


@app.route('/solve_problem', methods=["POST"])
def solve_problem():
    data = request.json
    print(jsonify(data))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
