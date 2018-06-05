
from flask import Flask, jsonify,request
from app.models.Responses import * 
from app.models.User import User
from app.models.UserRequest import UserRequest
from app.models.DataStore import *
import jwt


app = Flask(__name__)
temp_users=[User("Sam","Weinchester","sammy@gmail.com","Sam","123",True)]
temp_requests=[UserRequest( "Samsung S7","Repair","Mobile Devices","In Progress","Sam"),UserRequest( "Range Rover","Repair","Cars","In Progress","Sam")]
data_store = DataStore(temp_users,temp_requests)


# Making an API Endpoint (GET)
@app.route('/')
def api_documentation():
    return "Maintenance-Tracher"


@app.route('/api/v1/login',methods=['POST'])
def api_login():
    data = request.get_json(force=True)
    username = data.get('username', None)
    password = data.get('password', None)

    print(username)

    user = data_store.searchList(username)
    if user is not None:
        if user.verify_password(password):
            response = user.getDictionary()
            response["token"]=data_store.generate_auth_token(response)
            response["success"]=True
            print(str(response))
            return jsonify(response)
        else:
            return jsonify(login_fail), 200
    else:
        return jsonify(login_fail) ,200


@app.route('/api/v1/register', methods=['POST'])
def register_user():
    data = request.args
    firstName = data.get("first_name")
    lastName = data.get("last_name")
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if firstName is not None and lastName  is not None and email  is not None and username is not None and password is not None:
        user = data_store.searchList(username)
        if user is None :
            response = data_store.createUser(User(firstName,lastName,email,username,password)).getDictionary()        
            response["token"]=data_store.generate_auth_token(response)
            registration_successful["user"]=response
            return jsonify(registration_successful)
           
        else:
            return jsonify(login_fail) ,401
    else:
        return jsonify(create_request_fail)


@app.route('/api/v1/users/requests')
@data_store.token_required
def api_get_requests(current_user):
        # print(current_user)
        return jsonify(data_store.getAllRequestsForUser(current_user.getUserName()))


@app.route('/api/v1/users/requests/<requestId>', methods=['GET'])
@data_store.token_required
def api_get_sepecific_request(current_user,requestId):
    req = data_store.getASpecificRequestsForUser(requestId)
    if req is not None:
        create_request_successful['data']=req
        return jsonify(create_request_successful)
    else:
        return jsonify(request_fail)


@app.route('/api/v1/users/requests', methods=['POST'])
@data_store.token_required
def api_create_request(current_user):

    data = request.get_json(force=True)
    request_title = data.get('title', None)
    request_type = data.get('type', None)
    request_category = data.get('category', None)
    request_status = data.get('status', None)
    if request_title is not None and request_type is not None and request_category is not None and request_status is not None:
        req = UserRequest(request_title,request_type,request_category,request_status,current_user.getUserName())
        create_request_successful['data']=data_store.addRequest(req).getDictionary()
        return jsonify(create_request_successful)
    else:
        return jsonify(create_request_fail)
   

@app.route('/api/v1/users/requests/<requestId>', methods=['PUT'])
@data_store.token_required
def api_modify_request(current_user,requestId):
    data = request.args
    data = request.get_json(force=True)
    requestTitle = data.get('title', None)
    requestType = data.get('type', None)
    requestCategory = data.get('category', None)
    requestStatus = data.get('status', None)
    print(requestTitle)

    if requestTitle is not None and requestType is not None and requestCategory is not None and requestStatus is not None:
        req=UserRequest(requestTitle,requestType,requestCategory,requestStatus,current_user.getUserName(),requestId)  
        mod_req=data_store.modifyRequest(req)
        if mod_req is not None:
            create_request_successful['data'] = mod_req
            return jsonify(create_request_successful)
        else:
            return jsonify(request_fail)
    else:
        return jsonify(create_request_fail)


if __name__ == '__main__':
    app.run(debug=True)