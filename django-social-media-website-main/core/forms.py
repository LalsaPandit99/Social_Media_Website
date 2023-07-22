from django import forms
from .models import Article

class ArticleInformation(forms.From):
    article_title = forms.CharField(max_length=100, label='Article Title')
    article_description = forms.CharField(max_length=500, label='Article Description')
    is_public = forms.BooleanField(label='Is Article Publish?')
    password = forms.CharField(widget=forms.PasswordInput)
    