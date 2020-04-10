#!flask/bin/python
from flask import Flask,request,send_from_directory,jsonify,Response
import json
import sys  
sys.path.append('modules/')  
import predict as pre
import preprocessing as pro
import diacritize as dia

app = Flask(__name__)

@app.route('/text_classification', methods=['GET'])
def get_tasks():
    url_text = request.args.get('url')
    article=pro.pipeline(url_text)
    classe=pre.predict(article)
    data={'class': classe,'text':str(article)}
    # json.dumps(data, ensure_ascii=False)

    response = Response(json.dumps(data,ensure_ascii = False),content_type="application/json; charset=utf-8" )
    return response
   

@app.route('/', methods=['GET'])
def get_index():
    return send_from_directory('.', 'index.html')

@app.route('/diacritize', methods=['GET'])
def get_diac():
    url_text = request.args.get('url')
    article=pro.pipeline(url_text)
    article_diac=dia.diacritize(article)
    response = Response(json.dumps(article_diac,ensure_ascii = False),content_type="application/json; charset=utf-8" )
    return response

if __name__ == '__main__':
    app.run(debug=True)
