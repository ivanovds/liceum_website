from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    main_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Post text'}))

    class Meta:
        model = Post
        fields = ('main_text', 'image')
