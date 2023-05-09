from flask import Flask, request, jsonify, abort, send_from_directory
import re
import os
from config import CONFIG as cfg

# Constants
ERR_AUTH = "You passed invalid access credentials."
ERR_REQ = "This service does only accept binary data. " \
          "Please also ensure that your key contains only alphanumeric characters or -, _, and ."
ERR_FILE_NOT_FOUND = "Couldn't find a file with this key."
ERR_FOLDER_NOT_FOUND = "Couldn't find the data folder."
ERR_INVALID_KEY = "You passed an invalid key."
MSG_STORE = "Your file was successfully stored."
MSG_DELETE = "Your file was successfully deleted."

# The Flask app
app = Flask(__name__)

'''
Ensure that the key has a sane format
'''
def _check_key(key):
    pattern = re.compile("^[a-zA-Z0-9-_\\.]+$")

    # Matches the pattern and prevent breaking out of the data folder
    return bool(pattern.match(key)) and ('..' not in key)




'''
A very simple authentication mechanism
'''
def _authenticated(headers):
    access_key = dict(headers).get("X-Access-Key")
    access_secret = dict(headers).get("X-Access-Secret")
    return access_key == cfg.get("access_key") and access_secret == cfg.get("access_secret")


'''
Store a file
'''
@app.route('/store/<key>', methods=['POST'])
def store(key):

    if not _authenticated(request.headers):
        abort(401, ERR_AUTH)

    if _check_key(key) and request.content_type == "application/octet-stream":
        data = request.get_data()
        f = open("{}/{}".format(cfg.get("data_folder"), key), "wb")
        f.write(data)
        f.close()
        return jsonify({"status": "success", "msg": MSG_STORE, "key": key})
    else:
        abort(400, ERR_REQ)

'''
Download a file
'''
@app.route('/retrieve/<key>', methods=['GET'])
def retrieve(key):
    if not _authenticated(request.headers):
        abort(401, ERR_AUTH)

    if not _check_key(key):
        abort(400, ERR_INVALID_KEY)

    file_path = "{}/{}".format(cfg.get("data_folder"), key)

    if not os.path.isfile(file_path):
        abort(404, ERR_FILE_NOT_FOUND)

    return send_from_directory(cfg.get("data_folder"),key)

'''
List all files
'''
@app.route('/list', methods=['GET'])
def list():
    if not _authenticated(request.headers):
        abort(401, ERR_AUTH)

    folder = cfg.get("data_folder")

    if not os.path.isdir(folder):
        abort(404, ERR_FOLDER_NOT_FOUND)

    return jsonify(os.listdir(folder))

'''
Delete a file
'''
@app.route('/delete/<key>', methods=['DELETE'])
def delete(key):
    if not _authenticated(request.headers):
        abort(401, ERR_AUTH)

    if not _check_key(key):
        abort(400, ERR_INVALID_KEY)

    file_path = "{}/{}".format(cfg.get("data_folder"), key)

    if os.path.isfile(file_path):
        os.remove(file_path)
        return jsonify({"status": "success", "msg": MSG_DELETE, "key": key})
    else:
        abort(404, ERR_FILE_NOT_FOUND)

if __name__ == "__main__":
    app.run(debug=True)
