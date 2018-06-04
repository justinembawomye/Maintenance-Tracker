
from flask import Flask, jsonify,request
from app.models.Responses import * 
from app.models.User import User
from app.models.UserRequest import UserRequest
from app.models.DataStore import *
import jwt


app = Flask(__name__)
temp_users=[User("Sam","Weinchester","sammy@gmail.com","Sam","123")]
temp_requests=[UserRequest( "Samsung S7","Repair","Mobile Devices","In Progress","Sam"),UserRequest( "Range Rover","Repair","Cars","In Progress","Sam")]
data_store = DataStore(temp_users,temp_requests)

#Making an API Endpoint (GET)
@app.route('/')
def api_documentation():
    return "Maintenance-Tracher"

@app.route('/api/v1/login', methods=['POST'])
def api_login():
    data = request.args
    username = data.get("username")
    password = data.get("password")

    user = data_store.searchList(username)
    if user != None :
        if user.verify_password(password):
            response = user.getDictionary()
            response["token"]=data_store.generate_auth_token(response)
            print(str(response))
            return jsonify(response)
        else:
            return jsonify(login_fail), 401
    else:
        return jsonify(login_fail) ,401


@app.route('/api/v1/users/requests')
@data_store.token_required
def api_get_requests(current_user):
       # print(current_user)
        return jsonify(data_store.getAllRequestsForUser(current_user.getUserName()))


@app.route('/api/v1/users/requests/<requestId>', methods=['GET'])
@data_store.token_required
def api_get_logged_in_user_requests(current_user,requestId):

        return jsonify(data_store.getASpecificRequestsForUser(requestId))

@app.route('/api/v1/users/requests', methods=['POST'])
@data_store.token_required
def api_create_request(current_user):
    data = request.args

    requestTitle=data.get("title")
    requestType = data.get("type")
    requestCategory=data.get("category")
    requestStatus=data.get("status")

   
    if requestTitle!= None and requestType!= None and requestCategory!= None and requestStatus!= None:
        req =UserRequest(requestTitle,requestType,requestCategory,requestStatus,current_user.getUserName())
        create_request_successful['data']=data_store.addRequest(req).getDictionary()
        return jsonify(create_request_successful)
    else:
        return jsonify(create_request_fail)
   

@app.route('/api/v1/users/requests/<requestId>', methods=['PUT'])
@data_store.token_required
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


if __name__ == '__main__':
    app.run(debug=True)