from flask import Flask, jsonify
from module import search_filter

app = Flask(__name__)


@app.route('/get_info/<data>', methods=['Get'])
def main_fun(data):
    info = search_filter.search(data)

    return jsonify(info)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
