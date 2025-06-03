from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Chào mừng bạn đến với Lab 3 - Đoàn Quốc Thịnh</h1>"
