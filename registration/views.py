from django.shortcuts import render,redirect,HttpResponseRedirect
from . import forms

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = forms.Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form.cleaned_data
            return render(request, 'registration/success.html', {'form': form})
    else:
        form = forms.Form()
    return render(request,'registration/Registration.html',{'form':form})
