from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()


    def __str__(self):
        return "%s %s" % (self.id, self.user)