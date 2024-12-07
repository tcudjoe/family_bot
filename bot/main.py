from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data['Body']
    sender = data['From']
    print(f"Message from {sender}: {message}")
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)

if __name__ == '__main__':
    app.run(port=5000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def start_bot():
    return None