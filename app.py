from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
