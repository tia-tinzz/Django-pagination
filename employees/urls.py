from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='indexpage'), # using function based view
    # path('', views.Index.as_view()), # using class based view
    path('home/',views.home,name="home")
]