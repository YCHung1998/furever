from rest_framework import serializers
from .models import Institution, Pet, Member
from .models import *


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class PetMemberRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetMemberRelationship
        fields = '__all__'
        ordering = ['-updated_at']

class InstitutionPetRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionPetRelationship
        fields = '__all__'
        ordering = ['-updated_at']


