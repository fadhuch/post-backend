from django.core.exceptions import RequestDataTooBig
from django.db import models
import uuid
from django.db.models.expressions import F
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.postgres.fields import ArrayField
from versatileimagefield.fields import VersatileImageField



# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128,default="")
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=128,)

class Comment(models.Model):
    post = models.ForeignKey("web.Post", on_delete=models.CASCADE)
    name = models.CharField(max_length=128,default="")
    comment = models.TextField()

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    heading = models.CharField(max_length=128)
    description = models.TextField()
    photo = VersatileImageField(upload_to='Post_image/',blank=True,null=True)
    no = models.IntegerField(default=1)

    def __str__(self):
        return self.heading

    def comments_count(self):
        return Comment.objects.filter(post=self).count()



class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)