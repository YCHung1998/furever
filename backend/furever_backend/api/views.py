from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models import Institution
from common.serializers import InstitutionSerializer


@api_view(['GET'])
def getData(request):
    institution = Institution.objects.all()
    serializer = InstitutionSerializer(institution, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDatas(request):
    institution = Institution.objects.all()
    serializer = InstitutionSerializer(institution, many=True)
    return Response(serializer.data)
