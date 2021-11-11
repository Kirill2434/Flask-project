import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request

parser_bp = Blueprint('parser_bp', __name__)


@parser_bp.route("/infoLMFC", methods=["POST"])
def tikets():
    url = request.json['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    result_quotes = []
    for quote in quotes:
        result_quotes.append(quote.text)
    return {'result': result_quotes}

