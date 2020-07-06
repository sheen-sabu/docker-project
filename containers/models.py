from django.db import models


class Container(models.Model):
    container_name = models.CharField(max_length=200)
    container_id = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
