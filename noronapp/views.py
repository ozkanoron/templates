from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html", locals())


def parallax(request):
    return render(request, "parallax.html", locals())


def blogPage(request):
    return render(request, "blog-page.html", locals())


def blogPage2(request):
    return render(request, "blog-page2.html", locals())


def profilePage(request):
    return render(request, "profile-page.html", locals())


def profilePage2(request):
    return render(request, "profile-page2.html", locals())


def error404(request):
    return render(request, "error-page.html", locals())


def cookingLanding(request):
    return render(request, "cooking-landing.html", locals())


def homeLanding(request):
    return render(request, "home-landing.html", locals())


def gallery(request):
    return render(request, "gallery.html", locals())


def emailTemplate(request):
    return render(request, "email.html", locals())


