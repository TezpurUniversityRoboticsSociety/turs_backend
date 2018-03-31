from django.shortcuts import render
from registration.models import Member

def index(request):
    return render(request,'home/home.html')

def member(request):
    members = Member.objects.filter(registered=True).filter(membership='Member')
    alumni = Member.objects.filter(registered=True).filter(membership='Alumni')
    return render(request,'home/members.html',{'members':members, 'alumni':alumni})