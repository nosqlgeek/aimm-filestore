from flask import Flask, request, jsonify, abort, send_from_directory
import re
import os
from config import CONFIG as cfg

# Constants
ERR_AUTH = "You passed invalid access credentials."
ERR_REQ = "This service does only accept binary data. " \
          "Please also ensure that your key contains only alphanumeric characters or -, _, and ."
ERR_NOT_FOUND = "Couldn't find a file with this key."
MSG_STORE = "Your file was successfully stored."
MSG_DELETE = "Your file was successfully deleted."

# The Flask app
app = Flask(__name__)

'''
Ensure that the key has a sane format
'''
def _check_key(key):
    pattern = re.compile("^[a-zA-Z0-9-_\\.]+$")
    return bool(pattern.match(key))


'''
A very simple authentication mechanism
'''
def _authenticated(access_key, access_secret):
    return access_key == cfg.get("access_key") and access_secret == cfg.get("access_secret")


'''
Store a file
'''
@app.route('/store/<key>', methods=['POST'])
def store(key):
    args = request.args
    if not _authenticated(args.get("access_key"), args.get("access_secret")):
        abort(401, ERR_AUTH)

    if _check_key(key) and request.content_type == "application/octet-stream":
        data = request.get_data()
        f = open("{}/{}".format(cfg.get("data_folder"), key), "wb")
        f.write(data)
        f.close()
        return jsonify({"status": "success", "msg": MSG_STORE, "key": key})
    else:
        abort(400, ERR_REQ)

@app.route('/retrieve/<key>', methods=['GET'])
def retrieve(key):
    args = request.args
    if not _authenticated(args.get("access_key"), args.get("access_secret")):
        abort(401, ERR_AUTH)

    file_path = "{}/{}".format(cfg.get("data_folder"), key)

    if not os.path.isfile(file_path):
        abort(404, ERR_NOT_FOUND)

    return send_from_directory(cfg.get("data_folder"),key)

@app.route('/delete/<key>', methods=['DELETE'])
def delete(key):
    args = request.args
    if not _authenticated(args.get("access_key"), args.get("access_secret")):
        abort(401, ERR_AUTH)

    file_path = "{}/{}".format(cfg.get("data_folder"), key)

    if os.path.isfile(file_path):
        os.remove(file_path)
        return jsonify({"status": "success", "msg": MSG_DELETE, "key": key})
    else:
        abort(404, ERR_NOT_FOUND)

if __name__ == "__main__":
    app.run(debug=True)
