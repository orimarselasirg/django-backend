from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import UserSerializer
from users.models import User
import bcrypt

@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)
    if request.method == 'POST':
        users_serializer = UserSerializer(data= request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(users_serializer.errors, status = status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET','PUT', 'DELETE'])
def user_detail_api_view(request, id):
    user = User.objects.filter(pk = id).first()
    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        if request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(user_serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        if request.method == 'DELETE':
            user.delete()
            return Response({"status" : "deleted", "msg": "usuario eliminado"}, status=status.HTTP_200_OK)
    else:
        return Response({'status' : 'not found', 'msg' : 'el usuario no fue encontrado'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def user_login_api_view(request):
#     userdatabase = User.objects.filter(username=request.data['username']).first()
#     users_serializer = UserSerializer(userdatabase)
#     if userdatabase:
#         clave = request.data['password'].encode()
#         hashed = bcrypt(clave, bcrypt.gensalt())
#         # if bcrypt.checkpw(request.data['password'], users_serializer.data['password']):
#         if hashed == users_serializer.data['password']:
#             return Response({users_serializer.data['password'], request.data['password']})
    
        

        