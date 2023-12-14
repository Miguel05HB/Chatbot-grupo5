from flask import Flask, render_template, request, jsonify
from chatbot import obtener_respuesta, aprender_respuesta_web

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    bot_response = obtener_respuesta(user_message)
    return jsonify({'bot_response': bot_response})

@app.route('/teach_bot', methods=['POST'])
def teach_bot():
    user_message = request.form['user_message']
    respuesta_aprendida = request.form['respuesta_aprendida']
    aprender_respuesta_web(user_message, respuesta_aprendida)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
