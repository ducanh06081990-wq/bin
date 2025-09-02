from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Xin chào, đây là web Flask đầu tiên của bạn!"

if __name__ == "__main__":
    app.run(debug=True)
