# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.db import models
from contacts.models import *


class Room(models.Model):
    room_no = models.CharField(max_length=100, primary_key=True, unique=True)
    room_name = models.CharField(max_length=100, null=True, blank=True)
    room_details = models.TextField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.room_no

    def __str__(self):
        return self.room_no

class Shelf(models.Model):
    shelf_no = models.CharField(max_length=100, primary_key=True, unique=True)
    shelf_details = models.TextField(max_length=200, null=True, blank=True)
    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.shelf_no

    def __str__(self):
        return self.shelf_no

class Rake(models.Model):
    rake_no = models.CharField(max_length=100, primary_key=True, unique=True)
    shelf = models.ForeignKey(Shelf, null=True, blank=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.rake_no

    def __str__(self):
        return self.rake_no

class Folder(models.Model):
    folder_no = models.CharField(max_length=100, primary_key=True, unique=True)
    rake = models.ForeignKey(Rake, null=True, blank=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.folder_no

    def __str__(self):
        return self.folder_no


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

class Case(models.Model):
    case_no = models.CharField(max_length=100, unique=True, verbose_name=_('case_no'))
    case_type = models.ForeignKey(CaseType, null=True, blank=True, on_delete=models.DO_NOTHING)
    # applicant = models.ForeignKey(Person, null=True, blank=True, related_name='case_applicant', on_delete=models.SET_NULL)
    # defendants = models.ManyToManyField(Person, null=True, blank=True, through='Defendants')
    # application_date = models.DateField(null=True, blank=True)
    status = models.ForeignKey(CaseStatus, null=True, blank=True, on_delete=models.DO_NOTHING)
    details = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _('case')
        verbose_name_plural = _('cases')
        permissions = (
            ('can_view_case', 'Can view case'),
        )


    def __str__(self):
        return self.case_no

    def __unicode__(self):
        return self.case_no

class File(models.Model):
    file_no = models.CharField(max_length=100, unique=True)
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.DO_NOTHING)
    rake = models.ForeignKey(Rake, null=True, blank=True, on_delete=models.DO_NOTHING)
    docs_location = models.CharField(max_length=200, null=True, blank=True)
    case = models.OneToOneField(Case, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='case_file')

    def __unicode__(self):
        return self.file_no

    def __str__(self):
        return self.file_no


class Applicant(models.Model):
    case = models.ForeignKey(Case, on_delete=models.DO_NOTHING, related_name='applicant_case')
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='case_applicant')

    def __unicode__(self):
        return self.case

    def __str__(self):
        return self.case

    class Meta:
        verbose_name = _('applicant')
        verbose_name_plural = _('applicantes')

class Defendent(models.Model):
    case = models.ForeignKey(Case, on_delete=models.DO_NOTHING, related_name='defendent_case')
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='case_defendent')

    def __unicode__(self):
        return self.case

    def __str__(self):
        return self.case

    class Meta:
        verbose_name = _('defendant')
        verbose_name_plural = _('defendants')
