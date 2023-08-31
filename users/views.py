from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializer import *
import jwt,datetime
from Buscador.settings import LOC

# Create your views here.
@api_view(['GET', 'POST'])
def userRegister(request):
    if request.method=="POST":
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET','POST'])
def userLogin(request):
    if request.method=="POST":
        us = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=us).first()

        if user is None:
            raise AuthenticationFailed('Credenciales invalidas')

        if not user.check_password(password):
            raise AuthenticationFailed('Credenciales invalidas')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, LOC, algorithm='HS256')
        response=Response()
        response.set_cookie(key='CRTF', value=token, httponly=True)


        return Response({"token":token})

class LogoutView(APIView):

    def post(self,request):
        response= Response()
        response.delete_cookie('jwt')
        response.data= {
            'message': 'pasado'
        }
        return response

class refresh(APIView):
    def get(self,request):

        token = request.COOKIES.get('CRFT')

        if not token:
            raise AuthenticationFailed('No existe sesion')

        try:
            payload = jwt.decode(token, LOC, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion Cerrada')


        payload = {
            'id': payload['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, LOC, algorithm='HS256')


        return Response({
            'CTRF': token
        })