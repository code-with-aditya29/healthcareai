# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load Excel data once when the app starts
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
        # Search for input in Excel (case-insensitive)
        match = df[df['Keyword'].str.lower() == user_input]
        if not match.empty:
            return jsonify({'response': match.iloc[0]['Response']})
    
    # Default response if no match found
    return jsonify({'response': "I'm still learning! Can't find a response for that."})

if __name__ == '__main__':
    app.run(debug=True)




#for intallation pip this
# pip install flask pandas openpyxl


#for running 
#python app.py