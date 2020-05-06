import flask
import json

from flask import (jsonify,
                   make_response,
                   request)
from jsonschema import (validate,
                        ValidationError)

from centrality_metrics.text2graph import Text2Graph


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Normalized Centrality Measure</h1><p>Enter a text " \
           "snippet to see the importance of each word. The text is first " \
           "represented as a graph. Then, by computing the number of " \
           "edges to each node, the normalized centrality of the words are " \
           "determined.</p>"


@app.route('/api/v1/centrality', methods=['GET'])
def api_centrality_score():
    schema = {
        "type": "object",
        "properties": {
            "text": {
                "type": "string"
            }
        },
        "required": ["text"]
    }
    headers = {"Content-Type": "application/json"}
    input_params = {key: value for key, value in request.args.items()}

    try:
        validate(input_params, schema)
    except ValidationError as e:
        validation_error = json.dumps(
            {
                f'error': '{e.message}. Expected {schema["required"]}'
            },
            indent=4, sort_keys=True
        )
        return make_response(validation_error, 400, headers)

    req = request.args["text"]
    if req == "":
        value_error = json.dumps(
            {
                "error": "value error. Expected non empty string"
            },
            indent=4, sort_keys=True
        )
        return make_response(value_error, 400, headers)

    doc = Text2Graph(req)
    doc.preprocess_text(stop_filter=True, pos_filter=True)
    doc.transform(window=2)
    results = doc.normalized_degree_centrality()
    return make_response(jsonify(results), 200, headers)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

