from django.urls import path
from add_link.views import index

urlpatterns = [
    path("", index, name="index")
]