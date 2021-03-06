from django.contrib import admin
from lodms.admin import admin_site
from django.utils.translation import gettext_lazy as _

from .models import *

# Register your models here.
# class KhatiyanTypeAdmin(admin.ModelAdmin):
    # pass
    # actions = ['view_docs']
    #
    # def view_docs(self, request, queryset):
    #     return render(request,'admin/view_docs.html', context={})
    #
    # view_docs.short_description = "View Docs"



admin_site.register(KhatiyanType)
admin_site.register(TypeOfLand)
admin_site.register(ClassOfLand)

class MouzaMetaInline(admin.StackedInline):
    model = MouzaMeta
    fields = ('non_settleable_land', 'settleable_land', 'surrendered_land',
                    'alluvion_diluvion', 'total_amount_of_land')
    # verbose_name = 'Doc location for file'
    max_num = 1

class MouzaAdmin(admin.ModelAdmin):

    def total_amount_of_land(self, obj):
        metas = obj.mouzameta_set.all()
        if metas:
            khas_land = metas[0].total_amount_of_land
        else:
            khas_land = 'তথ্য নাই!'
        return str(khas_land)

    def non_settleable_land(self, obj):
        metas = obj.mouzameta_set.all()
        if metas:
            khas_land = metas[0].non_settleable_land
        else:
            khas_land = 'তথ্য নাই!'
        return str(khas_land)

    def settleable_land(self, obj):
        metas = obj.mouzameta_set.all()
        if metas:
            khas_land = metas[0].settleable_land
        else:
            khas_land = 'তথ্য নাই!'
        return str(khas_land)

    def surrendered_land(self, obj):
        metas = obj.mouzameta_set.all()
        if metas:
            khas_land = metas[0].surrendered_land
        else:
            khas_land = 'তথ্য নাই!'
        return str(khas_land)

    def alluvion_diluvion(self, obj):
        metas = obj.mouzameta_set.all()
        if metas:
            khas_land = metas[0].alluvion_diluvion
        else:
            khas_land = 'তথ্য নাই!'
        return str(khas_land)


    inlines = [
        MouzaMetaInline,
    ]
    search_fields = ['mouza_name', 'jl_no']
    list_display = ('mouza_name', 'jl_no', 'upazila', 'non_settleable_land', 'settleable_land', 'surrendered_land',
                    'alluvion_diluvion', 'total_amount_of_land')

admin_site.register(Mouza, MouzaAdmin)
admin_site.register(MouzaMeta)


class PlotMetaInline(admin.StackedInline):
    model = PlotMeta
    fields = ('non_settleable_land', 'settleable_land', 'surrendered_land',
                    'alluvion_diluvion', 'total_amount_of_land')
    # verbose_name = 'Doc location for file'
    max_num = 1

# class PlotMetaAdmin(admin.ModelAdmin):
#     list_display = ['plot', 'total_khas_land', 'total_bondobosto_land', 'total_recorded_land',
#                     'total_orpito_land', 'total_amount_of_land']


class PlotAdmin(admin.ModelAdmin):

    def total_amount_of_land(self, obj):
        metas = obj.plotmeta_set.all()
        if metas:
            khas_land = metas[0].total_amount_of_land
        else:
            khas_land = 'তথ্য নাই!'
        return str(khas_land)

    def non_settleable_land(self, obj):
        metas = obj.plotmeta_set.all()
        if metas:
            khas_land = metas[0].non_settleable_land
        else:
            khas_land = 'তথ্য নাই!'
        return str(khas_land)

    def settleable_land(self, obj):
        metas = obj.plotmeta_set.all()
        if metas:
            khas_land = metas[0].settleable_land
        else:
            khas_land = 'তথ্য নাই!'
        return str(khas_land)

    def surrendered_land(self, obj):
        metas = obj.plotmeta_set.all()
        if metas:
            khas_land = metas[0].surrendered_land
        else:
            khas_land = 'তথ্য নাই!'
        return str(khas_land)

    def alluvion_diluvion(self, obj):
        metas = obj.plotmeta_set.all()
        if metas:
            khas_land = metas[0].alluvion_diluvion
        else:
            khas_land = 'তথ্য নাই!'
        return str(khas_land)


    inlines = [
        PlotMetaInline,
    ]

    list_filter = ['mouza',]
    search_fields = ['plot_no', 'mouza__mouza_name']
    list_display = ('plot_no', 'mouza', 'non_settleable_land', 'settleable_land', 'surrendered_land',
                    'alluvion_diluvion', 'total_amount_of_land')

admin_site.register(Plot, PlotAdmin)
# admin_site.register(PlotMeta, PlotMetaAdmin)
admin_site.register(Khatiyan)
admin_site.register(LandOwnerInfo)
