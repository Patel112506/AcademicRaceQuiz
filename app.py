from flask import Flask, render_template, jsonify
from questions import get_random_question

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/question')
def get_question():
    question = get_random_question()
    return jsonify(question)
