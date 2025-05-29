from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # یا هر view دیگری که داری
]
