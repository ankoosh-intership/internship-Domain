from django.db import models

# Create your models here.
class DomainsModel(models.Model):

    it = models.URLField(max_length=16, unique=True)
    com = models.URLField(max_length=16, unique=True)
    eu = models.URLField(max_length=16, unique=True)
    net = models.URLField(max_length=16, unique=True)
    org = models.URLField(max_length=16, unique=True)
    info = models.URLField(max_length=16, unique=True)
    biz = models.URLField(max_length=16, unique=True)
