from django.shortcuts import render, redirect
from .models import Blog, Message
from .forms import CommentForm
from django.core.paginator import Paginator

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
    
def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj' : page_obj,
    }

    return render(request, 'blog-list.html', context)