import flask

from flask import request, jsonify

from text2graph import Text2Graph


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Normalized Centrality Measure</h1><p>Enter a document " \
           "snippet to see the relative importance of each word.</p>"


@app.route('/api/v1/centrality', methods=['GET'])
def api_centrality_score():
    if 'text' in request.args:
        document = request.args['text']
    else:
        return "Error: No id field provided"

    doc = Text2Graph(document)
    doc.preprocess(stop_filter=True, pos_filter=False)
    doc.transform(window=2)
    results = doc.normalized_degree_centrality()

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)

