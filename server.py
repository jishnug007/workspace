import meinheld
from flask import jsonify, Flask
from flask_cors import CORS

from handler import fetchNlp

app = Flask(__name__)
CORS(app)

app.add_url_rule('/searchNlp',
                 view_func=fetchNlp.as_view('nlp'))


@app.route('/')
def hello():
    return "MY NLP"


@app.after_request
def apply_caching(response):
    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == '__main__':
    port = 8000
    print('App listening on %s' % str(port))
    meinheld.listen(("0.0.0.0", port))
    meinheld.run(app)
    # app.run( host='0.0.0.0',threaded=True)
