
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


@app.route('/api/v1/requests')
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

if __name__ == '__main__':
    app.run(debug=True)