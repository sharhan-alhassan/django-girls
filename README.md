## A Full Implementation of a Blog page from Django girls
### Set up
1. Write Django==3.1.7 in requirements.tx
1. pip install -r requirements.tx

## Blog description
**Features of the blog: Nouns and Verbs**
*Nouns make Classes*
*Verbs make the methods*
## Post properties
**---------**
1. title 
2. text - content 
3. author 
4. created_date
5. published_date
### methods for the blog
1. publish

## Pythonanywhere deployment procedures
1. Create an account and create an API token
2. Go to console and click on bash 
3. pip3.8 install --user pythonanywhere
4. $ pa_autoconfigure_django.py --python=3.8 https://github.com/<your-github-username>/my-first-blog.git

5. python manage.py createsuperuser

pa_autoconfigure_django.py --python=3.8 https://github.com/sharhan-alhassan/django-girls.git