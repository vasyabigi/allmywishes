# How to get AllMyWishes project up? #

## Installation

We have to get up two servers:
+ Django backend
+ Yeoman frontend

### Django backend

#### Creating the environment
Create a virtual python environment for the project.

##### For virtualenvwrapper
```bash
mkvirtualenv allmywishes
```

#### Clone the code

```bash
git clone git@github.com:vasyabigi/allmywishes.git
```

#### Install requirements
```bash
cd backend
pip install -r reqs/dev.txt
```

#### Sync database
```bash
python manage.py syncdb
```

#### Apply database migrations
```bash
python manage.py migrate
```

### Yeoman frontend

#### Install requirements

+ Install [node.js](http://nodejs.org/)
+ Install [yeoman](http://yeoman.io/), grunt, bower with this command:
    `npm install -g yo grunt-cli bower`
+ Install [compass](http://compass-style.org/install/)
+ Go inside frontend by `cd frontend`
+ Install node.js dependencies by `npm install` (from package.json)
+ Install frontend dependencies by `bower install` (from bower.json)

### Running Django backend
Go to `backend` folder
```bash
python manage.py runserver
```

### Running Yeoman frontend
Go to `frontend` folder in separate terminal tab
```bash
grunt server
```

Open browser to http://127.0.0.1:9000/

Enjoy!
