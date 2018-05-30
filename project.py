
from flask import Flask, jsonify,request
from app.models import *

app = Flask(__name__)

#Request Responses
login_successful={
        'success':true
        'message':"Logined in Succesfully."
        'token':123
        }
login_fail={
        'success':false
        'message':"Logined Failed."
        }
requests = [{'id': 20003,'title': u'Range Rover','type': u'Repair','category': u'Cars','status':u'Completed'},{'id': 20004,'title': u'Samsung S7','type': u'Repair','category': u'Phones and Tablet','status':u'In Progress'}]


#Making an API Endpoint (GET)
@app.route('/')
def api_documentation():
    return "Maintenance-Tracher"

@app.route('/api/v1/login')
def api_login():
    data = request.get_json(force==true)
    username = data.get('name',None)
    password = data.get('name',None)

    if username == "Bes":
        if password == "1234567890":
            return jsonify(login_successful)
        else
            return jsonify(login_fail)
    else:
        return jsonify(login_fail)


@app.route('/api/v1/requests')
def get_requests():
    auth_token = request.headers.get('Authorization')
    if auth_token:
        response =UserLoginRequest.  
    return jsonify(requests)

@app.route('/requests', methods=['POST'])
def add_request():
    requests.append(request.get_json())
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)