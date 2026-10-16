from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Cloud Deployment Lab!",
        "developer_name": "Sarthak Chaudhary",
        "version": "1.0.0",
        "status": "Running successfully in Docker on AWS EC2"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)