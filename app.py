from flask import Flask,jsonify,render_template
import json

app = Flask(__name__)

@app.route('/api')
def get_data():
    
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            
        return jsonify(data)
    except Exception as e:
        return e
@app.route('/todo')
def todo_page():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)