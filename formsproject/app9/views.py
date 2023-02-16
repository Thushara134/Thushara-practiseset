from django.shortcuts import render
from app9 import forms


# Create your views here.

def customerregistrationview(request):
    form = forms.CustomerEntry()
    if request.method == 'POST':
        data = forms.CustomerEntry(request.POST)
        if data.is_valid():
            print('form is valid')
            print('FirstName',data.cleaned_data['firstname'])
            print('LastName',data.cleaned_data['lastname'])
            print('Mobilenumber',data.cleaned_data['Mobilenumber'])
    return render(request,'template/details.html',{'form':form})
