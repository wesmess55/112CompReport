from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import BadHeaderError, EmailMessage
from .models import Movie, Genre
from .form import ContactForm
from django.conf.urls.static import static
# Create your views here.


def home(request):
    return render(request, 'index.html', {"title": "Welcome"})


def about(request):
    return render(request, 'about.html', {"title": "About"})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                email = EmailMessage(contact_name,
                                     content,
                                     contact_email,
                                     # change to your email
                                     ['youremail@gmail.com'],
                                     reply_to=[contact_email],
                                     )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, 'contact.html', {"title": "Contact", 'form': form})


def movielist(request):
    all_movies = Movie.objects.all()
    return render(request, 'movielist.html', {"title": "Movie List", "movies": all_movies})


def details(request, id):
    movies = Movie.objects.get(id=id)
    return render(request, 'details.html', {"title": "Movie Details", "movie": movies})