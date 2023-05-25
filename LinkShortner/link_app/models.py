from django.db import models
from datetime import datetime
# Create your models here.
class Urls(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    website = models.URLField("website",blank=False,null=False)
    ids = models.TextField("ids",blank=False,null=False,unique=True)

    def __str__(self) -> str:
        return (self.website +"-----------------------"+ self.ids  )