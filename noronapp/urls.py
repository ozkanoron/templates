from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('parallax', views.parallax, name="parallax"),
    path('blog', views.blogPage, name="blog-page"),
    path('blog2', views.blogPage2, name="blog-page2"),
    path('profile-page', views.profilePage, name="profile-page"),
    path('profile-page2', views.profilePage2, name="profile-page2"),
    path('404', views.error404, name="404-error"),
    path('email-template', views.emailTemplate, name="email-template"),
    path('cooking-landing-page', views.cookingLanding, name="cooking-landing-page"),
    path('home-desing-landing-page', views.homeLanding, name="home-desing-landing-page"),
    path('gallery', views.gallery, name="gallery"),

]