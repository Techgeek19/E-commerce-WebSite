# E-commerce Website 

### Made with :heart_decoration: and :tea: 
:computer: [`Gaurav Mishra`](https://github.com/Techgeek19)

## Quick Setup

``` bash
$ virtualenv env

# Activate venv
$ source env/bin/activate

# Install requirements
$ pip3 install -r requirements.txt

# Create DB
'NAME': 'ecomm',
'USER': 'postgres',
'PASSWORD': 'gauravgaurav',
'HOST': 'localhost',

$ python manage.py makemigrations
$ python manage.py migrate

# Run Server (http://localhost:8000)
python3 manage.py runserver
```

