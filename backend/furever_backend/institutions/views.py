from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view # function method
from rest_framework.response import Response
from rest_framework.views import APIView # class method

from .models import Institution
from .serializers import InstitutionSerializer


@api_view(['GET', 'POST'])
def institutions_list(request):
    if request.method == 'GET':
        # get data list
        institution = Institution.objects.all()
        serializer = InstitutionSerializer(institution, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # add a data 
        serializer = InstitutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def institution_detail(request, id):
    try:
        institution = Institution.objects.get(id=id)
    except Institution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InstitutionSerializer(institution)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InstitutionSerializer(institution, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        institution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
class InstitutionList(APIView):
    def get(self, request):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data)

    def post(self):
        pass
