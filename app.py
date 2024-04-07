from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    message = data.get('message')
    print("Received message from Raspberry Pi:", message)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
