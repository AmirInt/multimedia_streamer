from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health_check', methods=['GET'])
def check_health():
    return jsonify({
        'message': 'Whoa!'
    }), 200

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8000)