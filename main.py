#!/usr/bin/env python3

import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from data import Data

app = Flask(__name__)
app.secret_key = str(os.urandom(16).hex())
api_data = Data()

# allow cross-origin
CORS(app, resources={
	r"/*": {
		"origins": "*"
	}
})


def check_body(required, body_json):
	"""Checks if all required JSON keys are in the given body."""
	return all(tag in body_json for tag in required)


@app.route('/', methods=['GET'])
def home():
	resp = jsonify({ 'message': 'Welcome!' })
	resp.status_code = 200
	return resp


@app.route('/banner', methods=['GET'])
def banner():
	resp = jsonify(api_data.get_banner())
	resp.status_code = 200
	return resp


@app.route('/about', methods=['GET'])
def about():
	resp = jsonify(api_data.get_about())
	resp.status_code = 200
	return resp


@app.route('/story', methods=['GET'])
def story():
	resp = jsonify(api_data.get_story())
	resp.status_code = 200
	return resp


@app.route('/projects', methods=['GET', 'POST'])
def projects():
	if request.method == 'POST':
		required = ("title", "github", "languages", "description")
		res = check_body(required, request.get_json())

		if res:
			api_data.add_project(request.get_json())

			resp = jsonify({ 'message': 'Successfully added project!' })
			resp.status_code = 200
			return resp
		else:
			resp = jsonify({ 'message': 'Required field(s) not present.' })
			resp.status_code = 404
			return resp

	resp = jsonify(api_data.get_projects())
	resp.status_code = 200
	return resp


@app.route('/experience', methods=['GET', 'POST'])
def experience():
	if request.method == 'POST':
		required = ("color", "startDate", "endDate", "title", "company", "description", "technologies")
		res = check_body(required, request.get_json())

		if res:
			api_data.add_experience(request.get_json())

			resp = jsonify({ 'message': 'Successfully added experience!' })
			resp.status_code = 200
			return resp
		else:
			resp = jsonify({ 'message': 'Required field(s) not present.' })
			resp.status_code = 404
			return resp

	resp = jsonify(api_data.get_experience())
	resp.status_code = 200
	return resp


@app.route('/education', methods=['GET', 'POST'])
def education():
	if request.method == 'POST':
		required = ("color", "startYear", "endYear", "title", "place", "description")
		res = check_body(required, request.get_json())

		if res:
			api_data.add_education(request.get_json())

			resp = jsonify({ 'message': 'Successfully added education!' })
			resp.status_code = 200
			return resp
		else:
			resp = jsonify({ 'message': 'Required field(s) not present.' })
			resp.status_code = 404
			return resp

	resp = jsonify(api_data.get_education())
	resp.status_code = 200
	return resp


if __name__ == "__main__":
	"""Run the Flask REST API server."""
	app.run(host='0.0.0.0')
