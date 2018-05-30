
from flask import Flask, jsonify,request
app = Flask(__name__)

requests = [{'id': 20003,'title': u'Range Rover','type': u'Repair','category': u'Cars','status':u'Completed'},{'id': 20004,'title': u'Samsung S7','type': u'Repair','category': u'Phones and Tablet','status':u'In Progress'}]


#Making an API Endpoint (GET)
@app.route('/')
def api_documentation():
    return "Hello World"

@app.route('/api/v1/requests')
def get_requests():
   
    return jsonify(requests)

@app.route('/requests', methods=['POST'])
def add_request():
    requests.append(request.get_json())
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)