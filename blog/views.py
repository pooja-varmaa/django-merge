import email
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from . import views
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})


def tag_detail(request, slug):
    tag =  Tag.objects.filter(slug=slug).last()
    post = Post.objects.filter(tag__name=tag).all()
    return render(request, 'blog/tag_detail.html', {'post': post})

def category_detail(request, slug):
    category = Category.objects.filter(slug=slug).last()
    post = Post.objects.filter(category__name=category)
    return render(request, 'blog/category_detail.html', {'post': post})

def post_detail(request,slug):
    post = Post.objects.filter(slug=slug).last()        
    comments = Comments.objects.filter(post=post,parent__isnull=True)
    if request.method == 'POST':        
       comment_form = CommentForm(request.POST)
       if comment_form.is_valid():
            parent_obj = None 
            parent_id  = None 
            parent_id = request.POST.get('reply_id')
            if parent_id:
                parent_obj = Comments.objects.get(id=parent_id)
                if parent_obj:
                    parent_comment = comment_form.save(commit=False)
                    parent_comment.parent = parent_obj

            new_comment = comment_form.save(commit=False)      
            new_comment.post = post
            new_comment.save()
            return redirect('blog:post_detail', slug=slug)
            # return redirect('blog:post_detail',pk=pk)   
    else:
        comment_form = CommentForm()
    return render(request,'blog/post_detail.html',{'post': post,'comments': comments,'comment_form': comment_form})
      
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        print(form,'before')
        if form.is_valid():
            user = form.save()   
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request=request,email=email, password=password)
            print(user,'after')
            login(request, user)
            return redirect('blog:post_list')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form,'before')
        if form.is_valid():
            email = form.cleaned_data['email']
            print(email,'email')
            password = form.cleaned_data['password']
            print(password,'password')
            user = authenticate(request=request,email=email, password=password)
            print(user,'eyiuriewuoiuoewiooio')
            if user:
                print(user,'after')
                login(request, user)
                return redirect('blog:post_list')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})		

def log_out(request):
     logout(request)
     return redirect('blog:post_list')

def add_category(request):
    if request.method == 'POSt':
         form = CategoryForm(request.POST)
         if form.is_valid():
             category = form.save(commit=False)
             category.save()
             return redirect('category_list')
    else:
         form = CategoryForm()
    return render(request, 'blog/add_category.html', {'form' : form})    

def user_profile(request,email):
       user = get_object_or_404(MyUser,email=email)    
       return render(request, 'blog/user_profile.html', {'user': user})


def profile_edit(request, email):
    user = get_object_or_404(MyUser, email=email) 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user=form.save()
            return redirect('blog:user_detail',email=email)
    else:
        form = ProfileForm(instance=user)
    return render(request, 'blog/profile_edit.html', {'form': form}) 
