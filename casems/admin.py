from lodms.admin import admin_site
from django.contrib import admin
from django.conf.urls import include, url
from django.shortcuts import render
import os
from django.conf import settings
# Register your models here.
from .models import *

class ViewDocsAdmin(admin.ModelAdmin):
    actions = ['view_docs']

    def view_docs(self, request, queryset):
        return render(request,'admin/view_docs.html', context={})

    view_docs.short_description = "View Docs"

# FileAdmin code ==============================
class FileAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super(FileAdmin, self).changelist_view(request, extra_context=extra_context)

    def view_docs(self, obj):
        url = 'http://'
        url += self.request.get_host()
        url += self.request.get_full_path()
        url += str(obj.id)
        url += '/view/'
        return mark_safe('<a href="{src}" target="_blank">view</a>'.format( src=url ))

    def file_details_view(self, request, extra_context=None):
        object_id = request.META['PATH_INFO'].strip('/').split('/')[-2]
        try:
            file = self.model.objects.get(pk=object_id)
            docs = []
            docs_path = ''
            docs_location = file.docs_location

            if docs_location:
                docs_path = 'case_files/' + docs_location
            else:
                docs_path = 'case_files/%s/' % case.case_no

            directory = settings.MEDIA_ROOT+ "/" + docs_path

            if not os.path.exists(directory):
                os.makedirs(directory)

            for doc in os.listdir(directory):
                if not os.path.isdir(doc):
                    docs.append(docs_path+"/"+doc)

            context = {
                'opts': self.model._meta,
                'case_file': file,
                'docs': docs
            }

        except ValueError:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        return render(request, 'admin/file_details_view.html', context)

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('case',)
        return self.readonly_fields

    def get_urls(self):
        urls = super(FileAdmin, self).get_urls()
        urls_new = [
            url(r'view/$', self.admin_site.admin_view(self.file_details_view), name='file_details_view')
        ]
        return  urls_new + urls

    list_filter = ['case__case_type', 'case__status']
    search_fields = ['file_no', 'case__case_type__name']
    list_display = ('file_no', 'case', 'rake', 'folder', 'docs_location', 'view_docs')

admin_site.register(File, FileAdmin)

# CaseAdmin code ==============================
class FileInline(admin.StackedInline):
    model = File
    fields = ('docs_location',)
    verbose_name = 'Doc location for file'
    max_num = 1

class CaseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ApplicantInline(admin.StackedInline):
    classes = ['col', 's6']
    model = Applicant
    max_num = 10
    extra = 1
    autocomplete_fields = ['person']


class DefendentInline(admin.StackedInline):
    classes = ['col', 's6']
    model = Defendent
    max_num = 10
    extra = 1
    autocomplete_fields = ['person']
    # formset = (
    #     ('class', ('col', 's6')),
    # )


class CaseAdmin(admin.ModelAdmin):

    # fieldsets = (
    #     ('Case', {
    #         'classes': ('col', 's6'),
    #         'fields': (('case_no', 'case_type', 'status'), 'details')
    #     }),
    #     ('Case Applicants & Defendents', {
    #         'classes': ('col', 's6'),
    #         'fields': ('ApplicantInline', 'DefendentInline')
    #     }),
    #     ('Case File', {
    #         'classes': ('col', 's6'),
    #         'fields': (
    #             'FileInline'
    #         ),
    #     }),
    # )

    inlines = [
        ApplicantInline, DefendentInline, FileInline,
    ]

    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super(CaseAdmin, self).changelist_view(request, extra_context=extra_context)

    def view_case(self, obj):
        url = 'http://'
        url += self.request.get_host()
        url += self.request.get_full_path()
        url += str(obj.id)
        url += '/view/'
        return mark_safe('<a href="{src}" target="_blank">view</a>'.format( src=url ))

    def show_case_file(self, obj):

        try:
            loc = obj.case_file

        except Exception as e:
            loc = 'No file exist'

        return loc

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('case_no',)
        return self.readonly_fields

    def save_formset(self, request, form, formset, change):
        obj = form.instance
        docs_loc = form.data['case_file-0-docs_location']

        if docs_loc == '':
            loc = obj.case_no
        else:
            loc = docs_loc

        if not change:
            try:
                file = obj.case_file
                file.file_no = obj.case_no
            except Exception as e:
                file = File.objects.create(file_no=obj.case_no, docs_location=loc, case=obj)

        formset.save()

    def case_details_view(self, request, extra_context=None):
        object_id = request.META['PATH_INFO'].strip('/').split('/')[-2]
        try:
            case = self.model.objects.get(pk=object_id)
            case_file = case.case_file
            docs = []
            docs_path = ''
            docs_location = case_file.docs_location

            if docs_location:
                docs_path = 'case_files/' + docs_location
            else:
                docs_path = 'case_files/%s/' % case.case_no

            directory = settings.MEDIA_ROOT + "/" + docs_path

            if not os.path.exists(directory):
                os.makedirs(directory)

            for doc in os.listdir(directory):
                if not os.path.isdir(doc):
                    docs.append(docs_path+"/"+doc)

            context = {
                'opts': self.model._meta,
                'case': case,
                'case_file': case_file,
                'docs': docs
            }

        except ValueError:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        return render(request, 'admin/case_details_view.html', context)

    def get_urls(self):
        urls = super(CaseAdmin, self).get_urls()
        urls_new = [
            url(r'view/$', self.admin_site.admin_view(self.case_details_view), name='case_details_view')
        ]
        return  urls_new + urls

    fields = (('case_no', 'case_type', 'status'), 'details')
    list_filter = ['case_type', 'status']
    search_fields = ['case_no',]
    list_display = ('case_no', 'case_type', 'status', 'show_case_file', 'view_case')



admin_site.register(CaseType, CaseTypeAdmin)
admin_site.register(Case, CaseAdmin)
admin_site.register(CaseStatus)

admin_site.register(Room)
admin_site.register(Shelf)
admin_site.register(Rake)
admin_site.register(Folder)
