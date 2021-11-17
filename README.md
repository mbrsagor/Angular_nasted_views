# election
Election funny full-stack web application which backend Django Rest Framework and Frontend React.JS


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
