from wsgiref.validate import validator
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import fields
from django.http import request
from accounts.models import UploadImage
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import  Serializer


class SignupSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ['username','email','password']
		extra_kwargs = {
			'password':{'write_only':True}
		}


	def validate_password(self,value):
		validate_password(value)
		return value


	def create(self,validate_data):
		user = get_user_model()(**validate_data)
		user.set_password(validate_data['password'])
		user.save()
		return user



class LoginSerializer(Serializer):
	username = serializers.CharField(required=True)
	password = serializers.CharField(required=True)



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ('name','image')


    def validate(self, validated_data):
        validated_data['size'] = validated_data['image'].size
        print(validated_data)
        if validated_data['size'] > 4*1024*1024:
            raise serializers.ValidationError("file is larger than 5 mb.")
        else:
            validated_data = {
                'name': validated_data['name'],
                'image': validated_data['image']
            }
        return validated_data
        

    def create(self, validated_data):
        return UploadImage.objects.create(**validated_data)

   


