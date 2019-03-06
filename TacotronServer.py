import argparse
import parser

from flask import Flask, jsonify, render_template, request, make_response
from synthesizer import Synthesizer


app = Flask(__name__)



@app.route('/')
def index():
    parser = argparse.ArgumentParser()
    parser.add_argument('--checkpoint', required=True, help='Full path to model checkpoint')
    args = parser.parse_args()
    synthesizer = Synthesizer()
    synthesizer.load(args.checkpoint)
    a = request.args.get('text')

    response = make_response()
    response.data = synthesizer.synthesize(a)
    response.content_type = 'audio/wav'


    return response

if __name__ == '__main__':

   app.run(host='0.0.0.0')

