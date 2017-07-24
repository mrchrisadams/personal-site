from flask import Flask, render_template
from flask_common import Common

app = Flask(__name__)
common = Common(app)

@app.route("/")
def index():
    return render_template('home_page.html')

if __name__ == "__main__":
    common.serve()
