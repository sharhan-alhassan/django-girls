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

### Notes about DateTimeField() parameters
- auto_now: will update every time you save the model. kind of like 
"Last modified" field  //good for updated_at
- auto_now_add: the default field will be current date which you cant change 
manually  //good for created_at
- default=timezone.now: same as auto_now_add but you can set the field manually on the model
and save
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

- ```
    def index(request):
            post = Post.objects.filter(published_date__lte=timezone.now()).ordery_by('-published_date')
            return (request, 'blog/index.html', {'post': post})
    ```

8. To display on the index.html, create the tags `{{ post }}}`
- **NB: `{{ post }}` will results as a list of objects in the form `<QuerySet [<Post: post title1>, <Post: post title 2>]`**

9. To solve this, call the list of items in a for loop
```
{% for item in post% }
    {{ item }}
  {% endfor %}
```
- |linebreaksbr pipe converts linebreaks to paragraphs

- 
10. The mysterious {% url 'post_detail' pk=post.pk %}
- `post_detail` part means Django will be expecting a URL in `blogs/url.py` with `name=post_detail`
- `pk=post.pk`: For each data in the database has a pk. `post.pk` access the primary key and set to a variable `pk`

## Django Forms
- Django's admin is cool to create forms, but it is rather hard to customize and make pretty. With forms we will have absolute power over our interface - we can do almost anything we can imagine
- We can either:
    - Define a form from scratch 
    - create a ModelForm which will save the result of the form to the model (in the database)
    - We will create a form for our **Post** model
- `class Meta:` tells Django which model should be used to create this form `(model = Post)`
- we can choose which fields to be field in the form. In this case, the form will have fields for `title` and `text`. `author` should be the person who is currently logged in (**You**)
- Next is use the form in a `view` and display it in a `template`
- Inside the `form tag`, insert the following 
    - `csrf_token` from security
    - `form.as_p` to render forms as paragraph
## How to handle form data
1. When data is inserted into the `title` and `text` fields of the form, they are in `request.POST`
2. In the `views.py` file we have two situations to handle:
    - When we access the page for the first and want the form fields to be blank
    - When we go back to the `views.py` with all the data that was inserted
3. An `if else` statement can handle those two situations
```
if request.method == "POST":
    [...]
else:
    form = PostForm() #set form to empty
```
- therefore `form = PostForm(request.POST)`
4. Next is to check if the form is correct with all required fields filled
    - This part is handled with `form.is_valid()`
    - We check if the form is valid, if it is then we can save it.
    The code becomes:
    ```
    if form.is_valid():
        post = form.save(commit-False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
    ```
    - An `author` and `published_date`is added because they were not included in the form but required since they in the `Post Model` in `models.py`
    - `commit=False`: Don't save yet, we want to add `autheor` and `published_date`
    - The form is finally save and to be `redirected` to the `detail` page
    - `form.save()`: Now save
    - Import `redirect` module from django.shortcuts and use it to render the new created post to the the `detail.html` page:
        - `return redirect('detail', pk=post.pk)`
        - pk=post.pk, where **post** is now the newly created post

## Security 
-  To prevent unauthorized people/people who did log in to perform any CRUD function, add the following the `anchor` tag of the Add post, edit, and delete:
```
{% if user.is_authenticated %}
{% endif %}
```