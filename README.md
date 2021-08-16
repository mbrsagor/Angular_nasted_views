# djangoStripe
> Django Stripe web application for online payment system.

#### Dependencies
###### Prerequisites

- Python 3.8
- Django 3.2.6
- MongoDB

The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

###### Please follow Steps:
````bash
`https://github.com/mbrsagor/djangoStripe.git
cd djangoStripe
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
````
After install requirements create `.env` file and pasts `.env-sample` file code

```bash
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
