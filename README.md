# Django-Wagtail
The WebApp is a simple website management web application provided by Django CMS. The application is one of the most popular CMS Wagtail.

> N:B: I'm teaching my friends for university academic purposes making the web app.

### Prerequisites
###### Prerequisites

- Python 3.8.5
- Psql 13.0

The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

```bash
git clone https://github.com/mbrsagor/webapp.git
cd webapp
virtualenv venv --python=python3.8
source venv/bin/activate
```

##### Run development server:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

###### Use Dockerfile for development:
```
docker compose build
docker compose up
```

* ALTER USER postgres with encrypted password 'postgres';

#### Deployment Ngnix configurations:
   - ``sudo nano /etc/nginx/sites-available/webapp``
   - ``sudo nginx -t && sudo systemctl restart nginx``
