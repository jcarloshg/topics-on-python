# Steps to Create a Simple Django Project

1. **Install Python**

   - Django requires Python. This system already had Python 3.14.2 installed.

2. **Create and Activate Virtual Environment**

   - Create a virtual environment to manage project dependencies:
     ```bash
     python3 -m venv venv
     ```
   - No activation is needed if you always use `venv/bin/python` and `venv/bin/pip`.

3. **Install Django**

   - Install Django in the virtual environment:
     ```bash
     venv/bin/pip install django
     ```

4. **Create Django Project**

   - Create a new project named `myproject`:
     ```bash
     venv/bin/django-admin startproject myproject
     ```

5. **Create a Django App**

   - Create an app named `myapp`:
     ```bash
     venv/bin/python myproject/manage.py startapp myapp
     ```
   - If created in wrong place, move it into the project directory (`mv myapp myproject/`).

6. **Add App to INSTALLED_APPS**

   - Edit `myproject/myproject/settings.py` and add `'myapp',` to `INSTALLED_APPS`.

7. **Create a Basic View and URL**

   - In `myapp/views.py`, add:
     ```python
     from django.http import HttpResponse
     def index(request):
         return HttpResponse('Hello, this is my first Django app!')
     ```
   - In `myapp/urls.py`, add:
     ```python
     from django.urls import path
     from . import views
     urlpatterns = [
         path('', views.index, name='index'),
     ]
     ```
   - In `myproject/myproject/urls.py`, include your app's URLs:
     ```python
     from django.urls import path, include
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('myapp.urls')),
     ]
     ```

8. **Run Initial Migrations**

   - Apply the default migrations to set up the database:
     ```bash
     venv/bin/python myproject/manage.py migrate
     ```

9. **Run the Development Server**
   - Start the development server:
     ```bash
     venv/bin/python myproject/manage.py runserver
     ```
   - Visit http://127.0.0.1:8000/ to see your first Django app.

---

This file documents every step followed to create the basic Django project and app.
