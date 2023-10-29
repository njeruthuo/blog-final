from django.urls import path
from . import views


urlpatterns = [
    path('blog_list_view/', views.blog_list_view),
    path('blog_create_view/', views.blog_create_view),
    path('blog_delete_view/<int:id>/', views.blog_delete_view),
    path('blog_update_view/<int:id>/', views.blog_update_view),
]

# localhost:8000/api/blog_list_view/
# localhost:8000/api/blog_create_view/
# localhost:8000/api/blog_delete_view/1/
# localhost:8000/api/blog_update_view/1/
