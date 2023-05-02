"""
Definition of urls for PskovskiyFootball.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('registration/',views.registration, name= 'registration'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('anketa/', views.anketa, name='anketa'),
    path('important/', views.important, name= 'important'),
    path('blog/', views.blog, name='blog'), #new
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'), #new
    path('newpost/', views.newpost, name= 'newpost'),
    path('videopost/', views.videopost, name='videopost'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
