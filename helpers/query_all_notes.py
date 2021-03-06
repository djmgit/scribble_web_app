import json
import requests
from flask import current_app as app

def query_all(hasura_id):
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
            	"note_title"
        	],
        	"where": {
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
	else:
		response = {"status": "ok", "data": resp.json()}

	return response
