from django.db import models
from django.utils.translation import gettext_lazy as _

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
    description = models.TextField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.type_name

    def __str__(self):
        return self.type_name


class ClassOfLand(models.Model):
    """
        পতিত, আবাদি, অনাবাদি, জলাশয় ইত্যাদি
    """
    class_name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('class_name'))
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name=_('description'))

    def __unicode__(self):
        return self.class_name

    def __str__(self):
        return self.class_name


"""
    Does JL_No is unique for mouza?
"""

class Mouza(models.Model):
    """docstring for Mouza."""
    mouza_name = models.CharField(max_length=100, null=False, blank=False,  verbose_name=_('mouza_name'))
    jl_no = models.CharField(max_length=100, null=True, blank=True,  verbose_name=_('jl_no'))
    upazila = models.CharField(max_length=100, null=True, blank=True,  verbose_name=_('upazila'))

    class Meta:
        verbose_name = _('Mouza')
        verbose_name_plural = _('Mouzas')

    def __unicode__(self):
        return self.mouza_name

    def __str__(self):
        return self.mouza_name


class MouzaMeta(models.Model):
    """docstring for [object Object]."""
    mouja = models.ForeignKey(Mouza, null=True, blank=True, on_delete=models.SET_NULL)
    total_amount_of_land = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    non_settleable_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    settleable_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    surrendered_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    alluvion_diluvion = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    total_jolashoy = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_cultivation = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_hill = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_forest = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_unused = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

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
    plot_no = models.CharField(max_length=100, null=True, blank=True,  verbose_name=_('plot_no'))

    class Meta:
        verbose_name = _('Plot')
        verbose_name_plural = _('Plots')
        unique_together = ('mouza', 'plot_no',)

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
    total_amount_of_land = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    non_settleable_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    settleable_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    surrendered_land = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    alluvion_diluvion = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    total_jolashoy = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_cultivation = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_hill = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_forest = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_unused = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return self.plot

    def __str__(self):
        return str(self.plot)


'''
    একটি খতিয়ান কয়জনের নামে হইতে পারে?
    # খতিয়ানের ধরনঃ খাস খতিয়ান, এস,এ খতিয়ান, নামজারি খতিয়ান ইত্যাদি
    #
'''

class Khatiyan(models.Model):
    khatiyan_no = models.CharField(max_length=100, null=True, blank=True,  verbose_name=_('khatiyan_no'))
    mouza = models.ForeignKey(Mouza, null=True, blank=True, on_delete=models.SET_NULL)
    khatiyan_type = models.ForeignKey(KhatiyanType, null=True, blank=True, on_delete=models.SET_NULL)
    prepared_by = models.ForeignKey(Person, null=True, blank=True, related_name='khat_prepared_by', on_delete=models.SET_NULL)
    investigated_by = models.ForeignKey(Person, null=True, blank=True, related_name='khat_investigated_by', on_delete=models.SET_NULL)
    signed_date = models.DateField(auto_now=False, auto_now_add=False)
    remark = models.TextField(max_length=500, null=True, blank=True)
    # case_order_againset = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL)


    def __unicode__(self):
        return self.khatiyan_no

    def __str__(self):
        return self.khatiyan_no


class LandOwnerInfo(models.Model):
    """docstring for [object Object]."""
    khatiyan = models.ForeignKey(Khatiyan, null=True, blank=True, on_delete=models.SET_NULL)
    plot = models.ForeignKey(Plot, null=True, blank=True, on_delete=models.SET_NULL)
    amount_of_land = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    class_of_land = models.ForeignKey(ClassOfLand, null=True, blank=True, on_delete=models.SET_NULL)
    type_of_land = models.ForeignKey(TypeOfLand, null=True, blank=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.khatiyan + " / " + self.plot

    def __str__(self):
        return self.khatiyan + " / " + self.plot
