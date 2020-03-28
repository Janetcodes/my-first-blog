#This is where we are importing or using a code already created
#by someone else so we dont have to copy paste
from django.conf import settings
from  django.db import models
from django.utils import timezone

#The line below defines our model (its an object)
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

#Below are the methods or action items we want our Model to have
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
