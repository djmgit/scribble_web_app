import datetime
from flask import Blueprint, jsonify, request
from flask import current_app as app
import json
import requests
from helpers.check_login import is_loggedin
from helpers.search_notes import search_notes

router = Blueprint('note_search', __name__)

@router.route('/note_search', methods=['POST'])
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

	search_data = data.get("search")
	if not search_data:
		response = {"status": "Search data is not specified"}
		return jsonify(response)

	fields = data.get("fields")
	print (fields)
	if not fields:
		fields = ['note_title', 'note_body', 'keywords', 'category']

	response = search_notes(hasura_id, search_data, fields)
	return jsonify(response)
