from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def add(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many = True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_person(request):
    if request.method == 'GET':
        person_id = request.data.get('person_id')
        try:
            person = Person.objects.get(pk=person_id)
            serializer = PersonSerializer(person)
            return Response(person)
        except Person.DoesNotExist:
            return Response(serializer.errors, "The person does not exist")
    

@api_view(['PUT', 'DELETE'])
def update(request, pk):
    if request.method == 'PUT':
        try:
            person = Person.objects.get(pk=pk)
        except:
            Person.DoesNotExist
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    if request.method == 'DELETE':
        person = Person.objects.get(pk=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








