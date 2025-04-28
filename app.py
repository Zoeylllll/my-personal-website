from flask import Flask, request, render_template, redirect
import json
import os

app = Flask(__name__)

DATA_FILE = 'messages.json'

def load_messages():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_messages(messages):
    with open(DATA_FILE, 'w') as f:
        json.dump(messages, f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    messages = load_messages()
    if request.method == 'POST':
        username = request.form['username']
        comment = request.form['comment']
        messages.append({'username': username, 'comment': comment})
        save_messages(messages)
        return redirect('/message')
    return render_template('message.html', messages=messages)
