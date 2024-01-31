from django.db import models

# Create your models here.
import uuid
# from members.models import Member
# from pets.models import Pet

# class Contact(models.Model):
#     # contact method : contains 
#     # name, email, phone, address
#     id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name    = models.CharField(max_length=50, unique=True)
#     email   = models.EmailField(max_length=100)
#     phone   = models.CharField(max_length=20)
#     address = models.CharField(max_length=50)
#    class Meta:
#       abstract = True
#     def __str__(self):
#         return self.name

# institution class : to record the institution information
class Institution(models.Model):
    # institution : contains detail information of the institution
    # id                        = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                      = models.CharField(max_length=50, unique=True)
    institution_intro         = models.CharField(max_length=150)

    '''
    Institution.objects.create(name='first shelter',
                            institution_intro='this is the first shelter')
    '''
    def __str__(self):
        return self.name


class InstitutionExtension(models.Model):
    institution               = models.OneToOneField(Institution, on_delete=models.CASCADE, default=None)
    adopt_condition           = models.TextField()
    follow_up_quality         = models.TextField()
    support_service           = models.TextField()
    # contact                   = models.ForeignKey('Contact', on_delete=models.CASCADE, default=None)
    successful_adoption_case  = models.TextField()
    pets_location             = models.CharField(max_length=100)
    donation_account          = models.IntegerField()
    chip_conversion_assitance = models.BooleanField(default=False)
    dog_adoption_process      = models.TextField(default=None)
    cat_adoption_process      = models.TextField(default=None)


# blocklist class : to block the bad guy
# class Blocklist(models.Model):
#     insti_name = models.ForeignKey(Institution,
#                                     on_delete=models.CASCADE,
#     )
#     pet = models.OneToOneField(Pet,
#                                 on_delete=models.CASCADE,
#                                 default=None
#     ) # auto fetch id
#     blk_member = models.OneToOneField(Member, on_delete=models.CASCADE, default=None)
#     status = models.CharField(max_length=100) # publish , unpublish, adoption 
#     description = models.CharField(max_length=100)

#     def add_bad_guy(self, institution_id, member_id, pet_id, **args):
#         insti_name = Institution.objects.get(id=institution_id)
#         pet = Pet.objects.get(id=pet_id)
#         blk_member = Member.objects.get(id=member_id)
#         status = args['status']
#         description = args['description']
#         blocklist = Blocklist(insti_name=insti_name,
#                                 pet=pet,
#                                 blk_member=blk_member,
#                                 status=status,
#                                 description=description)
#         blocklist.save()

#         return None


# Create your models here.
class BigChart(models.Model): # similar to the membership
    # big chart : to record the big chart information
    from ..members.models import Member
    from ..pets.models import Pet
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=None)
    pet = models.ManyToManyField(Pet, through='Pets', default=None)
    pet_status = models.CharField(max_length=100) # publish , unpublish, adoption
    # 紀錄會員對狗的關係
    # members = models.ManyToManyField(Member, through='Members', default=None)
    # 0: 關注中, 1: 申請領養(中), 3: 審核失敗 4: 審核成功 
    status = models.IntegerField(default=0)     

    '''
    BigChart.objects.create(institution=Institution.objects.get(id=1),
                            pet=Pet.objects.get(id=1),
                            pet_status='unpublish')
                            ) 
    '''

    # member = models.ForeignKey('members.Member', on_delete=models.CASCADE, default=None)

if __name__ == '__main__':
    INSTITUTION_DATA = [{
    'name': 'first shelter',
    'institution_intro': 'this is the first shelter',
    'adopt_condition': 'this is the adopt condition',
    'follow_up_quality': 'this is the follow up quality',
    'support_service': 'this is the support service',
    # 'contact': Contact.objects.create(**CONTACT_DATA[0]),
    'successful_adoption_case':'this is the successful adoption case',
    'pets_location':'this is the pets location',
    'donation_account':'this is the donation account',
    'chip_conversion_assitance':'this is the chip conversion assitance',
    'dog_adoption_process':'this is the dog adoption process',
    'cat_adoption_process':'this is the cat adoption process',
    }]