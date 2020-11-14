from flask import Flask, jsonify
from Engine import getTotal,getAnalysisData
app = Flask(__name__)
#https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
@app.route('/')
def GetData():
   val=getAnalysisData();
   total=getTotal(val);
   return  jsonify(dict(data=[val, total]));

if __name__ == '__main__':
   app.run()