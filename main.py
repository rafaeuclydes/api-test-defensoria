from flask import Flask, request, jsonify
import requests


url_api = 'https://testedefensoriapr.pythonanywhere.com/precos'

app = Flask('__name__')
app.json.ensure_ascii = False
app.json.sort_keys = False

@app.route('/tapetes', methods=['GET'])
def get_data():

    date_informed = request.args.get('date')

    if not date_informed:
        return jsonify({'Erro': "O parâmetro 'data' é obrigatório"}), 400
    
    try:
        data_extapi = requests.get(url_api)
        resposta = data_extapi.json()

    except Exception as error:
        return jsonify({'Erro': 'Sentimos muito, nossa API esta indisponível no momento', 'detalhes': str(error)}), 503
    
    resultado_busca = {
        'data da busca': date_informed,
        'dados disponíveis': resposta
    }

    return jsonify(resultado_busca)


if __name__ == '__main__':
    app.run(debug=True, port=8080)