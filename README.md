# election
Election management system application for my university final semester project.  Here I'm teaching my friends and learning new logic. Which backend Django & Django Rest Framework and Mobile Application.

> N:B: I'm teaching my friends for university academic purposes making the web app.

### Prerequisites
###### Prerequisites

- Python 3.8.5
- Psql 13.0

The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

```bash
git clone https://github.com/mbrsagor/election.git
cd election
virtualenv venv --python=python3.8
source venv/bin/activate
```
Then create `.env` file and paste code from `example.env` file and add validate information.
###### After that run the server in development or production environment

##### Run development server:
```bash
python manage.py makemigrations app
python manage.py migrate app
python manage.py migrate
python manage.py runserver
```

* ALTER USER postgres with encrypted password 'postgres';

#### Deployment Ngnix configurations:
   - ``sudo nano /etc/nginx/sites-available/election``
   - ``sudo nginx -t && sudo systemctl restart nginx``