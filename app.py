from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! This is containerized Flask App from CI/CD'

@app.route('/health')
def health():
    return jsonify(status='ok')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
