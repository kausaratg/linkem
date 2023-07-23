from django.urls import path
from add_link.views import index, addlink_views, generate_link
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", index, name="index"),
    path("addlink/", addlink_views, name="addlink"),
    path("linkem/<str:username>/", generate_link, name="generatelink"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)