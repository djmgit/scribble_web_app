import datetime
from flask import Blueprint, jsonify, request
from flask import current_app as app
import json
import requests
from helpers.check_login import is_loggedin
from helpers.query_by_id import query_by_id

router = Blueprint('note_by_id', __name__)

@router.route('/note_by_id', methods=['POST'])
def add_note():
	response = ""

	try:
		data = request.get_json()
	except Exception as e:
		response = {"status": "data not found"}
		return jsonify(response)

	auth_token = request.headers.get('Authorization')
	if not auth_token or auth_token == "":
		response = {"status": "auth token not specified"}
		return jsonify(response)

	hasura_id = is_loggedin(auth_token)
	if not hasura_id:
		response = {"status": "User is not logged in. Please login first"}
		return jsonify(response)

	note_id = data.get('note_id')
	if not note_id:
		response = {"status": "note id not specified"}
		return jsonify(response)

	response = query_by_id(hasura_id, note_id)
	return jsonify(response)
