from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

#  above is the many to many relationship test

class Member(models.Model):
    name = models.CharField(max_length=128)
    # age = models.IntegerField()
    # Identify_ID = models.CharField(max_length=10, unique=True)
    budget = models.IntegerField(
        default=0,
        help_text='The amount of money that the member can spend on pets'
    )    

    '''
    Member.objects.create(name='first member',
                            # age=20,
                            # Identify_ID='A123456789',
                            budget=5000)
    '''
    def __str__(self):
        return self.name
    
class MemberExtension(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=128)