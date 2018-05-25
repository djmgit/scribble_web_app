import json
import requests
from flask import current_app as app

def search_notes(hasura_id, search_data, fields):
	url = "https://data.accidentally14.hasura-app.io/v1/query"
	admin_token = app.config.get("admin_token")

	headers = {
		"Content-Type": "application/json",
		"Authorization": admin_token,
		"X-Hasura-Role": "admin"
	}

	requestPayload = {
		"type": "select",
		"args": {
			"table": "notes",
			"columns": [
				"note_id",
				"note_title",
				"note_body",
				"keywords",
				"category"
			],
			"where": {
				"hasura_id": {
					"$eq": hasura_id
				}
			}
		}
	}

	resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

	if not resp.ok:
		response = {"status": "error", "data": resp.json()}
		return response

	data = resp.json()

	if len(data) == 0:
		response = {"status": "no data found"}
		return response

	filtered_data = []

	for obj in data:
		if "note_title" in fields and search_data.lower() in obj.get("note_title").lower():
			filtered_data.append(obj)
			continue

		if "note_body" in fields and search_data.lower() in obj.get("note_body").lower():
			filtered_data.append(obj)
			continue

		if "keywords" in fields and obj.get("keywords") and search_data.lower() in obj.get("keywords").lower():
			filtered_data.append(obj)
			continue

		if "category" in fields and obj.get("category") and search_data.lower() in obj.get("category").lower():
			filtered_data.append(obj)
			continue

	response = {"status": "ok", "data": filtered_data}

	return response
