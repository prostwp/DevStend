from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get_link', methods=['GET'])
def get_link():
    generated_link = "https://www.tradingview.com/x/vGqaV4qM/"

    return jsonify({"link": generated_link})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)