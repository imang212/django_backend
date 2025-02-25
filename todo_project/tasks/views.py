from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer



#vrátím data GET
@api_view(['GET', 'POST'])
def Vrat_seznam_ukolu(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

#from django.http import HttpResponse
#from django.template import loader
#def members(request):
#  template = loader.get_template('main.html')
#  return HttpResponse(template.render())
from rest_framework import status

@api_view(['POST'])
def Vloz_ukol(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()  # Save the task
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created task with id
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)