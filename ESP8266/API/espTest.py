SSID="Tufts_Wireless" # Network SSID
KEY=""  # Network key
tsATappkey = "keyq6MX1zmMDU7txy"
ATdocID = 'appof7fJr134DCw3p'

import ESPClient, ujson
ESPClient.wifi('SSID','PASS')
PORT = 443
Key = 'Bearer ' + tsATappkey
base='api.airtable.com'
request='%s /v0/%s/%s HTTP/1.1\\r\\n' 
request += 'Host: %s\\r\\n' % base
request += 'Content-Type: application/json\\r\\n'
request += 'Accept: application/json\\r\\n'
request += 'Authorization: %s\\r\\n' %Key
    
def readIt(table):
    req = request % ('GET','docID',table)
    req += '\\r\\n'
    print(req)
    code, reason, reply = ESPClient.REST(base, PORT, req, False)
    try:
        if code == 200:
            Json = reply.split("\\r\\n")[-3]
            response = ujson.loads(Json)['rows'][0]
            return code, response[property]
        else:
            return code, reason
    except:
        return (-1, reply)

def writeIt(table, field, Value):
    
    payload = {"records": [{"fields": {field: Value}}]}
    payload = ujson.dumps(payload)
    print(payload)
    req = request % ('PUT','docID',table)
    req += 'Content-Length: %d\\r\\n\\r\\n' % len(payload)
    req += 'json=%s\\r\\n\\r\\n' % payload
    print(req)

    code, reason, reply = ESPClient.REST(base, PORT, req, False)
    try:
        if code == 200:
            return code, reply
        else:
            return code, reason
    except:
        return (-1, reply)
        
        
        