from django import forms
from site1.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class MyRegistrationForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['first_name','last_name','email','username','password1']

    def clean_username(self):
        username= self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Username %s is already in use' % username)
        return username

class Comment(forms.ModelForm):
    class Meta:
        model = Post
        fields= ['text']