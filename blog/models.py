from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    """ category = models.ForeignKey('blog.Category', on_delete=models.CASCADE) """

    def __unicode__(self):
            return self.title


""" class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.title """

class PersonalBlog(Blog):   # Inherits from Blog!
    user = models.ForeignKey(User, on_delete=models.CASCADE)