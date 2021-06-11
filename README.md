# T2G
<hr>
Sports team management application created with React, Flask, ElephantSQL and Firebase 
<hr>

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

<hr>

## General Info
This project is a React applilcation that consumes the data from a Flask backend API. The project files for the backend API and the React frontend are within this  repository.

<hr>

## Technologies
<strong>Frontend</strong>:
* firebase ^8.6.2
* react ^17.0.2
* react-dom ^17.0.2
* react-router-dom ^5.2.0
* react-scripts 4.0.3
* web-vitals ^1.0.1

<strong>Backend</strong>:
* alembic: 1.6.4
* click: 8.0.1
* Flask: 2.0.1
* Flask-HTTPAuth: 4.4.0
* Flask-Login: 0.5.0
* Flask-Migrate: 3.0.0
* Flask-SQLAlchemy: 2.5.1
* greenlet: 1.1.0
* gunicorn: 20.1.0
* itsdangerous: 2.0.1
* Jinja2: 3.0.1
* Mako: 1.1.4
* MarkupSafe: 2.0.1
* psycopg2-binary: 2.8.6
* python-dateutil: 2.8.1
* python-dotenv: 0.17.1
* python-editor: 1.0.4
* six: 1.16.0
* SQLAlchemy: 1.4.15
* Werkzeug: 2.0.1

<hr>

## Setup
To run the Flask API, clone the project files into your project folder, then perform the following:
```
$ cd ./api
$ touch .env
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ flask db stamp head
```

The Flask API is currently hosted on Heroku:
```
$ heroku login
$ heroku config -a=<heroku_app_name> -s
```

Copy the contents of the configutation variables in the output of your terminal to the .env file you created in the first step<br>
Next, in your .env file add a new line:
```
FLASK_ENV=development
```

<hr>

To run the React frontend, come out of the current directory, then into the frontend directory:
```
$ cd ../frontend
$ touch .env
$ npm install
```
For your configuration variables, log into the account associated with app and pull environmental variables from there in the .env file you created in the step above.

In one terminal
```
$ npm run start-api
```

In another terminal
```
$ npm start
```