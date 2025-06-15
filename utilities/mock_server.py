from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/submit-order', methods=['POST'])
def submit_order():
    data = request.get_json()
    print(f"Order received: {data}")
    return jsonify({"status": "success", "order_id": 12345}), 200

if __name__ == '__main__':
    app.run(port=5001)
