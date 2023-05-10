from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    # print(data)
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    cf = fetch_conversion_factor(source_currency, target_currency)
    final_amount = cf * amount
    # print(cf * amount)

    response = {
        'fulfillmentText': "{} {} is {} {}".format(amount, source_currency, final_amount, target_currency)
    }
    return jsonify(response)
    # return "Hello1"


def fetch_conversion_factor(source, target):
    # don't have the API to get result from
    # so will send dummy result
    return 74


if __name__ == "__main__":
    app.run(debug=True)
