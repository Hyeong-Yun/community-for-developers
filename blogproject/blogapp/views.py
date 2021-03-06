from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm
from .forms import BlogModelForm

# Create your views here.
def home(request):
  return render(request, 'index.html')

# 블로그 작성 HTML을 보여 주는 함수
def new(request):
  return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
  if(request.method == "POST"):
    post = Blog()
    post.title = request.POST['title']
    post.body = request.POST['body']
    post.date = timezone.now()
    post.save()

  return redirect('home')
# django form을 이용해서 입력값을 받는 함수
# GET 요청 (=입력값을 받을 수 있는 Html을 갖다 줘야함)
# POST 요청 (= 입력한 내용을 데이터베이스에 저장)
# 둘 다 처리가 가능한  함수

def formcreate(request):
    if request.method == 'POST':
      #입력 내용을 DB에 저장 
      form = BlogForm(request.POST)
      if form.is_valid():
        post = Blog()
        post.title = form.cleaned_data['title']
        post.body = form.cleaned_data['body']
        post.save()
        return redirect('home')
    else:
      # 입력을 받을 수 있는 HTM을 갖다 주기
      form = BlogForm()
    return render(request,'form_create.html', {'form': form})

def modelformcreate(request):
  if request.method == 'POST':
      #입력 내용을 DB에 저장 
      form = BlogModelForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('home')
  else:
      # 입력을 받을 수 있는 HTM을 갖다 주기
      form = BlogModelForm()
  return render(request,'form_create.html', {'form': form})