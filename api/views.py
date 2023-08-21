from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

class userAuth(APIView):
    
    def get(self, request):
        user = User.objects.all()
        serializers = UserSerializer(user, many=True)
        return Response(serializers.data)    

    def post(self, request):
        data = request.data
        email = data['email']
        user = User.objects.filter(email=email).first()
        if user is not None:
            return Response({
                'status' : False,
                'message' : 'Email is already in use.',
                'data' : {}
            })
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()           
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

