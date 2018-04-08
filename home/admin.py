from django.contrib import admin
from .models import Timeline

admin.site.site_header = 'T.U.R.S. Web Administration'
# Register your models here.
admin.site.register(Timeline)