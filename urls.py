from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="root"),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('details/<int:id>', views.details, name="details"),
    path('movielist', views.movielist, name="movielist")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)