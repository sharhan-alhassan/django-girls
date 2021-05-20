from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(max_length=150, unique=True, editable=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField()

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.title

    def get_absolute_urls(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)