from flask import Flask, jsonify, request, make_response

app = Flask(__name__)  # create Flask application object

@app.route('/')  # assign this view function to '/' (i.e., the "root: of the web site)
def index():  # define the view function
    return '<h1>Hello, Flask world!</h1>' # return HTML for the page to display

# default (str)
# int
# float
# path (misc)
@app.route('/user/<int:id>')
def user_by_id(id):
    return f"<h2>This is user #{id}</h2>"


@app.route('/user')
def no_user():
#    raise InvalidUserSpec
    return f"<h2>No user ID specified</h2>"

class InvalidAPIRequest(Exception):
    status_code = 400
    def __init__(self, message, status_code=None, data=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self._data = data

    def to_dict(self):
        return_value = dict(self._data or ())
        return_value['message'] = self.message
        return  return_value

@app.errorhandler(InvalidAPIRequest)
def handle_invalid_request(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/student/<int:id>', methods=['POST', 'GET'])
def student(id):
    # IRL get data from DB
    accept_type = request.headers.get("ACCEPT")
    if accept_type and accept_type.endswith('json'):
        data = {
            'id': id,
            'first_name': 'Fred',
            'last_name': 'Flintstone',
            'city': 'Bedrock',
            # 'data': request.form,
            'json': request.json,
            'accept type': accept_type,
        }
        response = make_response(jsonify(data), 202)
        print(f"{type(response) = }")
        return response
    else:
        raise InvalidAPIRequest("Bad user ID", 404, {'id': id})
    

# app.register_route(index, '/')

if __name__ == '__main__':
    app.run(debug=True) # start the development server
