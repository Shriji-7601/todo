from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.TextField()
    created_at = models.DateField()

    is_completed = models.BooleanField(default=False)
    # default is parameter false is arguement

class Profile(models.Model):
    title = models.CharField(max_length=30)
        #title attribute hi profile class ka
    profile_pic = models.ImageField(upload_to="profile_pic/")