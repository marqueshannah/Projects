import redis
from flask import Flask, request
import json
import logging

app=app = Flask(__name__)

rd=redis.Redis(host='172.17.0.3', port=6418)


@app.route('/data', methods = ['POST'])
def read_data_file():
    try:
        with open('meteorite_landings.json', 'r') as f:
            ml = json.load(f)
        
        for item in ml['meteorite_landings']:
            rd.set(item['id'], json.dumps(item))
        return f'The data has been read\n'   
    except FileNotFoundError as no_file:
        logging.error(no_file)
        return 'Failed to open the file or File does not exist.'

@app.route('/data', methods=['GET'])
def load_data():
    ml_data_list = []
    for i in range(10001, 10301, 1):
        ml_data_list.append(json.loads(rd.get(i)))
    return json.dumps(ml_data_list, indent=2)
