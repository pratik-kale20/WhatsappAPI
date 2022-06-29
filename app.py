import flask
from flask import request
import requests
import json

app = flask.Flask(__name__)
url = "https://api.interakt.ai/v1/public/message/"

@app.route('/', methods = ['GET'])
def home():
    token = str(request.args['token'])
    mobile = str(request.args['mobile'])
    empName = str(request.args['emp'])
    visitorName = str(request.args['visitor'])
    purpose = str(request.args['purpose'])
    try: 
        payload = json.dumps({
        "countryCode": "+91",
        "phoneNumber": mobile,
        "callbackData": "Error message",
        "type": "Template",
        "template":{
            "name":"Appointmentapp",
            "languageCode": "en",
            "bodyValues": [
                empName,
                visitorName,
                purpose    
            ]
        }  
        })
        headers = {
        'Authorization': 'Basic '+ token,
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return 'working'
    except:
        return  "Error Message"
