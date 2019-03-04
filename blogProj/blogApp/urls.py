from django.urls import path, include
from . import views

# to direct to functions
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),

]

