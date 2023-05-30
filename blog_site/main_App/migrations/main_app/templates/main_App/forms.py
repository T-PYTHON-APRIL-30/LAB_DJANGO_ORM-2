from django import forms
from models import post


class PostForm(forms.modelsForm):
    class Meta:
        model=post
        field=['title','content','is_published']
        