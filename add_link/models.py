from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Add_link (models.Model):
    username = models.ForeignKey(User(), on_delete=models.CASCADE)
    link_for = models.CharField(max_length=250)
    link = models.URLField(max_length=300)


    def __str__(self):
        return self.link_for