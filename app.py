from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/frotar/<int:n_frases>')
def obtener_frases(n_frases):
	frases_aleatorias = frotar(n_frases)
	print(frases_aleatorias)
	return jsonify({'Frases auspiciosas:': frases_aleatorias})


@app.route('/')
def hello_world():
    return '¡prueba!'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

if __name__ == '__main__':
	main()
