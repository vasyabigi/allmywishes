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

### Yeoman backend

To be continued...
