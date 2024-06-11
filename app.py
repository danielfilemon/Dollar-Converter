from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    euro = amount / 1.18  # Assuming 1 dollar equals 1.18 euros
    return jsonify({'euro': euro})

if __name__ == '__main__':
    app.run(debug=True)

