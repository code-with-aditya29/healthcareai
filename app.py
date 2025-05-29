from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

try:
    df = pd.read_excel('responses.xlsx')
except FileNotFoundError:
    print("Error: responses.xlsx file not found!")
    df = pd.DataFrame()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input', '').strip().lower()
    if not user_input:
        return jsonify({'response': 'Please enter something!'})
    if not df.empty:
        match = df[df['Keyword'].str.lower() == user_input]
        if not match.empty:
            return jsonify({'response': match.iloc[0]['Response']})
    return jsonify({'response': "I'm still learning! Can't find a response for that."})

if __name__ == '__main__':
    app.run(debug=True)
