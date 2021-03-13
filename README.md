## A Full Implementation of a Blog page from Django girls
### Set up
1. Write Django==3.1.7 in requirements.tx
1. pip install -r requirements.tx

## Blog description
**Features of the blog: Nouns and Verbs**
*Nouns make Classes*
*Verbs make the methods*
## Post properties (columns in the Post table)
## Post
**---------**
1. title 
2. text - content 
3. author 
4. created_date
5. published_date
### methods for the blog
1. publish

## Register the *Post* model on the admin site
-- admin.site.register(Post)

## Pythonanywhere deployment procedures
1. Create an account and create an API token
2. Go to console and click on bash 
3. pip3.8 install --user pythonanywhere
4. $ pa_autoconfigure_django.py --python=3.8 https://github.com/<your-github-username>/my-first-blog.git

5. python manage.py createsuperuser

*pa_autoconfigure_django.py --python=3.8 https://github.com/sharhan-alhassan/django-girls.git*

## Django ORM and QuerySets
### How Django connects to the Database and stores data in it
1. QuerySet: A list of objects of a given Model. It allows you to read the data from the database, filter it and order it.
2. Use interactive **shell** to perform some queries by typing: `python manage.py shell` from the same directory as the `manage.py` file
3. Import models to work with on the shell
- `from blog.models import Post`
- `from django.contrib.auth.models import User`(this is to create an instance of Django owns User Model)
- `import timezone`
    - `from django.utils import timezone`
- `create a User object` 
    - `me = User.objects.get(username='admin')`
- `create a Post object`
    - `Post.objects.create(author=me, title='Second Article', text='A short story', published_date=timezone.now())`
- To publish a post, get an instance of it and use the `publish()` method on it
    - `post = Post.objects.create(author=me, title='Second Article', text='A short story', published_date=timezone.now())`
    - `post.publish()`
4. Filter objects: You can use `filter` instead of `all` to filter objects
*Eg:*
- `Post.objects.filter(author=me)`
- `Post.objects.filter(title__contains='article')`

5. Ordering Objects: We can order list objects. Let's try and order by `created_date`
    - `Post.objects.order_by('created_date')`
    **NB:**: You can order to see the latest post by adding **-** to the object `created_date` to become `-created_date`
6. Complex QuerySet: A combination of different QueruSets. 
    - `post = Post.objects.filter(published_date__lte=timezone.now()).ordery_by('-published_date')`
    *post therefore becomes the **variable** for the QuerySet*
7. To render a request into a template:

    - ```def index(request):
            post = Post.objects.filter(published_date__lte=timezone.now()).ordery_by('-published_date')
            return (request, 'blog/index.html', {'post': post})```

8. To display on the index.html, create the tags `{{ post }}}`
- **NB: `{{ post }}` will results as a list of objects in the form `<QuerySet [<Post: post title1>, <Post: post title 2>]`**
9. To solve this, call the list of items in a for loop
`{% for item in post% }`
    `{{ item }}`
  `{% endfor %}`