from flask import Flask, render_template, request, redirect
from database import create_db, insert_url, get_url
import string
import random

def generate_short_code(length=4):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


app = Flask(__name__)
create_db()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        long_url = request.form.get("long_url")
        short_code = generate_short_code()

        insert_url(long_url, short_code)

        short_url = request.host_url + short_code
        return render_template("index.html", short_url=short_url)

    return render_template("index.html", short_url=None)

@app.route("/<short_code>")
def redirect_url(short_code):
    long_url = get_url(short_code)
    if long_url:
        return redirect(long_url)
    return "Invalid Short URL", 404

if __name__ == "__main__":
    app.run(debug=True)
