from django.shortcuts import render
from core.models import Fixture, Prediction

# Create your views here.
def index(request):
    fixtures = Fixture.objects.all()
    context = {
        'fixtures': fixtures,
    }
    return render(request, 'index.html', context)
