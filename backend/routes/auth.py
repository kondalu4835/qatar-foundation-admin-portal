from flask import Blueprint, request, jsonify, current_app
from models import User
from extensions import db
import bcrypt
from flask_jwt_extended import create_access_token
from utils.token import generate_reset_token, verify_reset_token
import re
from datetime import timedelta

auth_bp = Blueprint('auth', __name__, url_prefix='/api')

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if not all([full_name, email, password, confirm_password]):
        return jsonify({"error": "All fields required"}), 400

    if not validate_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    if password != confirm_password:
        return jsonify({"error": "Passwords do not match"}), 400

    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Account already exists"}), 400

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(
        full_name=full_name,
        email=email,
        password=hashed_pw.decode('utf-8')
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Signup successful"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    remember_me = data.get('remember_me', False)

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({"error": "Invalid email or password"}), 401

    # Logic for Remember Me
    expires = timedelta(days=30) if remember_me else timedelta(hours=1)
    
    # identity is cast to string for JWT compatibility
    access_token = create_access_token(identity=str(user.id), expires_delta=expires)

    return jsonify({
        "token": access_token,
        "user": {
            "id": user.id,
            "name": user.full_name,
            "email": user.email
        }
    }), 200

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')
    user = User.query.filter_by(email=email).first()

    if user:
        token = generate_reset_token(email)
        # In production, you'd send this via email
        print(f"Reset link: http://localhost:8000/reset-password.html?token={token}")

    return jsonify({"message": "If this email exists, a reset link has been sent."})

@auth_bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    email = verify_reset_token(token)
    if not email:
        return jsonify({"error": "Invalid or expired token"}), 400

    data = request.json
    new_password = data.get('password')

    if len(new_password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    user = User.query.filter_by(email=email).first()
    hashed_pw = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    user.password = hashed_pw.decode('utf-8')

    db.session.commit()
    return jsonify({"message": "Password reset successful"})