import json
import requests

def is_loggedin(token):
	url = "https://auth.accidentally14.hasura-app.io/v1/user/info"

	headers = {
    	"Content-Type": "application/json",
    	"Authorization": "Bearer {}".format(token)
	}

	resp = requests.request("GET", url, headers=headers)
	resp = resp.json()

	return resp.get("hasura_id")
