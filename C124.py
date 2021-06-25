from logging import error
from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'Name': 'e',
        'Contact': '6474169050',
        'done': False
    },
    {
        'id': 2,
        'Name': 'a',
        'Contact': '91234567',
        'done': False
    },
]
@app.route("/")

def ae():
    return "hello viewer"

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
            return jsonify({
                'status': 'error',
                'message': 'Please provide data.'
            })

    task = {
        'id': tasks[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ''),
        'done': False,
    }

    tasks.append(task)
    return jsonify({
            'status': 'success',
            'message': 'Task added successfully!'
        })

@app.route("/get-data")
def get_tasks():
    return jsonify({
        'data': tasks,
    })

if (__name__ == "__main__"):
    app.run(debug = True)