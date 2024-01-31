from django.db import models
from institutions.models import Institution
# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=128)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=None)
'''
Pet.objects.create(name='first pet',
                    institution=Institution.objects.get(id=1))
                    # get the insti from first shelter by id
'''


class PetExtension(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE, default=None)