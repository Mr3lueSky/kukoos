from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/transactions')
def transactions():
    # Here you could retrieve transaction data from a database or external API and pass it to the transactions.html template
    return render_template('transactions.html')

if __name__ == '__main__':
    app.run(debug=True)
