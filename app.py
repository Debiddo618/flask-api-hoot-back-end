from flask import Flask, jsonify, request, g
from dotenv import load_dotenv

import bcrypt
from auth_middleware import token_required
from auth_blueprint import authentication_blueprint
from hoots_blueprint import hoots_blueprint
from comments_blueprint import comments_blueprint



load_dotenv()

app = Flask(__name__)
app.register_blueprint(hoots_blueprint)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(comments_blueprint)


# Run our application, by default on port 5000
app.run(debug=True)
