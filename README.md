# financial_project

Notes:
*** Views are like webpage responses, sometimes you want a file, sometimes you want a page
***Python manage.py migrate ENSURE TABLES ARE CREATED
***Python manage.py createsuperuser creates an administrator

1)	Django-admin startproject “name of project”.
2)	Move into first folder to where manage.py is.
3)	python manage.py runserver 127.0.0.1:8000
4)	python manage.py startapp “app_name”
5)	set up a view in new app
	a.	add this line of code from django.http import HttpResponse
	b.	add a function with a request input
	c.	use the new HttpResponse() function to return a string or html
6)	set up a urls.py inside of app
	a.	Add the following:
		from django.urls import path
		from . import views

		urlpatterns = [
			path('', views.”function inside of views.py”, name='index'),
		]
7)	Change urls.py in project folder
	a.	Add:
		Include from Django.urls and make reference to app and urls from app
8)	If you’d like to add fields, use models.py in app folder
	a.	Add classes here with appropriate models.Model and charfield/datetimefield
	b.	Use ForeignKey to determine focal point

Remember:
	•Change your models (in models.py).
	•Run python manage.py makemigrations to create migrations for those changes
	•Run python manage.py migrate to apply those changes to the database.

Commandline:
*** 