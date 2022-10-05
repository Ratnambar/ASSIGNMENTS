
from dataclasses import field
from xml.dom import ValidationErr
from django import forms
from .models import UploadImage



class ImageForm(forms.ModelForm):

    limit = 1*1024
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('image')
        if pic is None:
            return None
        if len(pic)>self.limit:
            print("can't upload")

    class Meta:
        model = UploadImage
        fields = '__all__'

    # def validate_image(self):
    #     image = self.cleaned_data.get('image',False)
    #     if image:
    #         if image.size > 4*1024:
    #             raise ValidationErr("Image file is larger than 4 MB")
    #         return image
    #     else:
    #         raise ValidationErr("couldn't read uploaded file")
