from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import TodoTask
from .serializers import TodoTaskSerializer

# Create your views here.
class TodoTaskViewSet(viewsets.ModelViewSet):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer