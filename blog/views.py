from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view

from .models import Post
from .forms import PostForm
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer


# class PostList(ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}
#
#
# @api_view(['GET', 'PUT'])
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)
#     # return render(request, 'blog/post_detail.html', {'post': post})
#
#
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render (request, 'blog/post_edit.html', {'form': form})
#
#
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def get_serializer_context(self):
        return {'request': self.request}


