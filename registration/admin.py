from django.contrib import admin
from registration.models import Member
from django.http import HttpResponse
import csv

# Register your models here.

def exporttoCSV(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="members.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name','Roll no','Gender','Email ID','Phone no.','Transaction ID'])
    members = queryset.values_list('name','roll','gender','email','phone','transaction_id')
    for member in members:
        writer.writerow(member)
    return response
exporttoCSV.short_description = 'Export to CSV'

class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'transaction_id', 'registered']
    actions = [exporttoCSV]

admin.site.register(Member, MemberAdmin)
