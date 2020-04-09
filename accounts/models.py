from django.db import models
from datetime import date

# Create your models here.
class Userip(models.Model):
    user_ip = models.TextField(null=True)
    date = models.DateField(default=date.today)
    class Meta:
        db_table = 'userip'


