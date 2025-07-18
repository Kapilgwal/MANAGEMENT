from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from authentication.serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Registration Success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data.get('user')
            return Response({'msg': 'Login Success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
