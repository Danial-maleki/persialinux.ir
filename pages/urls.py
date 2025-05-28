from django.urls import path
from . import views


urlpatterns=[
    path("" , views.Home.as_view() , name = 'home'),
    path("Os/" , views.Os.as_view() , name = 'discord'),
    path("contactus/" , views.Contactus.as_view() , name = 'contactus'),
    path("aboutus/" , views.Aboutus.as_view() , name = 'aboutus'),
    path("info/" , views.Info.as_view() , name = 'info'),
    path("learn/" , views.Learn.as_view() , name = 'learn'),
    path("chat/" , views.Chat.as_view() , name = 'chat'),
    path("wikilinux/" , views.Wikilinux.as_view() , name = 'wikilinux'),
    path("news/" , views.News.as_view() , name = 'news'),
    path('signup/' , views.SignupView.as_view() ,  name = 'signup'),
    path('logout/', views.logout_view, name='logout'),
]