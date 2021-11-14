# 1. Create a virtual environment
- python3 -m venv . 

# 2. Navigate into the virtual env folder and execute the command below Mac
- source bin/activate
# 2. b. Windows
- .\Scripts\activate

# 3. Install django
- pip install django

# 4. Save installed packages in a requirements.txt file

- pip freeze > requirements.txt

# 5. Create src folder to hold all django files
- mkdir src
- cd src
# 6. Change into the src directory and create a django project 

- django-admin startproject nettyflix .
# 7. Start nettyflix app.
- python3 manage.py runserver
# 8. Create your first app
- python3 manage.py startapp videos

# 9. Add app to the installed_apps in settings folder

  ```python
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #own apps
    'videos',
]
  ```
# 10. Run migrations to create database table for video


> python3 manage.py makemigrations
> python3 manage.py migrate

# Add Video app to django admin backend 

```python
from django.contrib import admin
from .models import Video
# Register your models here.
admin.site.register(Video)
```







  









