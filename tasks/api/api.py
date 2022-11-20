from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import TaskSerializer
from users.api.serializer import UserSerializer
from tasks.models import Task
from users.models import User

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def task_api_view(request, id):
    if request.method == 'GET':
        try:
            user = User.objects.filter(id=id)
            if user:
                tasks = Task.objects.filter(user=id)
                task_serializer = TaskSerializer(tasks, many=True)

                if tasks :
                    return Response(task_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({'status' : 'sin tareas', 'msg': 'el usuario no tiene tarea'}, status=status.HTTP_404_NOT_FOUND)
            else:
                print({
                    'status': 'usuario no encontrado',
                    'msg': 'el id del usuario no existe',
                    'path': 'api_view_task'
            })
                return Response({'status: usuario no encontrado o no existe'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            print({
                'status': 'error',
                'msg': 'la peticion presenta una error',
                'path': 'api_view_task'
            })
            return Response({'status': 'error', 'msg':'hay un error en la peticion'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        task = Task.objects.get(id = id)
        task_serializer = TaskSerializer(task, data= request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data)
    if request.method == 'PATCH':
        task = Task.objects.get(id = id)
        task_serializer = TaskSerializer(task, data= request.data, partial=True)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data)
    if request.method == 'DELETE':
        print('llegue')
        task = Task.objects.get(id = id)
        task.delete()
        return Response({'status': 'tarea borrada', 'msg': 'su tarea ha sido borrada'})

@api_view(['POST'])        
def task_api_view_creator(request):
    if request.method =='POST':
        try:
            task_serializer = TaskSerializer(data = request.data)
            if task_serializer.is_valid():
                task_serializer.save()
                return Response(task_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(task_serializer.errors, status = status.HTTP_406_NOT_ACCEPTABLE)
        except:
            print({
                'status': 'error',
                'msg': 'la peticion presenta una error',
                'path': 'api_view_task'
            })
        return Response({'status': 'error', 'msg':'hay un error en la peticion'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def task_api_view_search(request, task):
    if request.method == 'GET':
        try:
            tasks = Task.objects.filter(task__icontains= task)
            task_serializer = TaskSerializer(tasks, many=True)
            return Response(task_serializer.data, status=status.HTTP_201_CREATED)
        except:
            print({
                'status': 'error',
                'msg': 'la peticion presenta una error',
                'path': 'api_view_task_search'
            })
            return Response({'status': 'error', 'msg':'hay un error en la peticion'}, status=status.HTTP_400_BAD_REQUEST)