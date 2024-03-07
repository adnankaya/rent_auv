# DEMO

[[Demo Video on Youtube]](https://www.youtube.com/watch?v=mNpaSMKYQHM)

## Installations

```bash
# clone the project
git clone https://github.com/adnankaya/rent_uav.git
# go to project directory
cd rent_uav
cp .env.example .env
docker-compose up -d --build
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