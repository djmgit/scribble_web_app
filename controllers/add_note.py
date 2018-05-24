import datetime
from flask import Blueprint, jsonify, request
from flask import current_app as app
import json
import requests
from helpers.check_login import is_loggedin
from helpers.create_note import create_note

router = Blueprint('add_note', __name__)

@router.route('/add_note', methods=['POST'])
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

	note_title = data.get('note_title')
	if not note_title:
		response = {"status": "note title not specified"}
		return jsonify(response)

	note_body = data.get("note_body")
	if not note_body:
		response = {"status": "note body not specified"}
		return jsonify(response)

	keywords = data.get("keywords")
	category = data.get("category")

	hasura_id = is_loggedin(auth_token)
	if not hasura_id:
		response = {"status": "User is not logged in. Please login first"}
		return jsonify(response)

	response = create_note(hasura_id, note_title, note_body, keywords, category)
	return jsonify(response)
