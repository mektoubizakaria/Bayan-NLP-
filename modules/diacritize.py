import json
import http.client

def diacritize(article):
    article = article.replace('"', '')
    conn = http.client.HTTPSConnection("farasa-api.qcri.org")
    payload = "{\"text\":\"%s\"}"% article
    payload = payload.encode('utf-8')
    headers = { 'content-type': "application/json", 'cache-control': "no-cache", }
    conn.request("POST", "/msa/webapi/diacritizeV2", payload, headers)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    data_dict = json.loads(data)
    return data_dict['output'] 