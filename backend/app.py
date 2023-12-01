from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

@app.route("/api", methods=["GET"])
@cross_origin()
def hello():
    return {
    "backendtest": "Hello, World from the backend!"
    }

# serve index.html for React rendering
@app.route("/")
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, "index.html")


# catch 404 errors, allows us to refresh any main page and have it rendered
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")

if __name__ == 'main':
    app.run()
