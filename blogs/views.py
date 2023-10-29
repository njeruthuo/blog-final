from .models import Blog
from rest_framework import generics
from .serializers import BlogSerializer

from django.utils.text import slugify


class BlogListView(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.published.all()


blog_list_view = BlogListView.as_view()


class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.published.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        slug = serializer.validated_data.get('slug') or None

        if slug is None:
            slug = slugify(title)
        serializer.save(slug=slug)


blog_create_view = BlogCreateView.as_view()


class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.published.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'


blog_delete_view = BlogDeleteView.as_view()


class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.published.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'


blog_update_view = BlogUpdateView.as_view()
