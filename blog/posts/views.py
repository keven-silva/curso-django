from re import template
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from posts.models import Post
from django.db.models import Q, Count, Case, When

class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        qs = qs.annotate(
            comment_numbers=Count(
                Case(
                    When(comment__comment_publicated=True, then=1)
                )
            )
        )

        return qs


class PostSearch(PostIndex):
    pass


class PostCategory(PostIndex):
    template_name = 'posts/post_category.html'


class PostDetail(UpdateView):
    pass
