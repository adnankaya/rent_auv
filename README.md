## Installations

```bash
# clone the project
git clone https://github.com/adnankaya/rent_uav.git
# go to project directory
cd rent_uav
# create venv instance named as env
python3.11 -m venv env
# for linux/macos users
source env/bin/activate
# for windows users
.\env\Scripts\activate
# install packages
pip install -r requirements.txt
# DOCKER
# docker-compose exec db
# psql -U developer postgres
# create database db_rent_uav;
# Migrate files
python manage.py migrate
# [Optional] make migrations if necessary
python manage.py makemigrations app-name
python manage.py migrate
# [DEVELOPMENT] init all command
python manage.py init_all
# run project for development mode
python manage.py runserver --settings=src.settings.dev
# run project for production mode
python manage.py runserver --settings=src.settings.prod
# run project for test mode
python manage.py runserver --settings=src.settings.settings_for_test
```
## Static Files
```
python manage.py collectstatic
```

## Internationalization
```
python manage.py makemessages -l tr --ignore=venv
python manage.py compilemessages
```

## Technical Notes

1. Find and remove migration files
```bash
find . -path "*/migrations/*.py" -not -path "./venv/*" -not -name "__init__.py" -delete
```