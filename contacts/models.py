from django.db import models

# Create your models here.
SEX = (
    ('M', 'পুরুষ'),
    ('F', 'মহিলা'),
)

class Person(models.Model):
    full_name = models.CharField(max_length=200, null=False, blank=False)
    family_name = models.CharField(max_length=200, null=True, blank=True)
    fathers_name = models.CharField(max_length=200, null=True, blank=True)
    mothers_name = models.CharField(max_length=200, null=True, blank=True)
    spous_name = models.CharField(max_length=200, null=True, blank=True)
    nid = models.CharField(max_length=200, null=True, blank=True, unique=True)
    brn = models.CharField(max_length=200, null=True, blank=True, unique=True)
    # dob = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=50, null=True, blank=True, choices=SEX)

    # def show_phone_numbers(self):
    #     phones = ''
    #     for ph in self.person_phone.all():
    #         phones +=  ph.phone_number + '<br>'
    #
    #     if phones:
    #         return phones
    #     else:
    #         return 'None'

    def __unicode__(self):
        return self.full_name

    def __str__(self):
        return self.full_name


ADDRESS_TYPE = (
    ('P', 'স্থায়ী ঠিকানা'),
    ('C', 'বর্তমান ঠিকানা'),
)

class Address(models.Model):
    person = models.ForeignKey(Person, null=True, blank=True, related_name='person_address', on_delete=models.SET_NULL)
    address_type = models.CharField(max_length=50, null=True, blank=True, choices=ADDRESS_TYPE)
    house_no = models.CharField(max_length=200, null=True, blank=True)
    village = models.CharField(max_length=200, null=True, blank=True)
    postoffice = models.CharField(max_length=200, null=True, blank=True)
    up_word_no = models.CharField(max_length=200, null=True, blank=True)
    union = models.CharField(max_length=200, null=True, blank=True)
    upazila = models.CharField(max_length=200, null=True, blank=True)
    zila = models.CharField(max_length=200, null=True, blank=True)


    def __unicode__(self):
        return self.house_no

    def __str__(self):
        return self.house_no

PHONE_TYPE = (
    ('personal', 'personal'),
    ('office', 'office'),
    ('home', 'home'),
)

class Phone(models.Model):
    person = models.ForeignKey(Person, null=True, blank=True, related_name='person_phone', on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    phone_type = models.CharField(max_length=50, null=True, blank=True, choices=PHONE_TYPE)


    def __unicode__(self):
        return self.phone_number

    def __str__(self):
        return self.phone_number

class Email(models.Model):
    person = models.ForeignKey(Person, null=True, blank=True, related_name='person_email', on_delete=models.SET_NULL)
    email_id = models.CharField(max_length=150, null=True, blank=True)



    def __unicode__(self):
        return self.email_id

    def __str__(self):
        return self.email_id
