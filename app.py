import logging
from flask import Flask, jsonify, render_template
from osrs_api import izracunaj_vse_profite

app = Flask(__name__)

# Izklop odvečnega šuma v terminalu
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/data')
def api_data():
    podatki = izracunaj_vse_profite()
    return jsonify(podatki)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
