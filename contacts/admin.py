from django.contrib import admin
from lodms.admin import admin_site
from django.utils.safestring import mark_safe
# Register your models here.
from .models import *

class AddressAdmin(admin.ModelAdmin):
    list_display = ('person', 'house_no', 'village', 'address_type',)
    list_filter = ['address_type', 'person']
    search_fields = ['house_no', 'person__full_name']
admin_site.register(Address, AddressAdmin)


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('person', 'phone_number', 'phone_type',)
    list_filter = ['phone_type']
    search_fields = ['person__full_name', 'phone_number']
admin_site.register(Phone, PhoneAdmin)


class EmailAdmin(admin.ModelAdmin):
    list_display = ('person', 'email_id',)
    list_filter = ['person']
    search_fields = ['email_id', 'person__full_name']
admin_site.register(Email, EmailAdmin)


class AddressInline(admin.StackedInline):
    model = Address
    fields = (('house_no', 'village'), ('up_word_no', 'union'), ('upazila', 'zila'))
    # fieldsets = (
    #     ('Address1', {
    #         'fields': ('house_no', 'village',)
    #     },),
    #     ('Address2', {
    #         'fields': ('up_word_no', 'union', 'upazila', 'zila',)
    #     })
    # )
    verbose_name = 'Person Address'
    max_num = 2
    extra = 1

class PhoneInline(admin.TabularInline):
    model = Phone
    fields = ('phone_number', 'phone_type',)
    verbose_name = 'Person Address'
    extra = 1

class EmailInline(admin.TabularInline):
    model = Email
    fields = ('email_id',)
    verbose_name = 'Person Address'
    extra = 1
    max_num = 3

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
        PhoneInline,
        EmailInline
    ]

    def show_phone_numbers(self, obj):
        phones = ''
        for ph in obj.person_phone.all():
            phones += '<li>' + ph.phone_number + '</li>'

        if phones:
            return mark_safe(phones)
        else:
            return 'None'
        # return mark_safe('<a href="{src}" target="_blank">view</a>'.format( src=url ))


    list_display = ('full_name', 'fathers_name', 'mothers_name', 'nid', 'brn', 'sex', 'show_phone_numbers')
    list_filter = ['sex',]
    search_fields = ['full_name', 'fathers_name', 'mothers_name', 'nid', 'brn']

admin_site.register(Person, PersonAdmin)
