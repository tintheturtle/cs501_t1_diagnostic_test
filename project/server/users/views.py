# project/server/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

user_blueprint = Blueprint('user', __name__)

class UserAPI(MethodView):
    """
    User Registration Resource
    """

    def get(self):        
    	# Get all users
        users = User.query.all()

        try:
            # Extract data from User Models
            user_list = [ {"id": user.id, "email": user.email } for user in users ]

            # User List is non-empty
            responseObject = {
                'status': 'success',
                'message': 'Successfully queried database.',
                'user_list': user_list
            }
            return make_response(jsonify(responseObject)), 201
        except Exception as e:
            # Error occurred
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401

# define the API resources
user_view = UserAPI.as_view('user_api')

# add Rules for API Endpoints
user_blueprint.add_url_rule(
    '/users/index',
    view_func=user_view,
    methods=['GET']
)