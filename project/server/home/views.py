# project/server/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

home_blueprint = Blueprint('home', __name__)

class HomeAPI(MethodView):
    """
    User Registration Resource
    """

    def get(self):  

        # Create response object
        responseObject = {
            'user_list': "http://ec2-54-152-152-116.compute-1.amazonaws.com:8000/users/index",
            'registration': "http://ec2-54-152-152-116.compute-1.amazonaws.com:8000/auth/register"
        }
        return make_response(jsonify(responseObject)), 2010     


# define the API resources
home_view = HomeAPI.as_view('home_api')

# add Rules for API Endpoints
home_blueprint.add_url_rule(
    '/',
    view_func=home_view,
    methods=['GET']
)