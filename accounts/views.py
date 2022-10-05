
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework import mixins, serializers, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.serializers import SignupSerializer, LoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes,api_view,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import *
from .models import *







class SignupViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
	permission_classes = [AllowAny]
	queryset = User.objects.all()
	serializer_class = SignupSerializer



class LoginView(APIView):
	permission_classes = [AllowAny]

	def post(self,request):
		serializer = LoginSerializer(data=request.data)
		if serializer.is_valid():
			try:
				user = User.objects.get(username=serializer.data['username'])
			except BaseException as e:
				raise ValidationError({"message":"user does not exist."})
			if user:
				if user.check_password(serializer.data['password']):
					token = Token.objects.get(user=user)
					return Response({'token':str(token)})
				return Response({"message":"incorrect password."})
			return Response({"message":"User does not exist."})
		return Response({'message':serializer.errors})


class ImageViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UploadImage.objects.all()
    serializer_class = ImageSerializer
   

    # def get(self, request, format=None):
    #     images = [image.image.size for image in UploadImage.objects.all()]
    #     print(images)
    #     return Response({"msg":images})

    # def post(self,request, format=None):
        
    #     serializer = ImageSerializer(data=request.data)
    #     if serializer.is_valid():
    #         print(serializer.data)
    #         serializer.save()
    #         return Response("image uploaded.")
    #     return Response("not uploaded.")


