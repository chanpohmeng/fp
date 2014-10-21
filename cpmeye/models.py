from django.db import models
from django.contrib.auth.models import User

class Submission(models.Model):
    title = models.CharField(max_length = 64, unique=True)
    content = models.CharField(max_length = 256)
    chancounter = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title
