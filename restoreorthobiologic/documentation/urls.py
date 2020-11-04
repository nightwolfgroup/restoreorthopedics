from django.urls import path
from documentation import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nav_cms/', views.nav_cms, name='nav_cms'),
    path('users/', views.users, name='users'),
    path('profile/', views.profile, name='profile'),
    path('messages/', views.messages, name='messages'),
    path('business/', views.business, name='business'),
    path('social/', views.social, name='social'),
    path('nav_mod/', views.nav_mod, name='nav_mod'),
    path('password_page/', views.password_page, name='password_page'),
    path('schedule/', views.schedule, name='schedule'),
    path('image_docs/', views.image_docs, name='image_docs'),
    path('blog/', views.blog, name='blog'),
    path('job/', views.job, name='job'),
    path('event/', views.event, name='event'),
    path('landing/', views.landing, name='landing'),
    path('seo/', views.seo, name='seo'),
    path('analytics/', views.analytics, name='analytics'),
    path('security/', views.security, name='security'),
    path('technical/', views.technical, name='technical'),
]