from django import forms


class CustomerEntry(forms.Form):
    gender=[('male','MALE'),('female','FEMALE')]
    lOCATION = [('HYD','Hyderabad'),('bgl','banglore'),('chennai','chennai'),('mum','mumbai')]
    firstname=forms.CharField(widget=forms.Textarea)
    lastname=forms.CharField(widget=forms.Textarea)
    mobilenumber=forms.IntegerField()
    GENDER = forms.CharField(widget=forms.Select(choices=gender))
    LOCATION = forms.CharField(widget=forms.Select(choices=lOCATION))
    Email = forms.CharField()
