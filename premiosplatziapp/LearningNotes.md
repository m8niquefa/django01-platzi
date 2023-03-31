# Django Project

A project in django is a set of apps in django

This project will have several apps:

## Polls

Small apps to be reusable

# Commands
* ```python manage.py runserver```
* ```python manage.py startapp polls```
* ```python manage.py makemigrations polls``` Create the migrations from the Python classes
* ```python manage.py migrate``` 
* ```python manage.py shell``` Terminal with access to the project.


## Inside the Django Shell
* ```>>> Question.objects.all()```


# Django objects ORM Related

* Saving:
Just use save method ```object_instance.save()```. Example: ```
