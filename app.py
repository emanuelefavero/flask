from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

username = ""


@app.route("/")
def index():
    global username
    return render_template("index.html", title="Home", name=username)


@app.route("/register", methods=["POST"])
def register():
    global username
    username = request.form.get("name")
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html", title="About")


# HTTP METHODS
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         # DO THE LOGIN STUFF
#         return "You are now logged in"
#     else:
#         # SHOW THE LOGIN FORM
#         return "Please log in"


# URL PARAMETERS
# specify the type using converters: <int:variable_name>
# converters: int, float, path, uuid
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"
