from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='static')

exchange_rates = {
    'euro': 0.85,  # Assuming 1 dollar equals 0.85 euros
    'real': 5.00,  # Assuming 1 dollar equals 5.00 reais
    'usd': 1.00    # Assuming 1 dollar equals 1 dollar
}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        print(f"Received amount: {amount} from currency: {from_currency} to currency: {to_currency}")
        if amount < 0:
            raise ValueError("Amount must be positive")
        
        from_rate = exchange_rates.get(from_currency)
        to_rate = exchange_rates.get(to_currency)
        
        if from_rate is None or to_rate is None:
            raise ValueError("Invalid currency")
        
        # Convert the amount to USD first, then to the target currency
        amount_in_usd = amount / from_rate
        converted_amount = amount_in_usd * to_rate
        
        return jsonify({to_currency: converted_amount})
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)

