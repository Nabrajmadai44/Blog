from django.urls import path
from blog_app import views

urlpatterns = [
    path("", views.post_list, name="post-list"),
    path("post_detail/<int:pk>/", views.post_detail, name="post-detail"),
    path("post_delete/<int:pk>/", views.post_delete, name= "post-delete"),
    path("draft_list", views.draft_list, name= "draft-list"),
    path("post_edit/<int:pk>/", views.post_edit, name = "post-edit"),
]
