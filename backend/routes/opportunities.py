from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Opportunity
from extensions import db

opp_bp = Blueprint('opportunities', __name__, url_prefix='/api/opportunities')


# GET ALL
@opp_bp.route('', methods=['GET'])
@jwt_required()
def get_opportunities():
    user_id = get_jwt_identity()
    opps = Opportunity.query.filter_by(user_id=user_id).all()

    result = []
    for o in opps:
        result.append({
            "id": o.id,
            "name": o.name,
            "duration": o.duration,
            "start_date": o.start_date,
            "description": o.description,
            "skills": o.skills,
            "category": o.category,
            "future_opportunities": o.future_opportunities,
            "max_applicants": o.max_applicants
        })

    return jsonify(result)


# CREATE
@opp_bp.route('', methods=['POST'])
@jwt_required()
def create_opportunity():
    user_id = get_jwt_identity()
    data = request.json

    required_fields = ['name', 'duration', 'start_date', 'description', 'skills', 'category', 'future_opportunities']

    if not all(field in data and data[field] for field in required_fields):
        return jsonify({"error": "All required fields must be filled"}), 400

    new_opp = Opportunity(
        user_id=user_id,
        name=data['name'],
        duration=data['duration'],
        start_date=data['start_date'],
        description=data['description'],
        skills=data['skills'],
        category=data['category'],
        future_opportunities=data['future_opportunities'],
        max_applicants=data.get('max_applicants')
    )

    db.session.add(new_opp)
    db.session.commit()

    return jsonify({"message": "Opportunity created"}), 201


# GET SINGLE
@opp_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_one(id):
    user_id = get_jwt_identity()
    opp = Opportunity.query.filter_by(id=id, user_id=user_id).first()

    if not opp:
        return jsonify({"error": "Not found"}), 404

    return jsonify(vars(opp))


# UPDATE
@opp_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    user_id = get_jwt_identity()
    opp = Opportunity.query.filter_by(id=id, user_id=user_id).first()

    if not opp:
        return jsonify({"error": "Not found"}), 404

    data = request.json

    for key in data:
        setattr(opp, key, data[key])

    db.session.commit()

    return jsonify({"message": "Updated successfully"})


# DELETE
@opp_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    user_id = get_jwt_identity()
    opp = Opportunity.query.filter_by(id=id, user_id=user_id).first()

    if not opp:
        return jsonify({"error": "Not found"}), 404

    db.session.delete(opp)
    db.session.commit()

    return jsonify({"message": "Deleted successfully"})
