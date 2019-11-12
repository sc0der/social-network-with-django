from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from subject.models import Subject
from django.contrib import messages
from .models import Savolho
from subject.models import Subject
from answers.models import Comment
from answers.forms import CommentForm
from .forms import SavolForm, SavolEditForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.views.generic import ListView, DetailView, UpdateView, DeleteView
# Create your views here.

# определение вывода все информации
def PostList(request):
    comment = Comment.objects.all()
    subject = Subject.objects.all()
    post = Savolho.objects.all()
    context = {'post':post, 'subject':subject, 'comment':comment}
    return render (request, 'questions/index.html', context)

# опредление для вывода комментов и детальную информацию
def PostDetail(request, post):
    this_post = get_object_or_404(Savolho, slug=post)
    comments = this_post.comment_set.filter(approved_comment=True)
    new_comment = None
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = this_post
        # parent_object = None
        # try:
        #     parent_id = int(request.POST.get("parent_id"))
        # except:
        #     parent_id = None 
        # if parent_id:
        #      parent_qs = Comment.objects.filter(id=parent_id)
        #     #  parent_qs.author = request.user
        #      if parent_qs.exists():
        #          parent_object = parent_qs.first()
                 
        new_comment.author = request.user
        new_comment.save()
        return redirect('savolho_detail', this_post.slug)
    else:
        comment_form = CommentForm()
    is_liked = False
    if this_post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'post':this_post,
        "is_liked": is_liked,
        'comments':comments, 
        'new_comment':new_comment, 
        'comment_form':comment_form,
        'total_likes': this_post.total_likes()}
    return render(request, 'questions/index_detail.html', context)

@login_required
def post_delete(request, pk):
    post = Savolho.objects.get(id=pk)
    if request.method == "POST" and post.author == request.user:
        post.delete()
        return redirect('index')
    return render(request, 'questions/post_deleted.html', {
        'post':post 
        })
    
@login_required
def add_savol(request):
    if request.method == 'POST':
        savolform = SavolForm(request.POST, request.FILES)
        if savolform.is_valid():
            new_savol = savolform.save(commit=False)
            new_savol.author = request.user
            new_savol.save()
            return HttpResponseRedirect('/')
    else:
        savolform = SavolForm()
    context = {'savolform':savolform}
    return render(request, 'questions/add_savol.html', context)

@login_required
def edit_savol(request, pk):
    article = Savolho.objects.get(id=pk)
    if request.method == "GET":
        article.author = request.user
        form = SavolEditForm(instance=article)
    else:
        form=SavolEditForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect("index")
    return render(request, 'questions/edit_savol.html',{
        'form':form
    })

def search(request):
    template_name = "search.html"
    query = request.GET.get("q")
    if query:
        queryset_list = Savolho.objects.filter(
            Q(title__icontains=query)|
            Q(savol__icontains=query))
        context = {
            'queryset_list': queryset_list
        }
        return render(request, template_name, context)

@login_required
def like_post(request):
    post = get_object_or_404(Savolho, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())
# Определение инфор по авторам