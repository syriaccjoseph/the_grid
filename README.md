# The Grid

A simple grid web-app to add products with category and sub category.

## Requirements

Python 3

## Installation

Make sure to make a python3 virtual environment and activate it.<br>

Install packages from requirements.txt:

```
pip install -r requirements.txt
```
Run migrations:
```
python manage.py makemigrations products
python manage.py migrate
```

## Load Test data
```
python manage.py loaddata fixtures/the_grid_testdata.json
```

## Run The Grid
```
python manage.py runserver
```
>Go to <localhost:8000/products>