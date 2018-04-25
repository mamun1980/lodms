from django.db import models

# Create your models here.
class Room(models.Model):
    room_no = models.CharField(max_length=50, primary_key=True, unique=True)
    room_details = models.TextField(max_length=200, null=True, blank=True)
    # room_image = models.ImageField(upload_to='media', null=True, blank=True)

    def __unicode__(self):
        return self.room_no

    def __str__(self):
        return self.room_no



class CaseType(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class CaseStatus(models.Model):
    status = models.CharField(max_length=50, null=True, blank=True, unique=True)
    priority = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.status

    def __unicode__(self):
        return self.status



CASE_STATUS = (
    ('1', 'অসম্পুর্ন আবেদন'),
    ('2', 'শুনানির জন্য অপেক্ষমাণ'),
    ('3', 'শুনানি চলছে'),
    ('4', 'প্রতিবেদন দাখিল'),
)

class Case(models.Model):
    case_no = models.CharField(max_length=50, unique=True)
    case_type = models.ForeignKey(CaseType, null=True, blank=True, on_delete=models.SET_NULL)
    # applicant = models.ForeignKey(Person, null=True, blank=True, related_name='case_applicant', on_delete=models.SET_NULL)
    # defendants = models.ManyToManyField(Person, null=True, blank=True, through='Defendants')
    # application_date = models.DateField(null=True, blank=True, auto_now=False)
    # status = models.CharField(max_length=50, null=True, blank=True, choices=CASE_STATUS)
    status = models.ForeignKey(CaseStatus, null=True, blank=True, on_delete=models.DO_NOTHING)
    details = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        permissions = (
            ('can_view_case', 'Can view case'),
        )

    # def save(self, *args, **kwargs):
    #     import pdb; pdb.set_trace()
    #     super(Case, self).save(*args, **kwargs)
    #     print('saving Case model')
    #     pass

    def __str__(self):
        return self.case_no

    def __unicode__(self):
        return self.case_no


class File(models.Model):
    file_no = models.CharField(max_length=100, unique=True)
    docs_location = models.CharField(max_length=200, null=True, blank=True)
    case = models.OneToOneField(Case, null=True, blank=True, on_delete=models.SET_NULL, related_name='case_file')

    def __unicode__(self):
        return self.file_no

    def __str__(self):
        return self.file_no


    def view_docs(self):
        return 4


class FileDocs(File):
    class Meta:
        proxy = True
        verbose_name = 'File Doc'
        verbose_name_plural = 'File Docs'
