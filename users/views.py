from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .api.serializer import UserSerializer

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request' : request})

        if login_serializer.is_valid():
            user =login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserSerializer(user)
                if created:
                    print(token)
                    print(user_serializer.user)
                    return Response({'token' : token.key, 'user' : user_serializer.data}, status=status.HTTP_202_ACCEPTED)
                else:
                    # metodo para borrar sesiones multiple de una usuario el hacer login
                    sessions = Session.objects.filter(expire_date__gte = datetime.now()) # todas las sesiones a partir del datetime.now()
                    if sessions.exists(): # valido si existe una sesion
                        for ses in sessions: # si hay sesion, recorro cada una de las sesiones
                            ses_data = ses.get_decoded() # decodifico las data de cada sesion
                            if user.id == int(ses_data.get('_auth_user_id')): # y valido si el id del usuario que hace el login es igual al id del ususario de la sesion que se recorre
                                ses.delete() # si es asi, se borra la sesion
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({'token' : token.key, 'user' : user_serializer.data}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'status': 'no activo', 'msg': 'el usuario no esta activo'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'status': 'error', 'msg': 'usuario o contraseña incorrecto'}, status = status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        print(token)
        token = Token.objects.filter(key = token).first()

        if token:
            user = token.user
            sessions = Session.objects.filter(expire_date__gte = datetime.now())
            if sessions.exists():
                for ses in sessions:
                    ses_data = ses.get_decoded()
                    if user.id == int(ses_data.get('_auth_user_id')):
                        ses.delete()
            token.delete()
            return Response({'status': 'session closed', 'msg' : 'sesion cerrada con exito'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'user not found', 'msg': 'error en autentiación'}, status=status.HTTP_401_UNAUTHORIZED)
