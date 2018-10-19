# -*- coding: utf-8 -*-
# 必要なモジュールの読み込み
from flask import Flask, jsonify,make_response

# Flaskクラスのインスタンスを作成
# __name__は現在のファイルのモジュール名
app = Flask(__name__)

# GETの実装
@app.route('/get', methods=['GET'])
def get():
    result = { "greeting": 'hello flask' }
    return make_response(jsonify(result))

# エラーハンドリング
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#appを起動
if __name__ == '__main__':
	app.run()
