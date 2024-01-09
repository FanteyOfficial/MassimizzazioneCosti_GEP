from flask import Flask, render_template

app = Flask(__name__)

table_data = [
    {'Name': 'John', 'Age': 25, 'Country': 'USA'},
    {'Name': 'Alice', 'Age': 30, 'Country': 'Canada'},
    {'Name': 'Bob', 'Age': 22, 'Country': 'UK'},
]

@app.route('/')
def index():
    return render_template('index.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)