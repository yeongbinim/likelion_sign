from django.shortcuts import render,redirect, get_object_or_404
from .models import *
# views.py

def home(req):
    blog_objects = Blog.objects.all()
    return render(req, 'home.html', {'data': blog_objects})

def post_create(req):
    if req.method == 'POST':
        blog_object = Blog()
        blog_object.title = req.POST['title']
        blog_object.body = req.POST['body']
        blog_object.save()
        return redirect('/blog/'+str(blog_object.id))
    return render(req, 'post_create.html')

def post_read(req, id):
    blog_object = get_object_or_404(Blog, pk=id)
    comments = blog_object.comment_set.all()
    context = {
        'data' : blog_object,
        'comments' : comments,
    }
    # if req.method == 'POST':
    #     blog_object.comment_set.create(body = req.POST['comment'])
    return render(req, 'post_read.html', context)

def post_edit(req, id):
    blog_object = get_object_or_404(Blog, pk = id)
    if req.method == "POST":
        blog_object.title = req.POST['title']
        blog_object.body = req.POST['body']
        blog_object.save()
        return redirect('/blog/'+str(id))
    return render(req,'post_edit.html',{'data' : blog_object})


def comment_create(req,id):
    if req.method == 'POST':
        blog_object = get_object_or_404(Blog, pk = id)
        blog_object.comment_set.create(body = req.POST['comment'])
    return redirect('/blog/'+str(id))

def post_delete(req, id):
    blog_object = get_object_or_404(Blog, pk = id)
    blog_object.delete()
    return redirect('/')