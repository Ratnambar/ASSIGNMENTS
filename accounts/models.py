from xml.dom import ValidationErr
from django.db import models

# Create your models here.



class UploadImage(models.Model):

    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='accounts/', blank=True, null=True)

    # def validate_image(image):
    #     filesize = image.file.size
    #     mb = 1
    #     if filesize > mb*1024:
    #         raise ValidationErr("Max file size 5mb")


    