from flask import Flask, request, jsonify
import requests
from flasgger import Swagger


url_api = 'https://testedefensoriapr.pythonanywhere.com/precos'

app = Flask(__name__)
app.json.ensure_ascii = False
app.json.sort_keys = False
Swagger(app)

@app.route('/tapetes', methods=['GET'])
def get_data():

    """
    API de busca de preços de tapetes por data
    --- 
    parameters:
      - name: date
        in: query
        type: string
        required: true
        description: Data deve ser informada pelo usuário

    responses:
      200:
        description: Requisição realizada com sucesso

      400:
        description: Parâmetro informado não informado

      503:
        description: API externa indisponível

    """

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