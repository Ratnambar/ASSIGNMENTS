from xml.dom import ValidationErr
from django.db import models

# Create your models here.



class UploadImage(models.Model):

    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='accounts/', blank=True, null=True)


    