from flask import Flask, request, jsonify

# Flask app initialization
app = Flask(__name__)


@app.route('/server', methods=['GET'])
def server():
    return {'data': 'Flask server'}


@app.route('/mine', methods=['POST'])
def mine():
    print(request.get_json()['data'])
    return 'weq', 200


app.run(host='localhost', port=5000, debug=True)
