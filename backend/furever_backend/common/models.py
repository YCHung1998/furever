from django.db import models

# Create your models here.
class Institution(models.Model):
    # institution : contains detail information of the institution
    # id                        = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                      = models.CharField(max_length=50, unique=True)
    institution_intro         = models.CharField(max_length=150)


class Pet(models.Model):
    name = models.CharField(max_length=128)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=None)
    members = models.ManyToManyField("Member", related_name="attention_member", default=None)

class Member(models.Model):
    name = models.CharField(max_length=128)
    # age = models.IntegerField()
    # Identify_ID = models.CharField(max_length=10, unique=True)
    budget = models.IntegerField(
        default=0,
        help_text='The amount of money that the member can spend on pets'
    )

# # relationship between pet and member
# class PetMemberRelationship(models.Model):
#     pet = models.ForeignKey(Pet, on_delete=models.CASCADE, default=None)
#     member = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)
#     member_status = models.CharField(max_length=100) # subscribe adoption 申請

# # 機構抓狗的 刊登未刊登相關資料
# class InstitutionPetRelationship(models.Model):
#     institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=None)
#     pet = models.ForeignKey(Pet, on_delete=models.CASCADE, default=None)
#     pet_status = models.CharField(max_length=100) # publish , unpublish, adoption


class BigChart(models.Model): # similar to the membership
    # big chart : to record the big chart information
    sign_up_date = models.DateTimeField(auto_now_add=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=None)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, default=None)
    # pet = models.ManyToManyField(Pet, through='Pet', default=None)
    pet_status = models.CharField(max_length=100) # publish , unpublish, adoption
    # 紀錄會員對狗的關係
    member = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)
    # members = models.ManyToManyField(Member, through='Member', default=None)
    # 0: 關注中, 1: 申請領養(中), 3: 審核失敗 4: 審核成功 
    status = models.IntegerField(default=0)     


'''
python manage.py makemigrations common
python manage.py migrate common


python manage.py shell


from common.models import Institution, Pet, Member, BigChart

inst1 = Institution.objects.create(name='first shelter',
institution_intro='1st shelter')
inst2 = Institution.objects.create(name='second shelter',
institution_intro='2nd shelter')
inst3 = Institution.objects.create(name='third shelter',
institution_intro='3rd shelter')

pet1 = Pet.objects.create(name='first pet',institution=inst1)
pet2 = Pet.objects.create(name='second pet',institution=inst1)
pet3 = Pet.objects.create(name='third pet',institution=inst2)
pet4 = Pet.objects.create(name='forth pet',institution=inst2)
pet5 = Pet.objects.create(name='fifth pet',institution=inst2)
pet6 = Pet.objects.create(name='sixth pet',institution=inst3)

# filter form pet 獲得insti的狗隻 
Pet.objects.filter(institution=1)  # --> pet1 pet2

Pet.objects.filter(institution=2)  # --> pet3 pet4 pet5
Pet.objects.filter(institution=2).count() # --> 3

# 當機構登入狗隻就要放上bigchart狀態設置未刊登
bigchart1 = BigChart.objects.create(institution=inst1,pet=pet1,pet_status='unpublish', status=0, member=member1)
#
member1 = Member.objects.create(name='first member',budget=5000)
member2 = Member.objects.create(name='second member',budget=500)
member3 = Member.objects.create(name='third member',budget=10000)

'''