from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Saravanan Nadanasabesan ECS Fargate!</h1><p>The deployment is successful.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
