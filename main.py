from flask import Flask, request, jsonify
import requests

app = Flask('__name__')

@app.route('/tapetes', methods=['GET'])
def get_data():





app.run(debug=True)