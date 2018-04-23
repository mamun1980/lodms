from django.db import models
from contacts.models import *
# Create your models here.

class KhatiyanType(models.Model):
    """
        নামজারি, খাস, এস,এ ইত্যাদি
    """
    type_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.type_name

    def __str__(self):
        return self.type_name

class TypeOfLand(models.Model):
    """
        খাস, রেকর্ডিয়, বন্দোবস্ত, অর্পিত ইত্যাদি
    """
    type_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TexField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.type_name

    def __str__(self):
        return self.type_name


class ClassOfLand(models.Model):
    """
        পতিত, আবাদি, অনাবাদি, জলাশয় ইত্যাদি
    """
    class_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TexField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.class_name

    def __str__(self):
        return self.class_name


"""
    Does JL_No is unique for mouza?
"""

class Mouza(models.Model):
    """docstring for Mouza."""
    mouza_name = models.CharField(max_length=100, null=False, blank=False)
    jl_no = models.CharField(max_length=100, null=True, blank=True)
    upazila = models.CharField(max_length=100, null=True, blank=True)
    total_amount_of_land = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return self.mouza_name

    def __str__(self):
        return self.mouza_name


class MoujaMeta(models.Model):
    """docstring for [object Object]."""
    mouja = models.ForeignKey(Mouza, null=True, blank=True, on_delete=models.SET_NULL)
    total_khas_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, editable=False)
    total_bondobosto_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_recorded_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_orpito_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return self.mouja

    def __str__(self):
        return self.mouja

"""
একটি দাগের জমি বিভিন্ন খতিয়ানে থাকতে পারে কিনা?
একই দাগের মধ্যে খাস, বন্দোবস্ত , রেকর্ডিয় জমি থাকতে পারে কিনা?
একই দাগের মধ্যে কৃষি, জলাভুমি, পতিত ইত্যাদি জমি থাকতে পারে কিনা?
"""

class Plot(models.Model):
    """docstring for Plot."""
    mouza = models.ForeignKey(Mouza, null=True, blank=True, on_delete=models.SET_NULL)
    plot_no = models.CharField(max_length=100, null=True, blank=True)
    total_amount_of_land  = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return self.plot_no

    def __str__(self):
        return self.plot_no

'''
    ভুমি কয় ধরনের হইতে পারে? ( খাস, রেকর্ড, অর্পিত, বন্দোবস্ত )
'''

class PlotMeta(models.Model):
    """docstring for [object Object]."""
    plot = models.ForeignKey(Plot, null=True, blank=True, on_delete=models.SET_NULL)
    total_khas_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_bondobosto_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_recorded_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_orpito_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return self.plot_no

    def __str__(self):
        return self.plot_no


'''
    একটি খতিয়ান কয়জনের নামে হইতে পারে?
    # খতিয়ানের ধরনঃ খাস খতিয়ান, এস,এ খতিয়ান, নামজারি খতিয়ান ইত্যাদি
    #
'''

class Khatiyan(models.Model):
    khatiyan_no = models.CharField(max_length=100, null=True, blank=True)
    mouza = models.ForeignKey(Mouza, null=True, blank=True, on_delete=models.SET_NULL)
    khatiyan_type = models.ForeignKey(KhatiyanType, null=True, blank=True, on_delete=models.SET_NULL)
    prepared_by = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL)
    investigated_by = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL)
    signed_date = models.DateField(auto_now=False, auto_now_add=False)
    remark = models.TexField(max_length=500, null=True, blank=True)
    # case_order_againset = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL)


    def __unicode__(self):
        return self.khatiyan_no

    def __str__(self):
        return self.khatiyan_no


class LandOwnerInfo(object):
    """docstring for [object Object]."""
    khatiyan = models.ForeignKey(Khatiyan, null=True, blank=True, on_delete=models.SET_NULL)
    plot = models.ForeignKey(Plot, null=True, blank=True, on_delete=models.SET_NULL)
    amount_of_land = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    class_of_land = models.ForeignKey(ClassOfLand, null=True, blank=True, on_delete=models.SET_NULL)
    type_of_land = models.ForeignKey(TypeOfLand, null=True, blank=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.khatiyan_no + " / " + self.plot

    def __str__(self):
        return self.khatiyan_no + " / " + self.plot
