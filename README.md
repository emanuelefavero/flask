# Flask

This is a cheat sheet repo for [Flask](https://flask.palletsprojects.com/en/2.2.x/)

> Flask is a lightweight Python [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface?useskin=vector) (Web Server Gateway Interface) web application framework. It is similar to Express.js in Node.js

## Installation for both new projects and cloned repos

- Create a virtual environment

```bash
mkdir myproject
cd myproject
python3 -m venv venv
```

> use `py -3 -m venv venv` on Windows

- Activate the virtual environment

```bash
. venv/bin/activate
```

> use `venv\Scripts\activate` on Windows

- Install Flask

```bash
pip install Flask
```

## Quickstart

- Create a file called `app.py` with the following content:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

- Run the app

```bash
flask --app app run --debug
```

> To allow access to other devices on the network, use `--host=0.0.0.0`

## Pass variables

```python
...
def hello_name():
name = 'John'
return f"Hello {name}!"

```

## HTTP Methods

```python
# HTTP METHODS
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # DO THE LOGIN STUFF
        return "You are now logged in"
    else:
        # SHOW THE LOGIN FORM
        return "Please log in"
```

## URL Parameters

```python
# URL PARAMETERS
# specify the type using converters: <int:variable_name>
# converters: int, float, path, uuid
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"
```

## Static files

- Add a folder called static to the root of the project
- Add a file called `style.css` to the static folder
- Reference that file in the HTML

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
```

## Template Engine (Jinja2)

- Create a folder called `templates` in the root of the project
- Create a file called `index.html` in the templates folder
- Render the template in the view

```python
from flask import render_template

@app.route("/")
def index():
  name = "John"
    return render_template("index.html", title="Home", name=name)
```

## Link between pages

```html
<a href="{{ url_for('index') }}">Home</a>
```

> Note: `index` is the name of the view function

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface?useskin=vector)
- [Python](https://www.w3schools.com/python/)

## License

- [MIT](LICENSE.md)
