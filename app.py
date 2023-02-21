from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    name = "John"
    # NOTE: variables should be escaped, Jinja2 does this automatically
    return f"<h1>Hello {name}</h1>"


# HTTP METHODS
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # DO THE LOGIN STUFF
        return "You are now logged in"
    else:
        # SHOW THE LOGIN FORM
        return "Please log in"
