from django import forms
from .models import Blog

class BlogForm(forms.Form):
  # 내가 입력받고자 하는 값을 입력
  title = forms.CharField()
  body = forms.CharField(widget=forms.Textarea)
  