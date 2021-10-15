from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'documentation/index.html')


@login_required
def nav_cms(request):
    return render(request, 'documentation/nav_cms.html')


@login_required
def users(request):
    return render(request, 'documentation/users.html')


@login_required
def profile(request):
    return render(request, 'documentation/profile.html')


@login_required
def messages(request):
    return render(request, 'documentation/messages.html')


@login_required
def business(request):
    return render(request, 'documentation/business.html')


@login_required
def social(request):
    return render(request, 'documentation/social.html')


@login_required
def nav_mod(request):
    return render(request, 'documentation/nav_mod.html')


@login_required
def password_page(request):
    return render(request, 'documentation/password_page.html')


@login_required
def schedule(request):
    return render(request, 'documentation/schedule.html')


@login_required
def image_docs(request):
    return render(request, 'documentation/image_docs.html')


@login_required
def blog(request):
    return render(request, 'documentation/blog.html')


@login_required
def job(request):
    return render(request, 'documentation/job.html')


@login_required
def event(request):
    return render(request, 'documentation/event.html')


@login_required
def landing(request):
    return render(request, 'documentation/landing.html')


@login_required
def seo(request):
    return render(request, 'documentation/seo.html')


@login_required
def analytics(request):
    return render(request, 'documentation/analytics.html')


@login_required
def security(request):
    return render(request, 'documentation/security.html')


@login_required
def technical(request):
    return render(request, 'documentation/technical.html')
