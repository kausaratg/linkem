from django.urls import path
from add_link.views import index, addlink_views

urlpatterns = [
    path("", index, name="index"),
    path("addlink/", addlink_views, name="addlink")
]