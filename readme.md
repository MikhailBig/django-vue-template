VUE + DJANGO Template
===

## About
This template gives a fast forward integration of Vue framework within a Django app

## Install
### Frontend
After cloning this repository you will need to install Node modules in the `frontend` folder

        cd ./frontend
        npm install

### Django
Make some first-time setups for django project

        pip install -r requirements.txt
        python manage.py makemigrations
        python manage.py migrate

Do not forget to set `SECRET_KEY` in `django_project/settings.py` if it is not a fresh install

                SECRET_KEY = 'Your secret key here'

## Run
### Serve
For development in the root project folder just use

        python manage.py runserver

and in the `frontend` folder start

        npm run watch

### Docker
This repo is ready for docker assemble so

        sudo docker build -t django-vue .
        sudo docker run -p 8000:8000 django-vue
