from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.
def home(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blog, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail}) 

def create(request):
    if request.method == 'POST':
        post = Blog()
        post.title = request.POST['title']
        post.image = request.FILES['image']
        post.body = request.POST['body']
        post.pub_date = timezone.datetime.now()
        post.lat_lng = request.POST['lat_lng']
        post.save()
        return redirect('/blog/' + str(post.id))
    else:
        return render(request, 'update.html')

def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.image = request.FILES['image']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.lat_lng = request.POST['lat_lng']
        blog.isUpdated = True
        blog.save()
        return redirect('/blog/' + str(blog.id))
    else:
        return render(request, 'update.html', {'blog':blog})
    
def delete(request, pk):
    blog = Blog.objects.get(pk = pk)
    return render(request, 'sure.html', {'blog':blog})

def sure(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')