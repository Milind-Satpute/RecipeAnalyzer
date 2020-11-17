from flask import Flask, jsonify
import json
from Engine import getTotal,getAnalysisData
app = Flask(__name__)
#https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
@app.route('/GetData')
def GetData():
   val=getAnalysisData();
   df_list = val.values.tolist()
   JSONP_data = jsonify(df_list)
   return JSONP_data



@app.route('/GetTotal')
def GetTotal():
    val = getAnalysisData();
    total=getTotal(val);
    df_list = total.values.tolist()
    JSONP_data = jsonify(df_list)
    return JSONP_data

if __name__ == '__main__':
   app.run()