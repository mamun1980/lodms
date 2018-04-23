from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import path, include
from lodms.admin import admin_site
from django.contrib.admin.utils import unquote
from django.utils.safestring import mark_safe
# Register your models here.
from .models import *


class ViewDocsAdmin(admin.ModelAdmin):
    actions = ['view_docs']

    def view_docs(self, request, queryset):
        # import pdb; pdb.set_trace();
        return render(request,'admin/view_docs.html', context={})

    view_docs.short_description = "View Docs"


class FileDocsAdmin(admin.ModelAdmin):
    change_form_template = 'admin/file_docs_change_form.html'

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        response = super().changeform_view(
            request, object_id=object_id, form_url='', extra_context=extra_context,
        )
        obj = self.get_object(request, unquote(object_id))

        files = []
        try:
            import os

            media_path = '/Users/mamun/projects/python/lodms/media/'

            docs_location = obj.docs_location
            if docs_location:
                for file in os.listdir(media_path+docs_location):
                    files.append(docs_location+"/"+file)
            else:
                files = os.listdir(media_path)
        except Exception as e:
            pass

        response.context_data['docs'] = files

        return response


class FileAdmin(admin.ModelAdmin):
    def show_docs_count(self, obj):
        '''
        files = []
        try:
            import os

            media_path = '/Users/mamun/projects/python/lodms/media/'

            docs_location = obj.docs_location
            if docs_location:
                for file in os.listdir(media_path+docs_location):
                    files.append(docs_location+"/"+file)
            else:
                files = os.listdir(media_path)
        except Exception as e:
            pass

        return len(files)
        '''
        return 0

    # readonly_fields = ('file_no', 'case', )

    list_display = ('pk', 'file_no', 'view_docs',)
    # list_display_links = ('file_no', 'show_docs_count',)



class FileInline(admin.StackedInline):
    model = File
    fields = ('docs_location',)
    verbose_name = 'Doc location for file'
    max_num = 1


class CaseAdmin(admin.ModelAdmin):

    inlines = [
        FileInline,
    ]

    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super(CaseAdmin, self).changelist_view(request, extra_context=extra_context)

    def view_case(self, obj):
        # import pdb; pdb.set_trace()
        url = 'http://'
        url += self.request.get_host()
        url += self.request.get_full_path()
        url += str(obj.id)
        url += '/view/'
        return mark_safe('<a href="{src}" target="_blank">view</a>'.format( src=url ))

    def show_case_file(self, obj):

        try:
            loc = obj.case_file.docs_location

        except Exception as e:
            loc = 'No file exist'

        return loc

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('case_no',)
        return self.readonly_fields


    list_display = ('case_no', 'case_type', 'status', 'show_case_file', 'view_case')

    # def save_model(self, request, obj, form, change):
    #     import pdb; pdb.set_trace();
    #
    #     if not change:
    #         # loc = obj.replace('/', '-')
    #         try:
                # file = obj.case_file
                # file.file_no = obj.case_no
    #         except Exception as e:
    #             # file = File.objects.create(file_no=obj.case_no, docs_location=obj.case_no)
    #             # request.case_file = file
    #             # file.case = obj
    #             # file.save()
    #             pass
    #
    #     super().save_model(request, obj, form, change)


    # def save_related(self, request, form, formsets, change):
    #     super().save_related(request, form, formsets, change)



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
        # import pdb; pdb.set_trace()
        object_id = request.META['PATH_INFO'].strip('/').split('/')[-2]
        try:
            # object_id = int(object_id)
            case = self.model.objects.get(pk=object_id)

            case_file = case.case_file

            docs = []
            import os

            media_path = '/Users/mamun/projects/python/lodms/media/'
            docs_path = ''

            docs_location = case_file.docs_location

            if docs_location:
                docs_path = 'case_files/' + docs_location
            else:
                docs_path = 'case_files/%s/' % case.case_no

            directory = media_path+docs_path

            if not os.path.exists(directory):
                os.makedirs(directory)


            for doc in os.listdir(directory):
                if not os.path.isdir(doc):
                    docs.append(docs_path+"/"+doc)


            # self.admin_site.each_context(request)
            context = {
                'opts': self.model._meta,
                'case': case,
                'case_file': case_file,
                'docs': docs
            }

        except ValueError:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        return render(request, 'admin/case_details_view.html', context)
        # return HttpResponse('case details view page')


    def get_urls(self):
        # import pdb; pdb.set_trace()
        from django.conf.urls import include, url
        urls = super(CaseAdmin, self).get_urls()
        urls_new = [
            url(r'view/$', self.admin_site.admin_view(self.case_details_view), name='case_details_view')
        ]
        # urls = urls.append(detail_view_url)
        return  urls_new + urls




admin_site.register(Room)
admin_site.register(CaseStatus)
admin_site.register(CaseType)
admin_site.register(Case, CaseAdmin)
admin_site.register(File, FileAdmin)
admin_site.register(FileDocs, FileDocsAdmin)
