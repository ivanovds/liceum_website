from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    

    class Meta:
        model = Profile
        fields = ('main_text', 'image')