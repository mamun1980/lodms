from django.contrib.admin import AdminSite

class LODMSAdminSite(AdminSite):
    site_header = 'ভুমি অফিস ( দোয়ারা বাজার )'
    


admin_site = LODMSAdminSite(name='admin')
