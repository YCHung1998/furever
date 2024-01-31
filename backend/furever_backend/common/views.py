from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view # function method
from rest_framework.response import Response
from rest_framework.views import APIView # class method

from .models import (Institution,
                    InstitutionExtension,
                    InstitutionPetRelationship)
from .models import (Pet, 
                    PetExtension,
                    PetMemberRelationship)
from .models import (Member,
                    MemberExtension)
from .serializers import (InstitutionSerializer,
                        PetSerializer,
                        MemberSerializer,
                        PetMemberRelationshipSerializer,
                        InstitutionPetRelationshipSerializer)


def _get_institution_by_id(institution_id):
    institution = Institution.objects.get(id=institution_id)
    return institution

def _institution_sign_up_pet(institution, pet, pet_status=0):
    #  0: unpublic, 1: public, 2: adoption
    # (i)nstitution (p)et (R)elationship
    ipR = InstitutionPetRelationship.objects.create(institution=institution,
                                                pet=pet,
                                                pet_status=pet_status
                                                )
    return ipR

# institution sign up the account
@api_view(['POST'])
def sign_up_institution(request):
    # given institution_info (name, institution_intro)
    # {
    #   "name": "DunnCY",
    #   "institution_intro": "Able actually source glass born itself without..."
    # }
    if request.method == 'POST':
        # add a data 
        serializer = InstitutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# institution sign up the pet
@api_view(['POST'])
def sign_up_pet_from_institution(request):
    # given pet_info (pet, petextension)
    # given pet_status (0: unpublic, 1: public, 2: adoption)
    # {
    # "pet_info":{
    #     "name": "John Myers",
    #     "institution": 2
    #     },
    # "pet_status":0
    # }
    if request.method == 'POST':
        name = request.data['pet_info']['name']
        institution = _get_institution_by_id(request.data['pet_info']['institution'])
        pet_status = request.data['pet_status']
        pet = Pet.objects.create(name=name,
                                institution=institution)
        ipR = _institution_sign_up_pet(pet=pet,
                                    institution=institution,
                                    pet_status=pet_status)
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
        institutionextention = InstitutionExtension.objects.get(id=id)
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