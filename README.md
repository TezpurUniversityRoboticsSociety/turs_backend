# Backend of the T.U.R.S. site.


## Prerequisites:

* Python 3.4 +
* Django 1.9 +

---


## Run

Open the main directory
```
python manage.py runserver
```
The website is hosted to the localhost at port 8000 i.e (http://localhost:8000)

---


## Directory Structure

```
/turobotics
    +-- /home
    |    +-- /migrations
    |    +-- /static
    |    |    +-- /css
    |    |    +-- /fonts
    |    |    +-- /img
    |    |    +-- /js
    |    +-- /templates
    |    |    +-- /home
    |    |    +-- /registration
    |    |    +-- /blog
    |    __init__.py
    |    admin.py
    |    apps.py
    |    models.py
    |    tests.py
    |    urls.py
    |    views.py
    +-- /registration
    |   +-- /migrations
    |    __init__.py
    |    admin.py
    |    apps.py
    |    models.py
    |    forms.py
    |    tests.py
    |    urls.py
    |    views.py 
    +-- /blog
    |   +-- /migrations
    |    __init__.py
    |    admin.py
    |    apps.py
    |    models.py
    |    tests.py
    |    urls.py
    |    views.py       
    +-- /turobotics
    |    __init__.py
    |    settings.py
    |    urls.py
    |    wsgi.py
    db.sqlite3
    manage.py
```
---