# Flask

This is a cheat sheet repo for [Flask](https://flask.palletsprojects.com/en/2.2.x/)

> Flask is a lightweight Python [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface?useskin=vector) (Web Server Gateway Interface) web application framework. It is similar to Express.js in Node.js

## Installation for new projects

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

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface?useskin=vector)
- [Python](https://www.w3schools.com/python/)
