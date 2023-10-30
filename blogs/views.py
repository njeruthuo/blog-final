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
        author = serializer.validated_data.get('author') or None

        if slug is None:
            slug = slugify(title)

        if author is None:
            author = self.request.user
        serializer.save(slug=slug, author=author)


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

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.slug:
            slug = slugify(instance.title)
        serializer.save(slug=slug)


blog_update_view = BlogUpdateView.as_view()
