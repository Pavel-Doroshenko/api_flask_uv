from flask.json.provider import DefaultJSONProvider
from flask import Flask, jsonify, request
from model.twit import Twit

twits = []  # Список для хранения в памяти твитов


class CustomJSONProvider(DefaultJSONProvider):
    def default(self, obj):
        """Функция переопределения метода default. Если объект является экземпляром класса Twit
        возвращается словарь с ключами body и autor. Во всех остальных случаях возвращается
        медод default родительского клосса DefaultJSONProvader
        """
        if isinstance(obj, Twit):
            return {"body": obj.body, "author": obj.author}
        else:
            return super().default(obj)


app = Flask(__name__)
app.json = CustomJSONProvider(
    app
)  # Здесь сообщаем приложению, что у нас собственный обработчик json


@app.route("/twit", methods=["POST"])
def create_twit():
    """Создание твита. Необходимо в тело запроса передать словарь
    {'body': 'hello world', 'author': '@aqaguy'}
    """
    twit_json = request.get_json()
    twit = Twit(twit_json["body"], twit_json["author"])
    twits.append(twit)
    return jsonify({"status": "success"})


@app.route("/twit", methods=["GET"])
def read_twits():
    return jsonify({"twits": twits})


@app.route("/twit", methods=["PUT"])
def update_twits():
    """Обновление твита. По умолчанию обновляется первый твит"""
    twit_json_update = request.get_json()
    twit = Twit(twit_json_update["body"], twit_json_update["author"])
    twits[0] = twit
    return jsonify({"status": "success"})


@app.route("/twit", methods=["DELETE"])
def delete_json():
    """Удаление твита. По умолчанию удаляется последний твит"""
    twits.pop()
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
