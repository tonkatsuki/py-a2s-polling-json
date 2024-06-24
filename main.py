from flask import Flask, jsonify, request
from flask_cors import CORS
import threading
import server_status

HOST = "0.0.0.0"
PORT = 5000

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def get_server_info():
    master_title = request.args.get("title", "servers")
    formatted_response = {master_title: server_status.server_info_cache}
    return jsonify(formatted_response)


if __name__ == "__main__":
    threading.Thread(target=server_status.update_server_info, daemon=True).start()
    app.run(host=HOST, port=PORT)
