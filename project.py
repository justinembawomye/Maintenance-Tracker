
from flask import Flask, jsonify,request
from app.models import *

app = Flask(__name__)

#Request Responses
login_successful={
        'success':True,
        'message':"Logined in Succesfully.",
        'token':123
        }
login_fail={
        'success':False,
        'message':"Logined Failed."
        }
auth_fail={
        'success':False,
        'message':"You are not authorised to access this page."
        }
request_fail={
        'success':False,
        'message':"Not a valid Request ID."
        }
create_request_fail={
        'success':False,
        'message':"All fields required."
        }
create_request_successful={
        'success':True,
        'message':"Your request was submitted successfully.",
        'token':123
        }
requests = [{'id': 20003,'title': u'Range Rover','type': u'Repair','category': u'Cars','status':u'Completed'},{'id': 20004,'title': u'Samsung S7','type': u'Repair','category': u'Phones and Tablet','status':u'In Progress'}]


#Making an API Endpoint (GET)
@app.route('/')
def api_documentation():
    return "Maintenance-Tracher"

@app.route('/api/v1/login', methods=['POST'])
def api_login():
    data = request.args
    username = data.get("username")
    password = data.get("password")

    if username == "Bes":
        if password == "1234567890":
            return jsonify(login_successful)
        else:
            return jsonify(login_fail)
    else:
        return jsonify(login_fail)


@app.route('/api/v1/users/requests')
def api_get_requests():
    try:
        token = request.headers["Authorization"]
    except:
        return jsonify(auth_fail)

    if token == '123':
        return jsonify(requests)
    else:
        return jsonify(auth_fail)

@app.route('/api/v1/users/requests/<requestId>', methods=['GET'])
def api_get_logged_in_user_requests(requestId):
    try:
        token = request.headers["Authorization"]
    except:
        return jsonify(auth_fail)

    if token == '123':
        if int(requestId) < len(requests) and int(requestId) >= 0:   
            return jsonify(requests[int(requestId)])
        else:
            return jsonify(request_fail)
    else:
        return jsonify(auth_fail)

@app.route('/api/v1/users/requests', methods=['POST'])
def api_create_request():
    data = request.args
    requestTitle=data.get("title")
    requestType = data.get("type")
    requestCategory=data.get("category")
    requestStatus=data.get("status")

    try:
        token = request.headers["Authorization"]
    except:
        return jsonify(auth_fail)

    if token == '123':
        if requestTitle!= None and requestType!= None and requestCategory!= None and requestStatus!= None:
            return jsonify(create_request_successful)
        else:
            return jsonify(create_request_fail)
    else:
        return jsonify(auth_fail)

@app.route('/api/v1/users/requests/<requestId>', methods=['PUT'])
def api_modify_request(requestId):
    data = request.args
    requestTitle=data.get("title")
    requestType = data.get("type")
    requestCategory=data.get("category")
    requestStatus=data.get("status")

    try:
        token = request.headers["Authorization"]
    except:
        return jsonify(auth_fail)

    if token == '123':
        if int(requestId) < len(requests) and int(requestId) >= 0:   
            if requestTitle!= None and requestType!= None and requestCategory!= None and requestStatus!= None:
                return jsonify(create_request_successful)
            else:
                return jsonify(create_request_fail)
        else:
            return jsonify(request_fail)
    else:    
        return jsonify(auth_fail)

if __name__ == '__main__':
    app.run(debug=True)