from flask import Flask
from flask import request
from send_example import send_example_json
from flask import render_template
import json
from send_api_key import send_mapbox_api_key
import psycopg2

app = Flask(__name__)

api_key = send_mapbox_api_key()

## If running through SQL
list_to_features = send_example_json()

# ## If loading from .json
# in_file = open('data/cong_113.json','r')
# list_to_features = json.load(in_file)
# in_file.close()

cong_113 = json.dumps(list_to_features)

@app.route('/')
def map():
    ## Have the home page be a place to input a file or paste the lat/long (address if ambitious)
    return render_template("Texas.html", cong_113 = cong_113, api_key = )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6969, debug=True)
