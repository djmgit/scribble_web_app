import json
import requests
from flask import current_app as app

def delete_by_id(hasura_id, note_id):
	url = "https://data.accidentally14.hasura-app.io/v1/query"
	admin_token = app.config.get("admin_token")

	headers = {
		"Content-Type": "application/json",
		"Authorization": admin_token,
		"X-Hasura-Role": "admin"
	}

	requestPayload = {
		"type": "delete",
		"args": {
			"table": "notes",
			"where": {
				"note_id": {
					"$eq": note_id
				},
				"hasura_id": {
					"$eq": hasura_id
				}
			}
		}
	}

	resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

	response = ""
	if not resp.ok:
		response = {"status": "error", "data": resp.json()}
		return response

	if resp.json()["affected_rows"] == 0:
		response = {"status": "Data not found"}
		return response

	response = {"status": "ok", "data": resp.json()}
	return response
