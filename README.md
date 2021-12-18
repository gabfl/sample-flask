# sample-flask

[![Build Status](https://github.com/gabfl/sample-flask/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/gabfl/sample-flask/actions)

Flask basic example

## Installation

```bash
virtualenv venv
source venv/bin/activate
pip3 install Flask Flask-API
```

## Run the app

```bash
python app.py

or python app_api.py
```

## Usage

### App

Visit http://127.0.0.1:5000/

### API

```bash
$ curl -s http://127.0.0.1:5000/user/1 | beautify 
{
    "name": "Bob",
    "email": "bob@gmail.com"
}

$ curl -s http://127.0.0.1:5000/users | beautify 
[
    {
        "name": "Gab",
        "email": "gab@gmail.com"
    },
    {
        "name": "Bob",
        "email": "bob@gmail.com"
    },
    {
        "name": "Tom",
        "email": "tom@gmail.com"
    }
]
```