from flask import Flask, jsonify
from config import Config
from extensions import db, jwt
from flask_cors import CORS
from routes.auth import auth_bp
from routes.opportunities import opp_bp

app = Flask(__name__)
app.config.from_object(Config)

# Proper CORS for JWT
# CORS(app, resources={r"/api/*": {
#     "origins": ["http://localhost:8000", "http://127.0.0.1:8000"],
#     "allow_headers": ["Content-Type", "Authorization"],
#     "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
# }})
CORS(app, resources={r"/api/*": {
    "origins": ["https://qatar-foundation-portal.onrender.com"],
    "allow_headers": ["Content-Type", "Authorization"],
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
}})


db.init_app(app)
jwt.init_app(app)

# Error Handlers
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"error": "Missing authorization token"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

app.register_blueprint(auth_bp)
app.register_blueprint(opp_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5000)