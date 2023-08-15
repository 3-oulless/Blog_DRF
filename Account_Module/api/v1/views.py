from rest_framework import generics

from Account_Module.models import Profile, User
from .serializers import (RegistrationSerializer,
                          CustomAuthTokenSerializer,
                          CustomTokenObtainSerializer,
                          ChangePasswordSerializer,
                          ProfileSerializer)

from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView



class RegistrationApiView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):

        srz = self.serializer_class(data=request.data)

        if srz.is_valid():
            srz.save()
            data = {'email':srz.validated_data.get('email')}
            return Response(data,status=status.HTTP_201_CREATED)
        
        return Response(srz.errors,status=status.HTTP_400_BAD_REQUEST)
        

class CustomObtainAuthToken(ObtainAuthToken):

    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        srz = self.serializer_class(data=request.data,context={'request': request})
        srz.is_valid(raise_exception=True)
        user = srz.validated_data.get('user')
        token,created = Token.objects.get_or_create(user=user)

        return Response({
            'token' : token.key,
            'phone':user.phone,
            'email':user.email
        })

class CustomDiscardAuthToken(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


class ChangePasswordView(generics.GenericAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):

        user = request.user
        srz = self.serializer_class(data=request.data)

        srz.is_valid(raise_exception=True)

        if not user.check_password(srz.validated_data.get('password')):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(srz.validated_data.get('new_password'))
        user.save()
        return Response({
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'Password updated successfully',
            'data': []
        })
        
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset,user=self.request.user)
        return obj