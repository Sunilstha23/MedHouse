from flask import Flask, render_template, jsonify, request

from chatapp import ChatApp as ca
app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('chatbot.htm', **locals())
    
@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']
        response = ca.chatbot_response(the_question)
        return jsonify({"response": response })

if __name__ == '__main__':
    app.run()