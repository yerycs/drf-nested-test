from django.db import models
from django.contrib.auth.models import User

class Private_ID_Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = True
        db_table = 'private_id_info'
# Create your models here.
