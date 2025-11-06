from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import Profile
from django import forms


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
      model = User
      fields = ('username',  'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with this email already exists.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('A user with this username already exists.')
        return username


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class ProfileForm(forms.Form):
    role = forms.ChoiceField(choices=[('ST', 'Student'), ('TC', 'Teacher')])
    class_number = forms.IntegerField(max_value=11, min_value=1, widget=forms.TextInput(attrs={'placeholder': 'Class number'}), required=False)
    class_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Class name'}), required=False)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Birth Date'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Bio'}))
    hobbies = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Hobbies'}))
    interesting_facts = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'placeholder': 'Facts'}))

    class Meta:
        model = Profile
        fields = ('role',  'class_number', 'class_name', 'date_of_birth')
    
    def clean_class_number(self):
        role = self.cleaned_data.get('role')
        class_number = self.cleaned_data.get('class_number')
        if role == 'ST' and class_number is None:
            raise forms.ValidationError('Student must have class_number')
        return class_number
