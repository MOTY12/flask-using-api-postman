from models.modules.core import app, req, request, os, secure_filename, url_for, jsonify
import datetime
from functools import wraps

def curl(config, payload):
    response = req.request(config['method'], config['url'], headers=config['headers'], data = payload)
    return response.json()
