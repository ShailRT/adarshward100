from django.shortcuts import render, redirect
from .models import Blog, Message
from .forms import CommentForm

def blog_detail(request, pk):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        f_message = request.POST['message']
        message = Message.objects.create(name=name, email=email, message=f_message, blog=blog)
        message.save()
        return redirect('blog-detail', pk)
    
    else:
        blog = Blog.objects.filter(slug=pk).first()
        similar_blogs = Blog.objects.all()[:2]
        context = {
            'blog': blog,
            'similar_blogs': similar_blogs,
        }
        return render(request, 'blog.html', context)
