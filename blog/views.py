from django.shortcuts import render, redirect
from .models import Blog, Message
from .forms import CommentForm

def blog_detail(request, pk):
    blog = Blog.objects.filter(slug=pk).first()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        f_message = request.POST['message']
        message = Message.objects.create(name=name, email=email, message=f_message, blog=blog)
        message.save()
        return redirect('blog-detail', pk)
    
    else:
        context = {
            'blog': blog
        }
        return render(request, 'blog.html', context)
