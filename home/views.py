from django.shortcuts import render
from registration.models import Member

def index(request):
    executives = Member.objects.filter(registered=True).filter(membership='Executive Member')
    return render(request,'home/home.html',{'executives':executives})

def member(request):
    members = Member.objects.filter(registered=True).filter(membership='Member')
    alumni = Member.objects.filter(registered=True).filter(membership='Alumni')
    return render(request,'home/members.html',{'members':members, 'alumni':alumni})