from .models import Institution#, Contact
from rest_framework import serializers

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'Institution'
        model = Institution
        fields = '__all__'

# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         db_table = 'Contact'
#         model = Contact
#         fields = '__all__'