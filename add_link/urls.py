from django.urls import path
from add_link.views import index, addlink_views, generate_link,  get_pdf
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", index, name="index"),
    path("addlink/", addlink_views, name="addlink"),
    path("linkem/<str:username>/", generate_link, name="generatelink"),
    path("get_pdf/<str:username>/", get_pdf, name="get_pdf"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)