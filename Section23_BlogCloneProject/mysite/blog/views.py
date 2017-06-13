from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)

################################
##      Class Based Views     ##
################################

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    #if no template name is said here. The default one is post_list.html. It is just
    # the first and second words lower cased and with an underscore
    model = Post

    # Define how I want to grab this list
    def get_queryset(self):
        # This allow us to deal with django ORMs (Object-related models)
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
                                    # lte = Less Than or Equal to
                                    # for more info on it, look for "Field Lookups on django documentation:
                                    # https://docs.djangoproject.com/en/1.10/topics/db/queries/#field-lookups

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/' # if this person is not logged in, where should this person go? To login_url
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/' # if this person is not logged in, where should this person go? To login_url
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


################################
##        Function Views      ##
################################


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post # Remmembe here that our Comment object has an
                                #attribute called post of type Post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()  # This is a method under class Comment that approves it
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk # Note that you must save this variable before
                              # delete this comment. The reason is simple: if
                              # when you delete it, you do not have the post pk
                              # which the comment was referring to it
    comment.delete() # Delete the comment from my database
    return redirect('post_detail', pk=post_pk)


















































##
