from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.views import generic
from django.views.generic.edit import FormView
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "indexs.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['name'] = "ali"
        context['posts'] = Post.objects.all()
        return context


class PostList(LoginRequiredMixin, generic.ListView):
    queryset = Post.objects.all()
    # model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = "-id"

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post


# class PostCreateView(LoginRequiredMixin, FormView):
#     template_name = 'contact.html'
#     form_class = PostForm
#     success_url = '/blog/post/'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PstDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = "/blog/post/"


@api_view()
def api_post_list_view(request):
    return Response({"ok":"ali"})
