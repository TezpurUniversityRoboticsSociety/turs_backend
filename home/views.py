from django.shortcuts import render
from registration.models import Member

def index(request):
    executive_prof = Member.objects.filter(registered=True).filter(membership='Executive Professor')
    executive_stud = Member.objects.filter(registered=True).filter(membership='Executive Member')
    return render(request,'home/home.html',{'executive_stud':executive_stud ,'executive_prof':executive_prof})

def member(request):
    members = Member.objects.filter(registered=True).filter(membership='Member')
    alumni = Member.objects.filter(registered=True).filter(membership='Alumni')
    return render(request,'home/members.html',{'members':members, 'alumni':alumni})