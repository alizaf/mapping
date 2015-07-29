from flask import Flask
from flask import request
from send_example import send_example_json
from flask import render_template
import json

import psycopg2

app = Flask(__name__)

list_to_export = send_example_json()

cong_113 = json.dumps(list_to_export)

@app.route('/')
def map():
    ## Have the home page be a place to input a file or paste the lat/long (address if ambitious)
    return render_template("Texas.html", cong_113 = cong_113)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6969, debug=True)
