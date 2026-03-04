from django.urls import URLPattern, path
from Django.webapp.firstapp.models import reservation
from . import views

# We're adding this at app level, for this firstapp only
urlpatterns = [
    path('function', views.hello_word),
    path('class', views.HelloIndia.as_view()), # as_view is only for classes
    path('reservation', views.home),
]