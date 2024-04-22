from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos
    if not todos:
        return "No todo items to delete", 404
    
    try:
        deleted_todo = todos.pop(position)
        return jsonify(todos)
    except IndexError:
        return "Index out of range", 404
        
    


todos = [
    { "label": "My first task", "done": False },
]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)