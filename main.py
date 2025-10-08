from flask import Flask, render_template, jsonify
from odds_api import get_live_odds
from arbitrage import detect_arbitrage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/arbs')
def get_arbs():
    odds_data = get_live_odds("soccer")
    arbs = detect_arbitrage(odds_data)
    return jsonify(arbs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
