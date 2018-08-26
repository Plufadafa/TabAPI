from flask import Flask, jsonify
from flaskext.mysql import MySQL


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route("/")
def hello():
    return "Hello World!    f"



@app.route("/tasks", methods=['GET'] )
def get_tasks():
    return jsonify({'tasks': tasks})

