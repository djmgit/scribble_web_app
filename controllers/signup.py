import datetime
from flask import Blueprint, jsonify, request
from flask import current_app as app
import json
import requests

router = Blueprint('signup_user', __name__)

@router.route('/signup', methods=['POST'])
def signup():
	response = ""
	url = "https://auth.accidentally14.hasura-app.io/v1/signup"

	try:
		data = request.get_json()
	except Exception as e:
		response = {"status": "data not found"}
		return jsonify(response)

	username = data.get("username")
	if not username or username == "":
		response = {"status": "username not found"}
		return jsonify(response)

	password = data.get("password")
	if not password or password == "":
		response = {"status": "password not found"}
		return jsonify(response)

	requestPayload = {
		"provider": "username",
		"data": {
			"username": username,
			"password": password
		}
	}

	headers = {
		"Content-Type": "application/json"
	}

	resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
	if not resp.ok:
		response = {"status": "Error", "data": resp.json()}
	else:
		response = {"status": "ok", "data": resp.json()}

	return jsonify(response)
