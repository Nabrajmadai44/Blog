from django.urls import path
from blog_app import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("post_detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post_delete/<int:pk>/", views.PostDeleteView.as_view(), name= "post-delete"),
    path("draft_list", views.DraftListView.as_view(), name= "draft-list"),
    path("draft_detail/<int:pk>/", views.DraftDetailView.as_view(), name= "draft-detail"),
    path("draft_publish/<int:pk>/", views.DraftPublishView.as_view(), name = "draft-publish"),
    path("post_create/", views.PostCreateView.as_view(), name="post-create"),
    path("post_update/<int:pk>/", views.PostUpdateView.as_view(), name= "post-update")
]
