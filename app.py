from flask import Flask, jsonify, request

#Creating an app using flask constructor
app = Flask(__name__)

#Creating a list of contacts
tasks = [
    {
        "id": 1,
        "name": u"Raju",
        "contact": u"9987644456",
        "done": False
    },
    {
        "id": 2,
        "name": u"Rahul",
        "contact": u"9876543222",
        "done": False
    }
]

#Creating an add-data route using POST method
@app.route("/add-data", methods=["POST"])

#Creating an add-task function
def add_task():

    #Writing a condition to return a message if the request is unsuccessful
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data."
        }, 400)

    task = {
        "id": tasks[-1]["id"]+1,
        "name": request.json["name"],
        "contact": request.json.get("contact", ""),
        "done": False
    }

    tasks.append(task)

    #returing a json object with status successful and message saying task added successfully.
    return jsonify({
        "status": "success",
        "message": "Task added successfully."
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        "data": tasks
    })

if (__name__ == "__main__"):
    app.run(debug=True)