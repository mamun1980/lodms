from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class LODMSAdminSite(AdminSite):
    # site_header = 'ভুমি অফিস ( দোয়ারা বাজার )'
    site_header = _("Land Office: Dowara Bazer")



admin_site = LODMSAdminSite(name='admin')
