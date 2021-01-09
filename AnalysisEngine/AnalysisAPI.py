from flask import Flask, jsonify
from flask_cors import CORS
import json
from Engine import getTotal, getAnalysisData

app = Flask(__name__)
CORS(app)


# https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
@app.route('/GetData')
def GetData(data):
    print(data);
    val = getAnalysisData(data);
    df_list = val.values.tolist()
    JSONP_data = jsonify(df_list)
    return JSONP_data


@app.route('/GetTotal')
def GetTotal():
    val = getAnalysisData();
    total = getTotal(val);
    df_list = total.values.tolist()
    JSONP_data = jsonify(df_list)
    return JSONP_data


if __name__ == '__main__':
    app.run()
