from flask import Flask, jsonify,request
from evaluation import results
import json


app = Flask(__name__)



def note_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': notes[key]
    }

@app.route("/get_data", methods=['POST'])
def get_data():
    data = request.get_json()
    marks=(data['marks'])
    model_ans=data['model_ans']
    user_ans=data['user_ans']
    return results(marks,model_ans,user_ans)

@app.route('/', methods=['GET'])
def main():
    return 'running'

if __name__ == "__main__":
    app.run(debug=True)