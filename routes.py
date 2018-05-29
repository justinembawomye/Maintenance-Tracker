from flask import Flask, jsonify
app = Flask(__name__)

test=[{'title': u'Hello World'}]


#Making an API Endpoint (GET)
@app.route('/')
def user_request():
	return jsonify(test)



requests = [
    {
        'id': 20003,
        'title': u'Range Rover',
        'type': u'Repair',
        'category': u'Cars', 
        'status':u'Completed' 
    },
    {
        'id': 20004,
        'title': u'Samsung S7',
        'type': u'Repair',
        'category': u'Phones and Tablet', 
        'status':u'In Progress' 
    }
]

@app.route('/api/v1.0/requests', methods=['POST'])
def get_hello_world():
    return jsonify(requests)

@app.route('/api/v1.0/users/requests/<requestId>', methods=['GET'])
def get_requests():
    return jsonify(requests)



if __name__ == '__main__':
    app.run(debug=True)