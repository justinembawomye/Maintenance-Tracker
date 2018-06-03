
from flask import Flask, jsonify,request
from app.models.Responses import * 
import app.models.User import User

app = Flask(__name__)




#Making an API Endpoint (GET)
@app.route('/')
def api_documentation():
    return "Maintenance-Tracher"

@app.route('/api/v1/login', methods=['POST'])
def api_login():
    data = request.args
    username = data.get("username")
    password = data.get("password")

    user = searchList(username)

    if user != None :
        if user.verify_password(password):
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
    requestTitle=data.get('title')
    requestType = data.get('type')
    requestCategory=data.get('category')
    requestStatus=data.get('status')

    try:
        token = request.headers["Authorization"]
    except:
        return jsonify(auth_fail)

    if token == '123':
        if int(requestId) < len(requests) and int(requestId) >= 0:   
            if requestTitle != None and requestType != None and requestCategory!= None and requestStatus!= None:
                return jsonify(create_request_successful)
            else:
                return jsonify(create_request_fail)
        else:
            return jsonify(request_fail)
    else:    
        return jsonify(auth_fail)

def searchList(username):
    for item in self.users:
        if item.getUserName() == username:
            return item
        else:
            return None

if __name__ == '__main__':
    self.users=[]
    self.requests=[]
    app.run(debug=True)