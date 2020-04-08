from django.db import models
import datetime

# Create your models here.
class Userip(models.Model):
    user_ip = models.TextField(null=True)
    date  = models.DateTimeField(default=datetime.datetime.now)
    count = models.IntegerField(null=True)
    class Meta:
        db_table = 'userip'
