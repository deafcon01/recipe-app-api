# recipe-app-api
Recipe app api source code

#### To execute and start running 
``` python3
docker-compose run app sh -c "django-admin.py startproject app ."
```

#### To execute tests
```python3
docker-compose run app sh -c "python manage.py test && flake8"
