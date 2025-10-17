from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template("index.html", message="Hello from Flask on AWS via CodePipeline!")

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
