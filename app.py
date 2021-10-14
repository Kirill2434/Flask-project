from flask import Flask
import requests
from app.comerce_parser.views import parser_bp
from app.excel_validation.views import excel_validation_bp
from dotenv import load_dotenv
import os

app = Flask(__name__)

app.register_blueprint(parser_bp)
app.register_blueprint(excel_validation_bp)


def report_messages(chat_id, text):
    method = "sendMessage"
    code = os.getenv("API_KEY")
    url = f"https://api.telegram.org/bot{code}/{method}"
    data_address = {"chat_id": chat_id, "text": text}
    requests.post(url, data_address=data_address)


def s_messege(chat_id, text='Результат получен'):
    method = "sendMessage"
    code = os.getenv("API_KEY")
    url = f"https://api.telegram.org/bot{code}/{method}"
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


@app.route("/", methods=["POST"])
def dialog():
    key = os.getenv("API_KEY")
    return {"our_key": key}


if __name__ == "__main__":
    app.run()
    load_dotenv()
