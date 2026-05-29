from flask import Flask, request, jsonify
import requests

url_api = 'https://testedefensoriapr.pythonanywhere.com/precos'

app = Flask('__name__')

@app.route('/tapetes', methods=['GET'])
def get_data():
    date_informed = request.args.get('date')

    if not date_informed:
        return "Erro: O parâmetro 'data' é obrigatório", 400
    





app.run(debug=True)