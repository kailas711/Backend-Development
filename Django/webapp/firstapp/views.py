from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from streamlit import rerun
from urllib3 import HTTPResponse

from Django.webapp.firstapp.forms import ReservationForm
# Create your views here.

def hello_word(request):
    return HttpResponse("Hello Word")

class HelloIndia(View):
    def get(self, request):
        return HttpResponse("hello India")

def home(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HTTPResponse("Success")
    return render(request, 'index.html', {'form':form })