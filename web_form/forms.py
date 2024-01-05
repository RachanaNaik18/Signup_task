from django import forms
from .models import user_form

class dj_form(forms.ModelForm):
    gen = (('Male','Male'), ('Female','Female'), ('Others','Others'))
    gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)

    c = (('Mumbai','Mumbai'), ('Dombivali','Dombivali'), ('Thane','Thane'), ('Bhandup','Bhandup'), ('Nashik','Nashik'))
    city = forms.ChoiceField(choices=c, widget=forms.Select)

    class Meta:
        model = user_form
        fields = '__all__'