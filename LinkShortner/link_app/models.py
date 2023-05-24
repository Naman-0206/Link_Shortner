from django.db import models

# Create your models here.
class Urls(models.Model):
    website = models.URLField("website",blank=False,null=False)
    ids = models.TextField("ids",blank=False,null=False,unique=True)