from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

doc_bp = Blueprint('docs', __name__)

# Sample document storage
documents = []

@doc_bp.route('/documents', methods=['GET'])
@jwt_required()
def get_documents():
    return jsonify(documents), 200

@doc_bp.route('/documents', methods=['POST'])
@jwt_required()
def create_document():
    data = request.get_json()
    document = {
        'id': len(documents) + 1,
        'title': data['title'],
        'content': data['content']
    }
    documents.append(document)
    return jsonify(document), 201

@doc_bp.route('/documents/<int:doc_id>', methods=['GET'])
@jwt_required()
def get_document(doc_id):
    document = next((doc for doc in documents if doc['id'] == doc_id), None)
    if document:
        return jsonify(document), 200
    return jsonify({'message': 'Document not found'}), 404

@doc_bp.route('/documents/<int:doc_id>', methods=['PUT'])
@jwt_required()
def update_document(doc_id):
    data = request.get_json()
    document = next((doc for doc in documents if doc['id'] == doc_id), None)
    if document:
        document['title'] = data['title']
        document['content'] = data['content']
        return jsonify(document), 200
    return jsonify({'message': 'Document not found'}), 404

@doc_bp.route('/documents/<int:doc_id>', methods=['DELETE'])
@jwt_required()
def delete_document(doc_id):
    global documents
    documents = [doc for doc in documents if doc['id'] != doc_id]
    return jsonify({'message': 'Document deleted'}), 200
