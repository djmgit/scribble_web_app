import json
import requests
from flask import current_app as app

def create_note(hasura_id, note_title, note_body, keywords, category):
	admin_token = app.config.get("admin_token")

	url = "https://data.accidentally14.hasura-app.io/v1/query"

	headers = {
    	"Content-Type": "application/json",
    	"Authorization": admin_token,
    	"X-Hasura-Role": "admin"
	}

	requestPayload = {
    	"type": "insert",
    	"args": {
        	"table": "notes",
        	"objects": [
            	{
                	"hasura_id": hasura_id,
                	"note_title": note_title,
                	"note_body": note_body,
                	"keywords": keywords,
                	"category": category
            	}
        	]
    	}
	}

	resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
	response = ""
	if not resp.ok:
		response = {"status": "error", "data": resp.json()}
	else:
		response = {"status": "ok", "data": resp.json()}

	return response
